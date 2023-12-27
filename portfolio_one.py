from tabulate import tabulate

# printing welcome message
print("Welcome to Paws n Cart! \n")
# printing a border line
print('-' * 100)
# saying user that this is a shopping cart
print("This is your shopping cart: ")
print('-' * 100)
flag = True
list_of_items = []
list_of_price = []
while flag:
    print("Would you like to:\n"
          "1.Add an item to your cart\n"
          "2.Remove an item from your cart\n"
          "3.View the total cost of your cart\n"
          "4.Checkout")
    option = input("Enter the number of the option you would like to choose: ")
    if option != "":
        # logic to add item to the list
        if option == "1":
            item_number = input("Please enter an item number to add an item to your card form the below list :\n"
                                "1.Whiskers Cat Food\n"
                                "2.Kong\n"
                                "3.Lucerne Hay\n"
                                "4.Fish Food\n")
            if item_number != "":
                if item_number == "1" or item_number.lower() == "whiskers cat food":
                    list_of_items.append("Whiskers Cat Food")
                    option = ""
                    print("Whiskers Cat Food has been added to your cart successfully ")
                    list_of_price.append(input("Please enter the price of the item: "))
                elif item_number == "2" or item_number.lower() == "kong":
                    list_of_items.append("Kong")
                    option = ""
                    print("Kong has been added to your cart successfully ")
                    list_of_price.append(input("Please enter the price of the item: "))
                elif item_number == "3" or item_number.lower() == "lucerne hay":
                    list_of_items.append("Lucerne Hay")
                    option = ""
                    print("Lucerne Hay has been added to your cart successfully ")
                    list_of_price.append(input("Please enter the price of the item: "))
                elif item_number == "4" or item_number.lower() == "fish food":
                    list_of_items.append("Fish Food")
                    option = ""
                    print("Fish Food has been added to your cart successfully ")
                    list_of_price.append(input("Please enter the price of the item: "))
                else:
                    print("Please enter valid item number ")
            else:
                print("Please enter valid item number ")
        # logic to remove item from list
        if option == "2" and len(list_of_items) != 0:
            item_number = input("Please enter an item number to remove an item from your card form the below list:\n"
                                "1.Whiskers Cat Food\n"
                                "2.Kong\n"
                                "3.Lucerne Hay\n"
                                "4.Fish Food\n")
            if item_number != "":
                if item_number == "1" or item_number.lower() == "whiskers cat food":
                    index = list_of_items.index("Whiskers Cat Food")
                    list_of_items.pop(index)
                    list_of_price.pop(index)
                    option = ""
                    print("Whiskers Cat Food has been removed from your cart successfully ")
                elif item_number == "2" or item_number.lower() == "kong":
                    index = list_of_items.index("Kong")
                    list_of_items.pop(index)
                    list_of_price.pop(index)
                    option = ""
                    print("Kong has been removed from your cart successfully ")
                elif item_number == "3" or item_number.lower() == "lucerne hay":
                    index = list_of_items.index("Lucerne Hay")
                    list_of_items.pop(index)
                    list_of_price.pop(index)
                    option = ""
                    print("Lucerne Hay has been removed from your cart successfully ")
                elif item_number == "4" or item_number.lower() == "fish food":
                    index = list_of_items.index("Fish Food")
                    list_of_items.pop(index)
                    list_of_price.pop(index)
                    option = ""
                    print("Fish Food has been removed from your cart successfully ")
                else:
                    print("Please enter valid item number ")
            else:
                print("Make sure your cart is not empty and you have entered valid item number  ")
        # logic to view cart and total amount
        if option == "3":
            print('-' * 100)
            print("This is your shopping cart: ")
            for count, item in enumerate(list_of_items):
               # print(tabulate([[item, list_of_price[count]]], tablefmt="plain"))
                print(f"{item} \t {list_of_price[count]}")
            total = 0
            for price in list_of_price:
                total = total + int(price)
            print(f"The total amount you need to pay is : {total}")
            option = ""
            print('-' * 100)
        # logic to checkout
        if option == "4":
            print('-' * 100)
            print("Thank you for shopping with Paws n Cart ")
            option = ""
            print('-' * 100)
            # flag = False
    else:
        print("Please enter valid option ")
        option = ""
