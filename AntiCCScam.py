#AntiCCScam
#Filip Rokita
#www.filiprokita.com



#import
import requests
import threading
from myconfig import *



#def
def do_request():
    while True:
        response = requests.post(url, headers=headers, data=data)
        print(response)



#main
threads = []
for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)
for i in range(50):
    threads[i].start()
for i in range(50):
    threads[i].join()