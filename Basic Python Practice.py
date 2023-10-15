#!/usr/bin/env python
# coding: utf-8

# ## String

# In[1]:


# 1.

name = input("  ")
print("Hello {} !".format(name))


# In[2]:


# 2.

# From low string print count of "Is".

string = "He is Amol and she is chaital"
print(string.count("is"))


# In[3]:


# 3.

# From low string split the word by space.

a = "Data is new oil"
splitted_list = a.split(" ")
print(splitted_list)


# In[4]:


# 4.

# now from below, join all the words by "=" and create a sentence.

i = ["Data", "is", "new", "oil"]
new_string = "=".join(i)
print(new_string)


# In[5]:


# 5.

# from below string replace "Java" with "Python"

sentence = "I love Programming in Java."
print(sentence.replace("Java","Python"))


# In[6]:


# 6.

# from below string remove(strip) additional spaces and print it.

msg = " This a message with spaces."
strip_msg = msg.strip()
print(strip_msg)


# In[7]:


#7. 

# From below string find postion(start index) of "sample"

sentence = "This is a sample sentence."
print(sentence.index("sample"))


# In[8]:


#8. 

#Given the string "Python is fun!", how can you calculate and print its length?

text = "Python is fun!"
print(len(text))


# In[9]:


#9.

#Print below string in reverse order

string = "Pineapple"[ : :-1]
print(string)


# In[10]:


#10. 

#Given the string "Welcome to Python Programming.", how can you capitalize the first letter of each word and print the modified string?

text = "Welcome to Python Programming."
print(text.upper())


# In[11]:


#11. 

#Convert all letter of string to Upper Case

text = "Data is new oil"
print(text.upper())


# In[12]:


#12. 

#From below string just convert first lettter of string to upper case

text = "i am learning python"
print(text.title())


# In[13]:


#13. 

#Convert all uppper case to lower and lower case to upper

text = "DaTA is NeW oIL"
print(text.swapcase())


# In[14]:


#14. 

#rint the addition of below 2 strings

a = 10
b = 60
print(a+b)


# In[15]:


#15. 

#print the additiono of below 2 strings

a = "20"
b = "30"
print(a+b)


# ## List

# In[16]:


#16.

#From belown list replace 4 with 44.

my_list=[1,2,3,4,5]
my_list[3]= 44
print(my_list)


# In[17]:


#17.

#From belown list add(insert) 200 at index 3

my_list = [1, 2, 3, 4, 5]
my_list[3]=200
print(my_list)


# In[18]:


#18.

#In below list add new number 66.

my_list = [1, 2, 3, 4, 5]
my_list.append(66)
print(my_list)


# In[19]:


#19.

#In below list insert new numbers 66,87,99.

my_list = [1, 2, 3, 4, 5]
my_list.extend([66,87,99])
print(my_list)


# In[20]:


# 20. 

#rom below list remove number 3.

my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)


# In[21]:


# 21. 

#From below list print count of "cherry"
my_list = [1, 2.5, "cherry", 3, "banana", 4.0, "cherry"]
my_list.count("cherry")
2


# In[22]:


# 22. 

#From below list print index of "banana"
my_list = [1, 2.5, "apple", 3, "banana", 4.0, "cherry"]
my_list.index("banana")


# In[23]:


# 23. 

#From below list remove last item
my_list = ["Pune","Delhi","Mumbai","Indore","Jaipur","Dehradun"]
my_list.remove("Dehradun")
print(my_list)


# In[24]:


# 24.
# Sort the below list in Alphabetical order
my_list = ["Grapes","Apple","Cherry","Mango","Banana"]
my_list.sort()
print(my_list)


# In[25]:


# 25 .
# Sort below list in reverse Alphabetical order
my_list = ["Grapes","Apple","Cherry","Mango","Banana"]
my_list.sort(reverse=True)
print(my_list)


# ## Assignment
# ## Problem 1
# ### Create a list named myList that has three elements:
# 
# ~The integer 3
# 
# ~The string 'element number 2'
# 
# ~Another list ['last','element']
# 
# in that order

# In[27]:


mylist = [3,'elemet',['last','element']]


# ### Problem 2
# ~Print the third element of the follwing list.

# In[30]:


l = [1,2,3,4,5,6,7,8]
print(l[2])


# ## Problem 3.
# Modify the last element of this list so that its value is 16. Print the modified list so you know the opration was performed succefully.

# In[31]:


listToModify = ['a', 'b', 'sixteen']
listToModify[2] = 16
print(listToModify)


# ## Problem 4.
# Calculate the length of the following list.

# In[32]:


listToFindLength = ['this ','is','the','list','whose','length','I','want']
len(listToFindLength)


# ## Problem 5.
# Calculate the sum of the following list.

# In[33]:


inList = [54,678,2890]
sum(inList)


# ## Problem 6.
# Find the maximum value of the following list.

# In[34]:


maxList = [455,677,223,1467,24,34577,34]
max(maxList)


# ## Problem 7.
# Find the minimum value of the following list.

# In[35]:


minList = [455,677,223,1467,24,34577,34]
min(minList)


# ## Problem 8.
# Append the string 'Append me!' to the end of the following list. Print the list to ensure the operation has been completed succefully.

# In[36]:


listToAppend = [1,2,3]
listToAppend.append('Append me!')
print(listToAppend)


# # Python for Loop ques

# In[38]:


#Example 1: Print the first 10 natural numbers using for loop.

for i in range(1,11):
    print(i)


# In[39]:


#Example 2: Python program to print all the even numbers within the given range.

given_range = 10
for i in range(10):
    if i%2==0:
        print(i)


# In[40]:


#Example 3: Python program to calculate the sum of all numbers from 1 to a given number.

give_number = 10
sum = 0
for i in range(1,10+1):
    sum+=i
    print(sum)
    


# In[41]:


#Example 4: Python program to calculate the sum of all the odd numbers within the given range.

given_range = 10
sum = 0
for i in range(given_range):
    if i%2!=0:
        sum+=i
        print(sum)


# In[42]:


# Example 5: Python program to print a multiplication table of a given number.

given_number = 5

for i in range(11):
    print(given_number,"x",i,"=",5*i)


# In[43]:


# Example 6: Python program to display numbers from a list using a for loop.

list = [1,2,4,6,88,125]
for i in list:
    print(i)


# In[44]:


#Example 7: Python program to count the total number of digits in a number.

num = 129475
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))


# In[45]:


#Example 8: Python program to check if the given string is a palindrome.

given_string = "madam"

reverse_string =""
if(given_string == reverse_string):
    print("The string", given_string,"is a Palindrome.")
else:  
    print("The string",given_string,"is NOT a Palindrome.")


# In[48]:


#Example 9: Python program that accepts a word from the user and reverses it.

given_string = input()
reverse_string = ""
for i in given_string:
    reverse_string= i+reverse_string
print(reverse_string)


# In[49]:


#Example 10: Python program to check if a given number is an Armstrong number.

given_number=153
given_number=str(given_number)
string_length=len(given_number)
sum=0
for i in given_number:
    sum+=int(i)**string_length
if sum == int(given_number):
    print("The given number",given_number,"is an Amstrong number.")
else:
    print("The given number",given_number,"is Not an Amstrong number.")    
    


# In[50]:


#Example 11: Python program to count the number of even and odd numbers from a series of numbers.

num_list = [1,3,5,6,99,134,55]

for i in num_list:
    
    # if divided by 2, all even
    # number leave a remainder of 0
    if i%2==0:
        print(i,"is an even number.")
    else:
        print(i,"is an odd number.")


# In[51]:


#Example 12: Python program to display all numbers within a range except the prime numbers.

def is_not_prime(n):
    flag = False
    for i in range(2, int((n**0.5)) + 1):
        if n % i == 0:
            flag = True
    return flag

range_starts = int(input("enter the start range:"))

range_ends = int(input("enter the end range: "))
print("Non-prime numbers between",range_starts,"and", range_ends,"are:")
 
for number in filter(is_not_prime, range(range_starts, range_ends)):
    print(number)       


# In[52]:


#Example 13: Python program to get the Fibonacci series between 0 to 50.


num = 50
first_value, second_value = 0, 1
for n in range(0, num):
    if n <= 1:
        next_value = n
    else:
        next_value = first_value + second_value
        first_value = second_value
        second_value = next_value
    if next_value > num:
        break
    print(next_value)
 


# In[53]:


#Example 14: Python program to find the factorial of a given number.

given_number= 5
 
factorial = 1
 
for i in range(1, given_number + 1):
    factorial = factorial * i
 
print("The factorial of ", given_number, " is ", factorial)


# In[55]:


#Example 15: Python program that accepts a string and calculates the number of digits and letters.

user_input = input("Enter the string: ")
digits = 0
letters =0
for i in user_input:
    if i.isdigit():
        digits = digits+1
    elif i.isalpha():
        letters = letters+1
print(" The input string",user_input, "has", letters, "letters and", digits,"digits.")


# # Dictionary

# In[57]:


#1. Given the following dictionary, print all the keys.
my_dict1 = {"name":"abhi","add":"gaya","pin":824209,"state":"bihar"}
print(my_dict1.keys())


# In[60]:


#2. Print all values of dictionary 
my_dict2 = {"name":"abhi","add":"gaya","pin":824209,"state":"bihar"}
print(my_dict2.values())


# In[62]:


#3. Print all values except "gaya"
my_dict2 = {"name":"abhi","add":"gaya","pin":824209,"state":"bihar"}
my_dict2.pop("add")
print(my_dict2)


# In[64]:


#4.  Delete key "pin" from below dict
my_dict2 = {"name":"abhi","add":"gaya","pin":824209,"state":"bihar"}
del my_dict2["pin"]
print(my_dict2)


# In[67]:


#5. Print value of "state" from below dictionary.
my_dict2 = {"name":"abhi","add":"gaya","pin":824209,"state":"bihar"}
print(my_dict2["state"])


# # Function 

# In[3]:


# 1. Write a python function for addition of 2 number
def add_num(num1,num2):
    sum = num1 + num2
    return sum


# In[4]:


add_num(34,56)


# In[10]:


# 2. Write function to add all numbers of list and print

def sum(*numbers):
    total = 0
    for x in numbers:
        total += x
        return total
    


# In[11]:


total = sum(5,6,7,4,8)
print(total)


# In[18]:


# 3 . Write a fucntion to check if number is even or odd and print it.

def even_odd(num):
    if num%2 == 0:
        print("{} is even Number".format(num))
  
        


# In[24]:


print(even_odd(22))
print(even_odd(21))


# In[51]:


# 4. Take any no of inputs in functions and print them.
def sum(*args):
    total = 0
    for x in args:
        total += x
    return total


# In[52]:


total = sum(1,2,5,7,8,9)
print(total)


# In[58]:


# 5 . Write a python function which will take N number of inputs and print addition of all numbers
def add_number(*numbers):
  sum=0
  for num in numbers:
    sum = sum + num
  return sum

addition = add_number(3,5,7,86,8)
print(addition)


# In[67]:


# 6 .Write python function which will take N number of string as inputs and will return list of Upper case string
def upper_string(*words):
  upper_list=[]
  for word in words:
    upper_list.append(word.upper())
  return upper_list

upper_words= upper_string("Enter the lower_name")
print(upper_words)


# In[63]:


# 7.write a python function which takes multiple keyword arguments.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{},{}".format(key,value))

print_kwargs(name="Alice", age=30, city="New York")


# In[56]:


# 8 .write a python function which takes keyword agruments and find maximum value among all

def find_max(**kwargs):
    return max(kwargs.values())

result = find_max(a=10, b=5, c=15)
print(result)


# In[ ]:




