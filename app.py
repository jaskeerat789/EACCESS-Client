import requests
import time
import math
import sys

class EACESS():

    username=None
    header={
        "Host":"172.31.1.6:8090",
        "Accept": "*/*",
        "Accept-Language":"en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer":"https://172.31.1.6:8090/",
        "Content-Type":"application/x-www-form-urlencoded",
        "Content-Length": "79",
        "DNT":"1",
        "Connection":"keep-alive",
        }

    def get_time(self):
        return(math.floor(time.time()*1000))

    def login(self,username,password): 
        EACESS.username=username
        EACESS.header["content-lenght"]="79"
        loginData={
            "mode":191,
            "username":username,
            "password":password,
            "a":self.get_time(),
            "producttype":0
        }
        
        r=requests.post('https://172.31.1.6:8090/login.xml',data=loginData,verify=False,headers=EACESS.header)
        print(r.text)

    def logout(self,username=None):
        if username is None:
                username=EACESS.username
        print(username)
        logoutData={
            "mode":193,
            "username":username,
            "a":self.get_time(),
            "producttype":0
        }
        EACESS.header["content-lenght"]="57"
        r=requests.post("https://172.31.1.6:8090/logout.xml",data=logoutData,verify=False,headers=EACESS.header)
        print(r.text)




