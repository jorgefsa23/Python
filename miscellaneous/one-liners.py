# ONE-LINERS

'''List of one-line codes

Strategy to shorter and readable Python code
Source: https://towardsdatascience.com/9-one-liners-anyone-learning-python-should-know-29fdea7c540c
'''

# 1) IF-ELSE: 
age = 18
valid = "You're an adult"
invalid = "You're NOT an adult"
print(valid) if age >= 18 else print(invalid)

#2) List comprehension (here creating a new list from another)
#syntax: [expression for item in list]
words = ['united states', 'brazil', 'united kingdom']
capitalized = [word.title() for word in words]
print(capitalized)

#3) Dictionary Comprehension
#syntax: {key: value for key, value in iterable}
dict_numbers = {x:x*x for x in range(1,6) }
print(dict_numbers)

#4) Join Dictionaries (an adition to: update and merge methods)
#syntax: ** operator in front of the dictionary
dict_1 = {'a': 1, 'b': 2}
dict_2 = {'c': 3, 'd': 4}
merged_dict = {**dict_1, **dict_2}
print(merged_dict)

#5) Remove duplicates in a list
#Transform in set() and then in a list()
numbers = [1,1,1,2,2,3,4,5,6,7,7,8,9,9,9]
new_numbers = list(set(numbers))
print(new_numbers)

#6) Multiple variables assignment
a, b, c = 1, "Name", True
print(a, b, c)

#7) Filtering values in list + lambda fuction
#syntax: filter(function, iterable)
my_list = [10, 11, 12, 13, 14, 15]
filtered_list = list(filter(lambda x: x%2 == 0, my_list ))
print(filtered_list)

#8) Sort dictionary by keys
product_prices = {'Z': 9.99, 'Y': 9.99, 'X': 9.99}
product_sorted = {key:product_prices[key] for key in sorted(product_prices.keys())}
print(product_sorted)

#9) Sort dictionary by values
#syntax: sorted(iterable, key=, reverse= False [True(max. to min.)])
population = {'USA':329.5, 'Brazil': 212.6, 'UK': 67.2}
population_by_values = sorted(population.items(), key=lambda x:x[1], reverse= True)
print(population_by_values)

