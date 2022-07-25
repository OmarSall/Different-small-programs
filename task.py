# from distutils import text_file
# from re import A
# import re

# #######################################
# def counter(word):
#     a = len(str(word))
#     return a 

# print(counter('Omarito'))
# ########################################
# elements = (
#     (1, 4),
#     (4, 5),
#     (6, 7),
#     (1, 3)
# )

# # for tup in elements:
# #     print(tup[1])

# result = [tup[1] for tup in elements]
# print(result)
################################################
# customer = (
#     ('id','98698761'), 
#     ('name', 'marry'), 
#     ('surname', 'smith'), 
#     ('rented_books', 3 )
#     )

# print(dict(customer))
#################################################
# passwords = ['ccavfb', 'baaded', 'bbaa', 'aaeed', 'vbb', 'aadeba', 'aba', 'dee', 'dade', 'abc', 'aae', 'dded', 'abb', 'aaf', 'ffaec']
# a=0

# print("Number of all items =",len(passwords))
# for item in passwords:
#     if 'ab' in item or 'ba' in item:
#         print(item)
#         a=a+1

# print("Number of selected items =",a)
#############################################################

# def check_the_list(lista, object):
#     if object not in lista:
#         lista.append(object)
#     else:
#         print("The element is already in the list!")

#     return lista

# elements = [1,2,3,4]
# check_the_list(elements, 2)
# print(elements)

#######################################################

# elements = [
#     [1, 4, 6, 7],
#     [4, 5, 6],
#     [6, 7, 8],
#     [],
#     ["nodata", "nodata"],
#     [1, 3]
#             ]
# for tup in elements:
#     if tup and isinstance(tup[0], int):
#         print(tup[0])
#####################################################      

# def foo(ist):
#     return ist[0]
    
# print(foo([5,4,3,2,1]))

############################################
#return the last item

# def last_item(lst):
#     return lst[-1]


# print(last_item([1,2,3,4]))
####################################
#return first and last item

# def foo(lst):
#     return lst[0], lst[-1]

# print(foo([1,2,3,4]))
######################################3
#return the max nr of the list

# def foo(mylist):
#     return max(mylist)

# print(foo([1,2,3,4,5,6,7,77]))
##################################

# def foo(*args):
#     return list(args)

# print(foo(1,'a',3,'b'))
######################################

# def foo(**kwargs):
#     return kwargs

# print(foo(a=1,c=5,d=109))
# ################################
# def foo(*args):
#     lst = []
#     for eachlist in args:
#         lst = lst + eachlist
#     return lst

# print(foo([1,2,3],[4,5,6]))
##############################

# def foo(*args):
#     if [] in args:
#         return False
#     else:
#         return True

# print(foo([1,2],[4,56,6]))
##################################
# def foo():
#     return "Hello"
    
# def funkcja():
#     return foo

# print(funkcja())
############################
# for i in (x/10 for x in range(0,101)):
#     print(i)

######################################

# def fun(number):
#     return dict(sign = "positive" if number > 0 else
#     "negative" if number < 0 else "zero",
#     parity = "odd" if number % 2 ==1 else
#     "even" if number % 2 == 0 else "non integer")

# print(fun(0))

#############################################

# def foo(lst):
#     if lst == []:
#         return "Empty list"
#     else:
#         return lst[-1]

# print(foo([]))
################################

# def foo(lst):
#     return lst[1:-1]

# print(foo([1,2,3,4]))
############################

# def foo(lst,object):
#     if len(lst) == 3:
#         lst.pop(0)
#         lst.append(object)
#         return lst
#     else:
#         None

# print(foo([1,2,3],6))
#############################

# def foo(lst):
#         return lst[::7]

# print(foo(['pon','wt','sr','czw','pt','sob','niedz','pon','wt','sr','czw','pt','sob','niedz','pon','wt','sr','czw','pt','sob','niedz']))
# ############################
# import itertools

# def foo(mylist):
#     list_of_lists = [mylist[i:i+5] for i in range(0, len(mylist),7)]
#     # print(list_of_lists)
#     return list(itertools.chain.from_iterable(list_of_lists))

# print(foo(['pon','wt','sr','czw','pt','sob','niedz','pon','wt','sr','czw','pt','sob','niedz','pon','wt','sr','czw','pt','sob','niedz']))
###################################
# x items every y items
# import itertools

# def foo(mylist, x, y):
#     list_of_lists = [mylist[i:i+x] for i in range(0, len(mylist),y)]
#     return list(itertools.chain.from_iterable(list_of_lists))

###############################################

# numbers = [1, 4, 6, 8, 9, 6, 7, 8, 9, 3, 44, 55, 6, 77, 88, 997, 7, 6, 7, 7, 8, 9, 8, 8, 8, 9, 8, 8, 0, 9, 0, 9, 8, 9, 8, 8, 8, 9, 9, 9, 9, 0, 1, 3, 5, 6, 7, 8, 7, 7, 7, 8, 7, 7, 5, 4, 5, 6, 5, 56, 4, 3, 4, 5, 6, 6, 7, 8, 8, 9]

# sum = 0
# for i in range(0, len(numbers),2):
#     sum = sum + numbers[i]
    
# mean = sum / (len(numbers)/2)
# print(mean)

#lepsze rozwiązanie
 
# every2 = numbers[::2]

# print(sum(every2)/len(every2))
####################################

# def middle_item(lst):
#     center = int(len(lst)/2)
#     return lst[center]

# print(middle_item([1,2,3,4,5]))
##################################

# def middle_item(lst):
#     if len(lst) % 2 == 0 or len(lst) == 0:
#         return 'Bad List'
#     else:
#         center = int(len(lst)/2)
#         return lst[center]

# print(middle_item([1,2,3,4,5,6]))
#######################################
#anti Duplicator
# def foo(lst):
#     return list(set(lst))

# print(foo([1,1,2,2,3,4,5,5,5]))   
######################################
# import random

# def foo():
#   return [random.randint(1,10) for i in range(1000)] 
# print(foo())
###############################

# def fun(word):
#     if 'xxx' in word:
#         return True
#     else:
#         return False
###############################3

# def fun(lst):
#     L2 = [lst[i] for i in range(len(lst)) if 'xxx' in str(lst[i])]
#     return L2

# print(fun(['xxnxx','agre','omarxxxxomar']))
#another solution

# def foo(mylist):
#     return [string for string in mylist if isinstance(string, str) and 'xxx' in string]
############################################
# def foo(dictionary):
#     return sum(dictionary.values())

# print(foo({'a':1,'b':3,'c':6}))
########################################
# def foo(mydict):
#     lst = []
#     for key, value in mydict.items():
#         lst = lst + value
#     return sum(lst)
########################################

# def foo(mydict):
#     return dict((key,value) for key, value in mydict.items() if value > 4 )
######################################
# def foo(mydict):
#     return dict((key,value) for key, value in mydict.items() if value > 4 and isinstance(value, int))
###################################
# vocabulary = {
#     "hello" : "Hi there!",
#     "what's your name" : "My name is Roboto!",
#     "what is your name" : "My name is Roboto!",
#     "bye" : "Goodbye!"
# }

# def talk(query, vocabulary):
#   if query in vocabulary:
#     return vocabulary[query]

############################################

# import datetime
# import difflib

# vocabulary = {
#     "hello" : "Hi there!",
#     "what's your name" : "My name is Roboto!",
#     "what is your name" : "My name is Roboto!",
#     "bye" : "Goodbye!",
#     "what time is it" : datetime.datetime.now().strftime("%H:%M")
# }

# def foo(query, vocabulary):
#     new_vocabulary = {key:[value, difflib.SequenceMatcher(None, query, key).ratio()]
#     for (key,value) in vocabulary.items()}
#     return new_vocabulary[max(new_vocabulary, key = lambda k: new_vocabulary[k][1])][0]
######################################
# import datetime 
# import calendar

# def findDay(date):
#     born = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
#     return (calendar.day_name[born])
#################################################
# ffor i in range(1,9+1):
#     open("day{}.txt".format(i), "w").close()
##################
# for i in range(1,9+1):
#    open("file{}.txt".format(i), "a").close()
################################
# import glob
# import re
# text_files = glob.glob("*.txt")
# lists = []

# for text_file in text_files:
#     with open(text_file) as file:
#         lists.append(file.readlines())

# all_lines = sum(lists, [])

# matches = [re.compile("[0-9]+\.*[0-9]*").search(line) for line in all_lines]

# numbers = [float(match.group(0)) for match in matches if match]

# print(sum(numbers)/len(numbers))
########################

# import glob
# import re
# text_files = glob.glob("*.txt")
# lists = []

# for text_file in text_files:
#     with open(text_file) as file:
#         lists.append(file.readlines())

# all_lines = sum(lists, [])

# matches = [re.compile("[0-9]+\.*[0-9]*").search(line) for line in all_lines]

# numbers = [float(match.group(0)) for match in matches if match]

# mean = sum(numbers)/len(numbers)

# with open('mean.txt', 'w') as f:
#     f.write(str(mean))

#################################################
#CREATE 50 EMPTY FOLDERS
# import os

# for i in range(1, 50+1):
#     os.makedirs(str(i))
#################################################
#50 folders and each folder has 5 subfolders named from mon to friday

# import os

# for folder in range(1, 50+1):
#     for subfolder in ["mon", "tue", "wed", "thu", "fri"]:
#         os.makedirs(str(folder) + "/" + str(subfolder))

##############################################
# delete a file
# import os
# os.remove("file2.txt")
########################
#delete all files in a folder

# import os
# import glob

# text_files = glob.glob("*.txt")

# for text_file in text_files:
#     os.remove("{}".format(text_file))
############################################
#Seek xxx and  in txt files and delete all the files containing those str
# import os
# import glob

# text_files = glob.glob("*.txt")


# for text_file in text_files:
#     with open(text_file) as file:
#         content = file.read().lower()

#         if 'xxx' in content:
#             os.remove(text_file)

############################################
#find the file with minimum size
# import os
# import glob

# text_files = glob.glob("*.txt")

# file_size = {text_file: os.path.getsize(text_file) for text_file in text_files}

# print(min(file_size, key = file_size.get))
############################################

# import json

# with open("file2.txt") as json_file1:
#     data = json.load(json_file1)
# print("DATA", data)

# data["metals"]["gold"] = {
#     "conductivity": 33.5,
#     "density": 0.255,
#     "heat": 0.129,
#     "melting point": 2171,
#     "thermal expansion": 4.7,
#     "yield strength": 288,
#     "tensile strength": 441,
#     "minimum impact energy": 22
#     }

# with open("file2.txt","w") as json_file2:
#     json.dump(data, json_file2)

#######################################
# import json

# with open("file2.txt") as json_file:
#     data = json.load(json_file)

# print({key:float(value)*2 for key, value in data.items()})
###########################################
# import json

# with open("file2.txt") as json_file:
#     data = json.load(json_file)
#     print(data['metals']['steel']['density'])

##########################################

# import json

# def foo(metal, property, filepath):
#     with open(filepath) as json_file:
#         data = json.load(json_file)
#         return data['metals']['steel'][property]

########################################
# import os
# import glob

# with open("file2.txt") as fp:
#     data = fp.read()

# with open("file3.txt") as fp:
#     data2 = fp.read()

# with open("file4.txt") as fp:
#     data3 = fp.read()

# data += "\n"
# data += data2
# data += data3

# with open ('together.txt', 'w') as fp:
#     fp.write(data)
#better solution

# import glob

# text_files = glob.glob("file*.txt")

# with open('together.txt', 'w') as outfile:
#     for text_file in text_files:
#         with open(text_file) as infile:
#             for line in infile:
#                 outfile.write(line + "\n")

# import glob

# all_txt_files = [open(file).readlines() for file in glob.glob("*.txt")]

# with open('output.txt', 'a+') as file_output:
#     for item in all_txt_files:
#         file_output.writelines(item)
#         file_output.write("\n")
    # pass

#####################################################
# import glob
# import os

# text_files = glob.glob("file*.txt")

# for text_file in text_files:
#     for number in range(1,10):
#         os.rename(text_file,f"file-{number}.txt")


# for i in range(1,10):
#    open("file{}.txt".format(i), 'w').close()
######################################

# x = 1
# y = '2'
# try:
#     print(x + y)
# except TypeError: # Better to be specific about the error you expect
#     print(int(x) + int(y))

################################3

# import re

# with open("file2.txt", "r") as file:
#     lines = file.readline()
#     lst = re.findall("[A-Z][a-z ',]*\?", lines)
    
# print(lst)
# #krótrze rozwiązanie

# import re

# with open("file2.txt", "r") as file:
#     lst = re.findall("[A-Z][a-z ',]*\?", file.readline())


# #inne rozwiązanie

# import re
# with open("file2.txt") as file:
#     content = file.read()
#     print(re.findall("[A-Z][a-z ',]*\?", content))


# firstname = "John"
# lastname = "Smith"

# print("Welcome {} {} to our shop!".format(firstname, lastname))

###################################################

# names = {"firstname" : "Andy", "lastname": "Smith"}
# print("Welcome {firstname} {lastname} to our shop!".format(**names))
################################################

# firstname = "Andy"
# lastname = "Smith"
# print("Welcome {:.1}.{:.1} to our shop!".format(firstname, lastname))
########################################

# def foo(mystring): 
#     my_str = mystring.replace(' ', '')
#     my_str1 = my_str.replace('.', '')
#     return len(my_str1)


# mystring = "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient python, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus."
# print(foo(mystring))

########################################
#Ratio of similarity between two strings
# import difflib

# def foo(string1, string2):
#     return (difflib.SequenceMatcher(None, str(string1), str(string2)).ratio())
    
# print(foo("tell me the time", "what time is it"))
###################################

# class Computer:
 
#     def __init__(self, model, memory, processor):
#         self.memory = memory
#         self.processor = processor
 
#     def price(self):
#         return (self.memory * self.processor) / 10
 
# macbook = Computer('Macbook Pro 15" 2016', 16, 2400)
# print(macbook.price())

################################
# import re

# class Robot:

#     def __init__(self):
#         pass

#     def speak(self, query):
#         if query == 'hi robot':
#             return 'hi human'
#         else:
#             return "I don't know"
#########################################################
# import re

# class Robot:

#     def __init__(self):
#         pass

#     def speak(self, query):
#         self.query = query
#         if 'sum' in query:
#             self.digits = re.findall("\d+",query)
#             self.conversion = [int(x) for x in self.digits]
#             self.mysum = sum(self.conversion)
#             return self.mysum

# robot = Robot()
# print(robot.speak("what is the sum of 25 and 2"))
##################################################
# import re

# a = "what is the sum of 1 and 3"

# digits = re.findall("\d",a)
# conversion = [int(x) for x in digits]
# # total = 0
# # total = [total + conversion[item] for item in range(0,len(conversion))]
# mysum = sum(conversion)
# # for items in range(0,len(conversion)):
# #     total = total + conversion[items]
##########################################

# import re

# class Mind:

#     def __init__(self):
#         pass
    
#     def think(self, query):
#         if 'sum' in query: # Check if string 'sum' is in query
#             numbers = re.findall(r'\d+', query) # Extract the numbers. E.g. ['1', '2']
#             numbers = [float(item) for item in numbers] # Convert the numbers into floats [1.0, 2.0]
#             return str(sum(numbers)) # Return the sum of the numbers
            
# class Robot():

#     def __init__(self):
#         self.mind = Mind() # When Robot is initialized with Robot(), that will also initialize Mind
       
#     def print_out(self, query):
#         print(self.mind.think(query)) # Prints out the output returned by mind.think(query) 

#     def write_down(self, query):
#         with open('a.txt', 'w') as file:
#             file.write(self.mind.think(query))

# robot = Robot()
# robot.print_out("what is the sum of 3 and 5?")
# robot.write_down("what is the sum of 3 and 5?")

#############################################################
#Print out the list of all attributues of an object int
# attributes = dir(int)
# print(attributes)

############################################################
# import re

# def foo(obj):
#     all_attributes = dir(obj)
#     normal_attributes = [attribute for attribute in all_attributes \
#             if not re.compile("__[a-z0-9A-Z_]*__").search(attribute)]
#     return normal_attributes

############################################
#return of an id number of an object

# def foo(obj):
#     return id(obj)

# print(foo(int))
##########################################
