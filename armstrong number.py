new_num = int(input("Enter a number: "))

i = 0

result = new_num

while result > 0:

   new_digit = result % 10

   i += new_digit ** 3

   result //= 10

if new_num == i:

   print(new_num," It is an Armstrong number")

else:

   print(new_num," It is not an Armstrong number") 
