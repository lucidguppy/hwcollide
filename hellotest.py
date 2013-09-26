import threading
import requests
import time
import random
import string

class GetUrl(threading.Thread):
    def __init__(self, url):
        self.url = url
        threading.Thread.__init__(self)

    def run(self):
        resp = requests.get(self.url)
        #print(self.url, resp.status_code)
        if resp.status_code == 500:
            print(self.text)
        #print(resp.text)


now = time.time()
threads = [ GetUrl("http://pi:8888") for x in range(100) ]
for t in threads: t.start()
for t in threads: t.join()
print("Elapsed time tornado %s" % (time.time() - now))
now = time.time()
threads = [ GetUrl("http://pi:8080") for x in range(100) ]
for t in threads: t.start()
for t in threads: t.join()
print("Elapsed time cherrypy %s" % (time.time() - now))
