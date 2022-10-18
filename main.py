
num1 = list(map(int, input('Enter first list').split()))
num2 = list(map(int, input('Enter second list').split()))

# ******************************
# Make your Code
# ******************************
if (len(num1) < len(num2)) or (len(num1)==len(num2)):
   num3 = num1 + num2
elif len(num2) < len(num1):
   num3 = num2 + num1   



print (num3) 
