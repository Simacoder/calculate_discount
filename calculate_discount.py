# function to calculate discount 

# global variables
price = float(input("enter the price: "))
discount_percent = int(input("Enter discount percentage:"))


def calculate_discount(price, discount_percent):
    # local variables
    # new_price
    
    if discount_percent >= 20:
        discount_percent = discount_percent / 100
        discount = discount_percent * price
        new_price = price - discount
        print(f"The discount is {discount_percent}, and new price is R{new_price} Thanks for shopping with us.")
    else:
        print(f"The percentage {discount_percent}% is too low , the {price} is the origianl price. Thanks for shoppign with us.")

calculate_discount(price, discount_percent)