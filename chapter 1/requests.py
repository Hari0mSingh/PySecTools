# some important libraries in python

# requests module

import requests

# making get request

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print("status code : ",response.status_code)
print('\n')
print("content :",response.content)
print('\n')
print("headers",response.headers)
print('\n')
print("text",response.text)
print('\n')
print("json",response.json())
print('\n')
print("url",response.url)
print('\n')
print("cookie",response.cookies)
print('\n')
print('\n')

#making a POST request

data = {"userId":2,"id":2,"title":"Hello from Hariom Singh","body":"vrevecjvcdsuycvdsycdvc"}

response1=requests.post("https://jsonplaceholder.typicode.com/posts",json=data)

print(response1.status_code)
print("\n")
print(response1.json())
print('\n')


# Session management {Create a session object}
session  = requests.session()

session.get('https://httpbin.org/cookies/set/sessioncookie/123456789')

response3 = session.get('https://httpbin.org/cookies')

print("content : ",response3.content)
print('\n')
print(response3.json())