n = int(input("Enter an integer:"))
temp = n
sum = 0
digits = len(str(n))

while n > 0:
  rem = n % 10
  sum = sum + rem ** digits
  n = n // 10
if temp == sum:
  print("Armstrong number")
else:
  print("Not an Armstrong number")
