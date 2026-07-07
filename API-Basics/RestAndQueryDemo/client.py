import requests 

r = requests.get("http://127.0.0.1:5000/books")

if r.status_code==200:
    print(r.json())
else:
    print("Issue retrieving information...")
