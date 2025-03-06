total_discount_sum = 0

response = input("Do you want to enter an order? (Yes/No): ").strip().lower()

while response == "yes":
    quantity = int(input("Enter quantity of item: "))
    price = float(input("Enter price per item: "))

    extended_price = quantity * price

    if extended_price > 10000:
        discount_rate = 0.25
    else:
        discount_rate = 0.10

    discount_amount = extended_price * discount_rate
    total_price = extended_price - discount_amount

    print("Extended Price: $", round(extended_price, 2))
    print("Discount Amount: $", round(discount_amount, 2))
    print("Total Price after Discount: $", round(total_price, 2))

    total_discount_sum += discount_amount

    response = input("Do you want to enter another order? (Yes/No): ").strip().lower()

print("Total Discounts Given: $", round(total_discount_sum, 2))
