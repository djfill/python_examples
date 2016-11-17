
num =input('Enter an Integer:')

def square(num):
   if not num.isdigit():
      return 'Invalid Entry'
   num = int(num)
   return num * num

print(num , 'Squared is:',square(num))

