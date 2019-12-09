#coding=utf-8
import requests
import sys

print("Example: https://www.example.com")
print()
print()

while 1:
    url = input("url:")

    r = requests.get(url)
    status = str(r.status_code)
    print('GET==> ' + status)

    r = requests.post(url)
    status = str(r.status_code)
    print('POST==> ' + status)
    
    r = requests.put(url)
    status = str(r.status_code)
    print('PUT==> ' + status)
    
    r = requests.delete(url)
    status = str(r.status_code)
    print('DELETE==> ' + status)
    
    r = requests.head(url)
    status = str(r.status_code)
    print('HEAD==> ' + status)
    
    r = requests.options(url)
    status = str(r.status_code)
    print('OPTIONS==> ' + status)

    print()
    print("CHECK OVER!")
    print()
