# Multi-line statement
a = 1 + 2 + 3 + \
4 + 5 + 6

print('{} is equal to'.format(a))

# Multi-line strings
''' This is a long comment
which extends up to a second line '''

# for loop
for i in range(1, 11):
    print('{} iteration'.format(i))
    if i == 5:
        break

# Function with doccstring
def double(num):
    """ Function to double the value """
    return 2*num

print(double.__doc__)

# Numeric literals
a = 0b1010 # binary literals
b = 100 #decimal literals
c = 0o310 #octal literals
d = 0x12c #Hexadecimal literals

# Float literal
float_1 = 10.5
float_2 = 1.5e2

# Complex literals
x = 2 + 3.14j

for i in [a, b, c, d, float_1, float_2, x]:
    print("literal : {}, type : {}".format(i, type(i)))

# None literals
food = None

# collections
print('*** Now tackling the collections')
fruits = ["apple", "mango", "grapefruit"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple','b':'bug','c':'character'} #dictionary
vowels = {'a', 'e', 'i', 'o', 'u', 'y'} #set
print(fruits)
print(numbers)
print(alphabets)
print(vowels)

# Manipulation lists
print('*** Collection type 1 : list')
print(fruits[0])
print(fruits[0:2])
print(fruits[1:3])

# Manipulating tuples
print('*** Collection type 2 : tuple')
print('Note : tuples are the same as lists, but immutable')
print(numbers[0:2])

# Manipulating sets
print('*** Collection type 3: set')
print(vowels)
vowels.add('a')
vowels.add('m')
print(vowels)

# Playing with print
print(1,2,3,4)

# Playing with inputs
print('*** Now with the inputs')
num = input('Enter a figure between 1 and 10 \n')

print('Voici sa racine carree : {}'.format(num**2))
