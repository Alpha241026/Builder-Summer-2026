import requests 

r = requests.get("http://127.0.0.1:5000/books")

if r.status_code==200:
    print(r.json())
else:
    print("Issue retrieving information...")

choice = input("Do you want to enter a new book record ? (y/n)\n")

if choice=="y":
    title = input("Enter title : ")
    category = input("Enter category : ")
    price = input("Enter price : ")
    stock = input("Enter stock : ")
    s = r.json()
    idlist = [book["id"] for book in s]

    new_book = {"id": max(idlist)+1, "title": title, "category": category, "price": int(price), "stock": int(stock)}

    r = requests.post("http://127.0.0.1:5000/books",json=new_book)

    if r.status_code==201:
        print(r.text)
    else:
        print("Error adding new book record !")
        
elif choice=="n":
    pass
else:
    print("Invalid input !")