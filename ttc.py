a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))
        
        # Validate triangle inequality
if a <= 0 or b <= 0 or c <= 0:
    print("Error: Side lengths must be positive numbers.")
        
if a + b <= c or a + c <= b or b + c <= a:
    print("Error: The given side lengths do not form a valid triangle.")
       
        # Determine triangle type
if a == b == c:
    triangle_type = "Equilateral"
elif a == b or b == c or a == c:
    triangle_type = "Isosceles"
else:
    triangle_type = "Scalene"
        
    print(f"The triangle is {triangle_type}.")    

    print("Error: Please enter valid numbers.")

