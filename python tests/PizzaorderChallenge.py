print("Place Order Here")

size = input("Chooss Size: Small $15, Medium $20, Large $25: ")
pepperoni = input("Do you want to add pepperoni?: ")
cheese = input("Do you want extra cheese?: ")
bill = 0

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
        if cheese == "Y":
            bill += 1
            print(f"Your bill is, ${bill}")
    else:
        print(f"Your bill is, ${bill}")
if size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
        if cheese == "Y":
            bill += 1
            print(f"Your bill is, ${bill}")
    else:
        print(f"Your bill is, ${bill}")
if size == "L":
    bill += 25
    if pepperoni == "Y":
        bill = 3 + 25
        if cheese == "Y":
            bill += 1 
            print(f"Your bill is, ${bill}")
    else:
        print(f"Your bill is, ${bill}")

    
    

