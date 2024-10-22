# -*- coding: utf-8 -*-
"""lists_and_tuples

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tyq4HXgfT5CFmJJc9_FPKm6iliVvoqVa
"""

# create a program to calculate the average of values in a list
#create list
scores = [2.5, 7.3, 6.5, 4.0, 5.2]
#use a for loop to calculate the total
total = 0
for score in scores:
    total += score
#calculate the average
average = total / len(scores)
#print the average
print("The average score is:", average)

# create a program that reads a file's cities.txt contents into a list

#function takes filename as argument
def read_cities_to_list(filename):
    #open the file
    with open(filename, 'r') as file:
        #list comprehension to reach each line from the file, strip whitespace,
        #and create a list of cities
        cities = [city.strip() for city in file.readlines()]
    #return list of citites
    return cities

# Read the cities from the file
cities_list = read_cities_to_list('cities.txt')

# Print the list of cities
print(cities_list)