import requests #importing library for http operations

#asking for the username to search
username = input("\nHi! Welcome to GitHub User Info Finder! Please enter the username to fetch their information - ")

r = requests.get(f"https://api.github.com/users/{username}", timeout=10) #retrieving data of mentioned username from GitHub

if r.status_code==200: #if user exists
    
    s = r.json() #storing the data as a dictionary
    print(f"Name : {s["name"]}\nEmail (can be None if not public): {s["email"]}\nBio : {s["bio"]}\nPublic Repos : {s["public_repos"]}\nFollowers : {s["followers"]}\nFollowing : {s["following"]}")

elif r.status_code==403: #rate limiting
    print("\nGitHub API request limit exceeded (60/hour)")

else:
    print("Sorry the requested user doesn't exist")
