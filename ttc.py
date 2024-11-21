a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))
        
if a <= 0 or b <= 0 or c <= 0:
    print("Error: Side lengths must be positive numbers.")
    
        #using inequlity theorem
if a + b <= c or a + c <= b or b + c <= a:
    print("Error: The given side lengths do not form a valid triangle.")
       
        # Determine triangle type
if a == b == c:
    print(f"The triangle is Equilateral.") 

elif a == b or b == c or a == c:
    print(f"The triangle is Isosceles.")  
    
else:    
    print(f"The triangle is Scalene.")    

if a + b + c >= 181:
    print('Invalid triangle sides')


