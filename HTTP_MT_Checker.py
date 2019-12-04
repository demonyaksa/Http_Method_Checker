#coding=utf-8
import requests
import sys

print("Example: https://www.example.com")
print()
print()

url = input("url:")

r = requests.get(url)
if r.status_code == 200:
    print('surport: GET')

r = requests.post(url)
if r.status_code == 200:
    print('surport: POST')
    
r = requests.put(url)
if r.status_code == 200:
    print('surport: PUT')
    
r = requests.delete(url)
if r.status_code == 200:
    print('surport: DELETE')
    
r = requests.head(url)
if r.status_code == 200:
    print('surport: HEAD')
    
r = requests.options(url)
if r.status_code == 200:
    print('surport: OPTIONS')

print()
print("CHECK OVER!")
input()
