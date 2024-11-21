weight = float(input('Enter your weight in kgs: '))
height = float(input('Enter your height in meters: '))

bmi = weight / (height **2)
if weight == 0 or height ==0:
    print('Oops: Enter a positive value and try again...')
elif weight <= 0 or height <= 0:
    print('Error!!!: Enter a positive value')    


if bmi < 18.5:
    print(f'Your BMI is{bmi:.2f}. You are classified as: Underweight.')  
elif 18.5 <= bmi <25:
    print(f'Your BMI is{bmi:.2f}. You are classified as: Normal weight.')    
elif 25 <= bmi <30:
    print(f'Your BMI is{bmi:.2f}. You are classified as: Overweight.')    
else: 
    print(f'Your BMI is{bmi:.2f}. You are classified as: Obesity.') 



