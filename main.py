print("Rezwana Sultana \n")

#1. Make a code that will take the input of two strings. If the two inputs are the same, your program will print “SAME”. If Not, It should show “NOT Same” and check which one is greater and print that.
A = input("input the 1st string: ")
B = input("input the 2nd string: ")
if A == B:
  print("SAME")
else:
  print("NOT Same")
  if A > B:
    print("A is greater than B.")
  else:
    print("B is greater than A.")
print("\n")

#2. Make a calculator, which will work as the following algorithm:
#a.Input 1st Number
#b.Input What you want to do with numbers (+, -, *, or /)
#c.Input 2nd Number
#d.Do calculation
#e.Show Result'''
x = float(input("Please input the 1st number: "))
y = input("Please input What you want to do with numbers (+, -, *, or /): ")
z = float(input("Please input the 2nd number: "))

if y == "+":
  addition = x + z
  print(x, '+', z, '=', addition)
elif y == "-":
  subtraction1 = x - z
  subtraction2 = z - x
  if x > z:
    print(x, '-', z, '=', subtraction1)
  else:
    print(z, '-', x, '=', subtraction2)
elif y == '*':
  multiplication = x * z
  print(x, 'x', z, '=', multiplication)
elif y == '/':
  if z == 0:
    print("SYNTAX ERROR")
  else:
    division = x / z
    print(x, '/', z, '=', division)
print("\n")

#3.Rainfall = [22, 3.4, 1, 8, 19, 21]
#From the above rainfall data, Find the average rainfall of that area.
#Total_rainfall= 22+3.4+1+8+19+21
#print(Total_rainfall)
Rainfall = [22, 3.4, 1, 8, 19, 21]
n = 5
Total_Rainfall = sum(Rainfall)
Avg_Rainfall = Total_Rainfall/n
print("Average rainfall is: ", Avg_Rainfall, "mm")
print("\n")

#4. A school has the following rules for the grading system:
#  a. Below 25 - F
#  b. 25 to 45 - E
#  c. 45 to 50 - D
#  d. 50 to 60 - C
#  e. 60 to 80 - B
#  f. Above 80 – A
#Ask the user to enter marks and print the corresponding grade.
x = float(input("Please input the number: "))
if x < 25:
    print("F")
elif (x >= 25 and x <= 45):
    print("E")
elif (x >= 45 and x <= 50):
    print("D")
elif (x >= 50 and x <= 60):
    print("C")
elif (x >= 60 and x <= 80):
    print("B")
elif (x > 80):
    print("A")