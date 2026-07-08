import requests 

r = requests.get("http://127.0.0.1:5000/books") #retrieving all books info

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
    idlist = [book["id"] for book in s] #list of ids

    new_book = {"id": max(idlist)+1, "title": title, "category": category, "price": int(price), "stock": int(stock)}

    s = requests.post("http://127.0.0.1:5000/books",json=new_book) #adding new book

    if s.status_code==201:
        print(s.text) #printing server's reply
    else:
        print("Error adding new book record !")
elif choice=="n":
    pass
else:
    print("Invalid input !")



choice = input("Do you want to update any book record ? (y/n)\n")

if choice=="y":
    book_id = input("Enter book id : ")
    field = input("Enter p to update a price field, s for a stock field or b for both : ") #client can update only the price or/and stock fields
    
    if field=="p":
        new_price = int(input("Enter new price : "))
        update_data = {"price": new_price}
        t = requests.patch(f"http://127.0.0.1:5000/books/{book_id}", json=update_data) #updating book field/s
        print(t.json()) #printing server's reply on the operation
    elif field=="s":
        new_stock = int(input("Enter new stock : "))
        update_data = {"stock": new_stock}
        t = requests.patch(f"http://127.0.0.1:5000/books/{book_id}", json=update_data)
        print(t.json()) 
    elif field=="b":
        new_price = int(input("Enter new price : "))
        new_stock = int(input("Enter new stock : "))
        update_data = {"price": new_price, "stock": new_stock}
        t = requests.patch(f"http://127.0.0.1:5000/books/{book_id}", json=update_data)
        print(t.json())
    else:
        print("Invalid field choice!")

elif choice=="n":
    pass
else:
    print("Invalid input !")



choice = input("Do you want to delete any book record ? (y/n)")

if choice=="y":
    book_id = input("Enter book id : ")

    u = requests.delete(f"http://127.0.0.1:5000/books/{book_id}") #deleting book record

    print(u.json()) #printing server's reply on the operation
elif choice=="n":
    pass
else:
    print("Invalid input !")