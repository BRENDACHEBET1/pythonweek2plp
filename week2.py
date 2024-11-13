#Create a list
my_list=[]
#Appending 10,20,30,40 t0 the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Inserting value 15 at the second position in the list
my_list.insert(1,15)

#Extending my_list with another list
my_list2=[50,60,70]

my_list.extend(my_list2)
print(my_list)

#Removing the last element
my_list.remove(70)
print(my_list)

#Sorting the list in an ascending order
my_list.sort()

# Step 7: Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("The index of 30 is:", index_of_30)

#Print the final list to verify the result
print("Final list:", my_list)