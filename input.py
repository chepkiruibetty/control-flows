def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        # Subtract the discount amount from the original price
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price


# Prompt the user to enter the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Ensure the discount percentage is valid
    if discount_percentage < 0:
        print("Discount percentage cannot be negative.")
    else:
        # Calculate and print the final price
        final_price = calculate_discount(original_price, discount_percentage)
        print(f"The final price after applying the discount is: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numeric values.")
