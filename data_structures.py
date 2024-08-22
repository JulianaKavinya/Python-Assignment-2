my_list =[]
print(my_list)

#my_list.append only takes exctaly one argument
# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Update an element in the list
my_list[1]=15
print(my_list)

# Extend the list with another list
list_2 = [50, 60, 70]
my_list.extend(list_2)
print(my_list)

 #Delete the last element in the list
del my_list[-1]
print(my_list)

# Sort the list in ascending order
my_list.sort()
print("Sorted list:", my_list)

# Find and print the index of the value 30
index_of_30 = my_list.index(30)
print(f"The index of 30 is: {index_of_30}")