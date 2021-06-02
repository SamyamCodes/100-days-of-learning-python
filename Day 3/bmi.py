height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))👆
bmi=round(weight/height**2)

if bmi <18.5:
  print(f"Your bmi has{bmi}value and you are underweight. ")
elif bmi <25:
  print(f"Your bmi has {bmi}value and you have a normal weight")
elif bmi<30:
  print(f"Yoyr bmi value is {bmi} and you are slightly overweight")
elif bmi<35:
  print(f"Your bmi value is {bmi} and you aare obese ")
else:
  print(f"Your bmi value is {bmi} and you are cliniclly obese.")
  








