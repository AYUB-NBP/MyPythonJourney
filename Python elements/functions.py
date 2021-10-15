def square(x):
    return x * x


y = int(input("Please type an interger: "))

result = square(y)

print(f"The square of {y} is "+ str(result))

for i in range(11):
    print(f"The square of {i} is {square(i)}")

#Whatever function I make can be imported from this file 
# as a module in another .py file.