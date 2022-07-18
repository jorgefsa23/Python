# ONE-LINERS

'''List of one-line codes

Strategy to shorter and readable Python code
Source: Own adaptation based on a List with 56 Python one-liners: https://blog.finxter.com/python-one-liners/
'''

# 1) IF-ELSE: 
score = 12
winner = "Great! Scored more than 10!"
looser = "Bad! Scored less than 10"
print(winner) if score >= 10 else print(looser)

#2) ELIF:
price = 99
print('no') if price> 100 else print("yes") if price==99 else print("maybe")

#3) Lambda funcion (anonimous fuctions)
square = lambda x: x**2
print(square(3))

#4) FOR loop
for i in range(10): print(i)

#5) FOR loop IF (list comprehension #1)
pairs_squared = [i**2 for i in range(10) if i%2==0]
print(pairs_squared)

#6) While
c = 20
while c < 30: print(c); c = c + 1

#7) List comprehension (here creating a new list from another)
#syntax: [expression for item in list]
teams = ['liverpool', 'valencia', 'manchester united', 'ac milan']
teams_cap = [team.title() for team in teams]
print(teams_cap)

#8) Dictionary Comprehension
#syntax: {key: value for key, value in iterable}
dict_numbers = {x:x*x for x in range(1,6) }
print(dict_numbers)

#9) Join Dictionaries (an adition to: update and merge methods)
#syntax: ** operator in front of the dictionary
data_1 = {'Name': 'Mark', 'Score': 10}
data_2 = {'Function': 'Data Scientist', 'Active': True}
merged_data = {**data_1, **data_2}
print(merged_data)

#10) Remove duplicates in a list
#Transform in set() and then in a list()
numbers = [1,1,1,2,2,3,4,5,6,7,7,8,9,9,9]
new_numbers = list(set(numbers))
print(new_numbers)

#11) Multiple variables assignment
a, b, c = 1, "Name", True
print(a, b, c)

#12) Filtering values in list (+ lambda fuction)
#syntax: filter(function, iterable)
my_list = [10, 11, 12, 13, 14, 15]
filtered_list = list(filter(lambda x: x%2 != 0, my_list ))
print(filtered_list)

#13) Sort dictionary by keys
product_prices = {'tennis': 22.99, 't-shirt': 19.99, 'hat': 9.99}
product_sorted = {key:product_prices[key] for key in sorted(product_prices.keys())}
print(product_sorted)

#14) Sort dictionary by values
#syntax: sorted(iterable, key=, reverse= False [True(max. to min.)])
car = {'car_1':205.75, 'car_2': 180.7, 'car_3': 100}
car_by_values = sorted(car.items(), key=lambda x:x[1], reverse= True)
print(car_by_values)

