import mystuff

mystuff.apple()

print(f'A tangerine in darija is {mystuff.tangerine}')

# Comparision between how Dictionaries work and module importation
# mystuff['apple'] -> Get apple's value from dictionary called mystuff.
# mystuff.apple() -> Call apple() Function from mystuff.py module.
# mystuff.tangerine -> Gets the variable tangerine from module mystuff.

# we have a very common pattern in Python: 1. Take a key=value style container.
# 2. Get something out of it by the key’s name.
# In the case of the dictionary, the key is a string and the syntax is [key]. In the
# case of the module, the key is an identifier, and the syntax is .key. Other than
# that they are nearly the same thing.

print('-'*10)
print('Classes')
print('-'*10)
# Classes are like Modules?


class MyStuff(object):
    def __init__(self):  # For If we wanna call a variable from the class: Class.variable
        self.tangerine = "I'm small and orange."
        self.naranga = "I'm a a big tangerine!"

    def apple(self):
        print("I AM A CLASSY APPLE!")

    def orange(self, use, taste):
        print(f"I'm an orange. I'm used for {use}, and I taste so {taste}.")

# How to Instantiate a class.


thing = MyStuff()

print(thing.tangerine)
print(thing.naranga)
thing.apple()
thing.orange('eating', 'sweet')


# class fruits(object):
#    def __init__(self, one, two, three):
#        self.one = one
#        self.two = two
#        self.three = three
#
#    def salade(one, two, three):
#       print(f'The salade has {one}, {two}, and {three}.')


print('-'*10)

# fruits.salade('Banana', 'Strawberry', 'Melon')

#Chlada = fruits.salade('Banana', 'Batata!', 'Zaaboul')
