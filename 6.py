
num1 = 1
num2 = 100

for num in range(num1, num2 + 1):  
    if num > 1:  
        if all(num % i != 0 for i in range(num1, int(num ** 0.5) + 1)):  
            print(num)


num1 = 1
num2 = 100

for num in range(num1, num2 + 1):  
    if num > 1:  
        if all(num % i != 0 for i in range(num1,num)):  
            print(num)