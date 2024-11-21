units = float(input("Units Consumed: $"))
fixed_meter_charge = 50
if units <= 100:
   price_per_unit = 0.50
elif units <= 300:
   price_per_unit = 0.75
else:
   price_per_unit = 1.20

if units < 0:
      print("Unit Error!")     
      
meter_charge = units * price_per_unit + fixed_meter_charge
print(f'Total Bill ($50 Meter_charge included): ${meter_charge:.2f}')        
      