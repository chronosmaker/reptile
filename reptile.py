#!/usr/bin/python 
#coding:utf-8

import requests
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

LOGIN_URL = 'http://www.cfdport.com/ec/jsp/logIn.jsp'
LOGIN_DATA = {'action': 'login', 'uname': 'huzichedui', 'pwd': '123456'}

SEARCH_URL = 'http://www.cfdport.com/ec/jsp/statistics/statisticscartimes.jsp'
SEARCH_DATA = {'starttime': '2017-09-01 07:30:00', 'endtime': '2017-09-05 07:30:00'}

SEARCH_STR = 'xxxx(.*?)</tr>'

def Get_Session(URL, DATA, HEADERS):
    ROOM_SESSION = requests.Session()
    ROOM_SESSION.post(URL, data=DATA, headers=HEADERS)
    return ROOM_SESSION


SESSION = Get_Session(LOGIN_URL, LOGIN_DATA, HEADERS)


RES = SESSION.post(SEARCH_URL, data=SEARCH_DATA, headers=HEADERS)
RES.encoding = 'utf-8'


array = re.findall(SEARCH_STR, RES.text, re.S)  

for s in array:
    s = re.sub(r'<(.*?)>|\t', "", s)
    s = re.sub(r'\r|\n|&nbsp;', " ", s)
    print (s)  
 