purchase_price = float(input("Enter purchase price: $"))
if purchase_price < 100: 
        discount_rate = 0
elif 100 <= purchase_price <= 500:
        discount_rate = 0.10
else: 
        discount_rate = 0.20
#to calculate discount and discounted price
discount = purchase_price * discount_rate 
discounted_price = purchase_price - discount 
#to determine the tax rate
if discounted_price < 200:
        tax_rate = 0.05
else:
        tax_rate = 0.08 
#to calculate tax and final price 
tax = discounted_price * tax_rate
final_price = discounted_price + tax

print("\n--- Summary ---")
print(f"Original purchase price: ${purchase_price:.2f}") 
print(f"Discount applied: ${discount:.2f}({discount_rate*100:0f}%)")
print(f"Tax applied: ${tax:.2f}({tax_rate*100:.0f}%)")
print(f"Total price to pay: ${final_price:.2f}")

    
