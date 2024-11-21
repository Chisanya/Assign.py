print("WELCOME")
purchase_price = float(input("Enter purchase price: $"))
if purchase_price < 100: 
        discount_rate = 0
elif    purchase_price <= 500:
        discount_rate = 0.10
else: 
        discount_rate = 0.20

discount = purchase_price * discount_rate 
discounted_price = purchase_price - discount 

if discounted_price < 200:
        tax_rate = 0.05
else:
        tax_rate = 0.08 
 
tax = discounted_price * tax_rate
final_price = discounted_price + tax

print("\n--- Summary ---")
print(f"Original purchase price: ${purchase_price:.2f}") 
print(f"Discount applied: ${discount:.2f}({discount_rate*100:.0f}%)")
print(f"Tax applied: ${tax:.2f}({tax_rate*100:.0f}%)")
print(f"Total price to pay: ${final_price:.2f}")


# purchase_amount = float(input('Enter purchase amount: $'))
# if purchase_amount < 100:
#         discount = 0
#         print('No discount')
# elif purchase_amount <= 500:
#         discount = 0.1 * purchase_amount
#         print(f'10% discount: ${discount:.2f}')
# else:
#         discount = 0.2 * purchase_amount
#         print(f'20% discount: ${discount:.2f}')

# discount_amount = purchase_amount - discount
# if discount_amount <200:
#         tax = 0.05 * discount_amount
#         print(f'5% tax: ${tax:.2f}')
# else:
#         tax = 0.08 * discount_amount
#         print(f'8% tax: ${tax:.2f}') 
# final_amount = discount_amount + tax
# print(f'Final amount: ${final_amount:.2f}')                               
