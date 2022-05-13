# String with 6 separarate words
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# Splitting the string into a list of 6 elements using the ' ' space in between
# as a separator.
stuff = ten_things.split(' ')  # Stuff is the list of 6 items.
# An additional list with more list elements
more_stuff = ["Day", "Night", "Song",
              "Frisbee", "Corn", "Banana", "Girl", "Boy"]
# Loop that adds a popped item from the "more_stuff" list and assigns it to
# the variable "next_one"
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
