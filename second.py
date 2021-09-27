# # WELCOME TO PYTHON # #
# Programming Python. WEEK 02
# 011 --> 018
# TASK 001 - Creating three variables & concatenate..
Name = str 
Age = str
Country = str

Name = "Younes"
Age = "23"
Country = "Algeria"

print('"Hello',"'"+ Name,"\b', How You Doing \\ "'""" Your Age Is "'+Age,'\b"" + And Your Country Is:',Country)
#--------------------------------------------------
# TASK 002 - print line by line
print('"Hello',"'"+ Name,"\b', How You Doing \\ \n"'""" Your Age Is "'+Age,'\b"" +\n And Your Country Is:',Country)
#--------------------------------------------------
# TASK 003 - Indexing + Slicing
name = 'Elzero'
print(name[1]) #second letter is "l"
print(name[2]) #third letter is "z"
print(name[5]) #last letter is "o"
#--------------------------------------------------
# TASK 004 - Slicing
print(name[1:4]) # "lze"
print(name[0:5:2]) # "Ezr"
print(name[4::-2]) # "rzE"
#--------------------------------------------------
# TASK 005 - remove #@#@ to clear the text
NAME = "#@#@Elzero#@#@"
# Method 01
print(NAME[4:10])
# Method 02
print(NAME.strip("#@"))
#--------------------------------------------------
# TASK 006 - num = "9" --> output "0009"
num = "9"
print(num.zfill(4))
num = "15"
print(num.zfill(4))
num = "130"
print(num.zfill(4))
num = "1500"
print(num.zfill(4))
#--------------------------------------------------
# TASK 007 - putting chars before string
# Method 01:
name_one = "Younes"
name_two = "Younes_Elzero"
print(name_one.center(34,"@").rstrip("@"))
print(name_two.center(28,"@").rstrip("@"))
# Method 02:
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))
#--------------------------------------------------
# TASK 008 - capitalize letters Aa
name_1 = "YOunes" # OUTPUT >>  yoUNES
name_2 = "yoUNES" # OUTPUT >>  YOunes
print(name_1.swapcase())
print(name_2.swapcase())
#--------------------------------------------------
# TASK 009 - count words in string
msg = "I Love Python and Although Love Elzero Web School"
print(msg.count("Love"))
#--------------------------------------------------
# TASK 010 - index of a char
nom = "Elzero"
print(nom.index("z"))
#--------------------------------------------------
# TASK 011 - replace words 
Msg = "I <3 Python and Although <3 Elzero Web School"
print(Msg.replace("<3","Love"))
#--------------------------------------------------
# TASK 012 - replace words (just one time)
MSG = "I <3 Python and Although <3 Elzero Web School"
print(MSG.replace("<3", "Love", 1))
#--------------------------------------------------
# TASK 013 - print name, age(int), country by Format ""f
# Method 01: Old way.
namee = "Younes"
agge = 23
countryy = "Algeria"
print("My name is %s, And my Age is %d, And my Country is %s" %(namee, agge, countryy))
# Method 01: New way.
print("My name is {:s}, And my Age is {:d}, And my Country is {:s}".format(namee, agge, countryy))
# Method 03: New way. Like in Java script
print(f"My name is {namee}, And my Age is {agge}, And my Country is {countryy}")