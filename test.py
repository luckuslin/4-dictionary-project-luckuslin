
amazon = [
    {"name": "SAMSUNG 32-Inch Class Full HD F6000 Smart TV","price": 127.99,"catergory": "Electronics"},
    {"name": "Xbox Series X 1TB Gaming Console Console", "price": 670, "catergory": "Electronics",},
    {"name": "Dining Table Set for 4","price": 251.10,"catergory": "Home & Kitchen",},
    {"name": "Bounty Quick Size Paper Towels, White, 8 Family Rolls","price": 24.42,"catergory": "Health & Household",},
    {"name": "TERRO Ant Killer Bait Stations T300B","price": 11.97,"catergory": "Garden & Outdoor"},
    {"name": "Apple AirPods 4 Wireless Earbuds, Bluetooth Headphones" ,"price": 99.99, "catergory:": "Electronics"}
]

#Finished Part 2(Somehow more unoptimized)
def asdfhjlalsdkjfhlaskdjhflajsdhflajsdhfljasdfasldjflasdlfaldshfkajdhfjhdffhjffhdjfhdjfhdjhfjadladkjfhqoeiwuryqweoiuryqew7yteryetyeryetr53634653463476514545345hcbbcnbvcnnbvbkuktuutktukuyyrqeywuryqewoyruqeowyrwqrbbcxvnzxbczxvcxbvbzxbvznxbvvbx():
    for index, item in enumerate(amazon):
            print(index, ":", item["name"], ":", item["price"])
            order=[]
    while True:
        cart=int(input("What Will You Order Today? If Done, Write 10:"))

        if cart == 0:
            samsung=input("Will you order the SAMSUNG 32-Inch Class Full HD F6000 Smart TV for 127.99? Y/N:")
            if samsung == "Y" or "y":
                    print("Added To Cart!")
                    order.append("SAMSUNG 32-Inch Class Full HD F6000 Smart TV:127.99")
            else :
                    print("Canceled order")
        elif cart == 1:
            console=input("Will you order the Xbox Series X 1TB Gaming Console Console for 670? Y/N:")
            if console == "Y" or "y":
                print("Added To Cart!")
                order.append("Xbox Series X 1TB Gaming Console Console:670")
            else :
                print("Canceled order")
        elif cart == 2:
            table=input("Will you order Dining Table Set for 4 for 251.10? Y/N:")
            if table == "Y" or "y":
                print("Added To Cart!")
                order.append("Dining Table Set for 4: 251.10")
            else :
                print("Canceled order")
        elif cart == 3:
            Bounty=input("Will you order the Bounty Quick Size Paper Towels, White, 8 Family Rolls for 24.42? Y/N:")
            if Bounty == "Y" or "y":
                    print("Added To Cart!")
                    order.append("Bounty Quick Size Paper Towels, White, 8 Family Rolls:24.42")
            else :
                    print("Canceled order")
        elif cart == 4:
            Ant_Bait=input("Will you order the TERRO Ant Killer Bait Stations T300B for 11.97? Y/N:")
            if Ant_Bait == "Y" or "y":
                    print("Added To Cart!")
                    order.append("TERRO Ant Killer Bait Stations T300B:11.97")
            else :
                    print("Canceled order")
        elif cart == 5:
            Airpods=input("Will you order the Apple AirPods 4 Wireless Earbuds, Bluetooth Headphones for 99.99? Y/N:")
            if Airpods== "Y" or "y":
                    print("Added To Cart!")
                    order.append("Apple AirPods 4 Wireless Earbuds, Bluetooth Headphones: 99.99")
            else :
                    print("Canceled order")
        elif cart == 10:
              bigcart = input("Do You Wish to Continue? Yes/No:")
              if bigcart == "Yes":
                    print("You Have Ordered:")
                    for i in order:
                          print(i)
                    print("Thank You for Shopping With Us!")
                    break
            
asdfhjlalsdkjfhlaskdjhflajsdhflajsdhfljasdfasldjflasdlfaldshfkajdhfjhdffhjffhdjfhdjfhdjhfjadladkjfhqoeiwuryqweoiuryqew7yteryetyeryetr53634653463476514545345hcbbcnbvcnnbvbkuktuutktukuyyrqeywuryqewoyruqeowyrwqrbbcxvnzxbczxvcxbvbzxbvznxbvvbx()







#First part finished (Unoptimized)
""" for index, item in enumerate(amazon):
    print(index, ":", item["name"], item["price"])
purchase=int(input("What Will you Order today? Pick the number:"))
for index, item in enumerate(amazon):
    print(index, ":", item["name"], item["price"])
   
if purchase == 0:
    tv=input("Will you order the SAMSUNG 32-Inch Class Full HD F6000 Smart TV for 127.99? Y/N:")
    if tv == "Y":
        print("Purchase Accepted!")
    else :
        print("Canceled order")
elif purchase == 1:
    xbox=input("Will you order the Xbox Series X 1TB Gaming Console Console for 670? Y/N:")
    if xbox == "Y":
        print("Purchase Accepted!")
    else :
        print("Canceled order")
elif purchase == 2:
    table=input("Will you order Dining Table Set for 4 for 251.10? Y/N:")
    if table == "Y":
        print("Purchase Accepted!")
    else :
        print("Canceled order")
elif purchase == 3:
    Bounty=input("Will you order the Bounty Quick Size Paper Towels, White, 8 Family Rolls for 24.42? Y/N:")
    if Bounty == "Y":
        print("Purchase Accepted!")
    else :
        print("Canceled order")
elif purchase == 4:
    Ant_Bait=input("Will you order the TERRO Ant Killer Bait Stations T300B for 11.97? Y/N:")
    if Ant_Bait == "Y":
        print("Purchase Accepted!")
    else :
        print("Canceled order")
elif purchase == 5:
    Airpods=input("Will you order the Apple AirPods 4 Wireless Earbuds, Bluetooth Headphones for 99.99? Y/N:")
    if Airpods== "Y":
        print("Purchase Accepted!")
    else :
        print("Canceled order")
elif purchase <= 6:
    print("Try again") """

