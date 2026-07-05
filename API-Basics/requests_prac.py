import requests #importing request module

r = requests.get('https://api.github.com/events') #getting a webpage

r = requests.post('https://httpbin.org/post', data={'key': 'value'}) #post request

r = requests.put('https://httpbin.org/put', data={'key': 'value'}) #put request

r = requests.delete('https://httpbin.org/delete') #delete request

payload1 = {'key1': 'value1', 'key2': 'value2'} #demo data to send in url's query string
r = requests.get('https://httpbin.org/get', params=payload1)

print(r.url)

payload2 = {'key1': 'value1', 'key2': ['value2', 'value3']} #demo data having a list of items as well
r = requests.get('https://httpbin.org/get', params=payload2)
print(r.url)

print(r.text) #reading content of server's response

print(r.encoding) #to find out what encoding requests is using

print(r.content) #accessing the response body as bytes, for non-text requests

print(r.status_code) #to check if a request was really successful...as some servers may return json object in a failed response, so r.json() isnt necessarily a perfect indicator of response success 
if r.status_code == 200:
    print(r.json()) #accessing response for json data
else:
    print("Request failed, skipping JSON parse")

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'} #adding custom HTTP headers to a request by passing in a dict to the headers parameter
r = requests.get(url, headers=headers)

print(r.headers) #viewing server's response headers

requests.get('https://github.com/', timeout=0.001) #an exception is raised if the server has not issued a response for timeout seconds (more precisely, if no bytes have been received on the underlying socket for timeout seconds). If no timeout is specified explicitly, requests do not time out

#note that r.history shows the chain of redirects if a URL forwarded you somewhere else

#The Session object allows you to persist certain parameters across requests...it also persists cookies across all requests made from the Session instance; so if you’re making several requests to the same host, the underlying TCP connection will be reused, which can result in a significant performance increase
s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')

print(r.text)


#From time to time you may be working with a server that, for whatever reason, allows use or even requires use of HTTP verbs not covered above. One example of this would be the MKCOL method some WEBDAV servers use. Do not fret, these can still be used with Requests. These make use of the built-in .request method. For example:
data = {'key': 'value'}
r = requests.request('MKCOL', 'https://httpbin.org/anything', data=data)
print(r.status_code)