###define the menu restaurant
menu 
{
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'coffee': 80,


}

print("WELCOME OUR RESTAURant")
print("what would you like to have ")
print("pizza: Rs40\n pasta: Rs80\n burger: Rs70\n salad: Rs30\n  ")


order_total = 0

item_1 = input("Enter the name of item you want to order")
if item_1 in menu:
    order_total += menu[item_1]
    print("your item {item_1}   has been added to your order")


else:
    print("ordered item {item_1} is not avaialable yet!")

another_order = input("do you want to add another item?(yes/no)")
if another_order=="yes":
    item_2 = input("Enter the second number of a item")
    if item_2 in Menu:
        order_total += menu[item_2]
print(f"item {item_2 } has been added to order")

else:
print(f"ordered item {item_2} is not avaiable")

print("the total amount of item to pay is {order_total}")
