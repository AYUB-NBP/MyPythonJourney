types_of_people = 10 #Numeric Value in a variable formated in another string x
x = f"There are {types_of_people} types of people."
# 2 variables with string value formated in a variable with string y
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
#Printing two variables with other variables 
# inside formated strings that...stringception
print(x)
print(y)

print(f"I said {x}")
print(f"I also said:'{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny! {}"
#Printing a varibale with string that has a {} using the format function 
#that takes a parameter of (hilarious) which is another variable containing a 
# Boolean value, but appears as a string
print(joke_evaluation.format(hilarious))
#Print a string using a function that fills {} with the parammeter given to it.
w = "This is the left side of..."
e = "a string with a right side."
# Concatenation
print(w+e)
