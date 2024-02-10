num = int(input("Enter a number : "))
sum = 0
remainder = 0
temp = num

while(temp > 0):
    remainder = temp % 10
    sum = sum + pow(remainder,len(str(num)))
    temp = temp//10

if(num == sum):
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")