# String handling

# userName = "rajan"

# print(userName)

# a ='suresh'

# b= 'ramesh'

# print("before-->",b)
# b=a
# a= "kumar"
# b= "santo" 
# print("after-->",b)

# a= "go"

# b= "come"

# b = a

# a = b

# print("final",a)

# a="ramesh"
# b="suresh"

# c= a

# a= b

# a = c

# print("final",c)
# print("final",b)



# indexing - getting the character in the given string based on the index number

# positiv indexing - indexing with positive numbers

# name = "suresh"

# print(name[5])
# name[1]
# name[3]

# # negative indexing - indexing with negative numbers

# print(name[-6])
# name[-6]


# # slicing

# print(name[2:100])

# negative slicing

# print(name[-3:-200])

# name = "suresh"

# #  ranging

# print(name[:6])

# print(name[-5:])

# string formatting

# name = "suresh"

# age = 23

# email = "dilli@gamail.com"

# # normal formatting

# # automatic formatting

# # manual formatting


# # concatenation - adding two strings with + operator
# # manual
# formatted = "my name is"+ " " + name + " and my age is "+ " " "23" + " " +" my email id is"+ " " + email
# print(formatted)

# # automatic formatting

# formatter = "my name is {} and my age is {} and email id is {}".format(name,age,email)
# print(formatter)

# # format -  is the function

# # manual formatting

# formatter = "my name is {1} and my age is {0} and email id is {2}".format(age,name,email)
# print(formatter)

# formatting = " my name is %s and age is %s and email id is %s" %(name,age,email)
# print(formatting)

# formatting = f"my name is {name} and age is {age} and email id is {email}"
# print(formatting)




# String built in functions ------------------


# name = "softlogic"
# name = name[1:]
# capword = "S"

# #name =capword+name
# #name = "%s%s"  %(capword,name)
# #name = "{1}{2}".format(capword,name)
# name = f"{capword}{name}"
# name = "{}{}".format(capword,name) 
# print(name)


# name = "softlogic"



# name=name[1:]

# d ="S"

# name= "{}{}".format(d,name)

# print(name)

# print(name)


# capitalize function----------


# name ="softlogic"

# name=name.capitalize()
# print(name)


# #  titlte ---------

# name = " my instite name is "

# name = name.title()

# print(name)

# # upper-------
# name = " my instite name is "

# name = name.upper()

# print(name)


# # lower---------
# name = " my instite name is "

# name = name.lower()

# print(name)

# swapcase--------

# name = " My Institute Is Logical"

# name = name.swapcase()

# print(name)


# # find------
# # index-----
# name = " My Instiytute Is Logical"

# #yindexnumber = name.find("x")
# yindexnumber =name.index("x")

# print(yindexnumber)



# name = "My Institute Is Logical"

# yindexnumber = name.find("x")

# # print(yindexnumber != -1)

# print(yindexnumber >=0)


# print(yindexnumber)

# print(name)


 
 #count-----------

# name = " My Institutye Is  y Logical"

# counter = name.count(" ")

# print(counter)


# # ends with--------

# name = " My Institute Is Logical"

# hence = name.endswith("al")

# print(hence)

# # starts with------
# name = " My Institute Is Logical"

# hence = name.startswith(" M")

# print(hence)


# name = " My Institute Is Logical"

# hence = name.replace("M","a")

# print(hence)

# Strip----------

# name = " My Institute Is Logical"

# hence = name.rstrip()

# print(hence)


# name = " My Institute Is Logical"

# hence = name.lstrip()

# print(hence)


#name = " My Institute Is Logical"

#hence = name.replace(" ","")


#print(hence)


# name = "adfffvvv"

# jig = name.isalpha()

# print(jig)

# name = "565656"

# jig = name.isnumeric()

# print(jig)


# name = "DS59SDDDD"

# jig = name.isalnum()

# print(jig)


# name = "softlogic"

# #('soft' ,'l' , 'logic')
# gen = name.partition("")
# print(gen)


# name ="my institue is softlogic"
# gen = name.split("")
# print(gen)


# remove the hifen slice from second lettr upto tenth letter
# and then add underscore on middle... ans show output and show the lenght also

name = "my-institute-is-softlogic"
gen = name.replace("-","")

genral = gen[1:11]

g= genral[0:5]+"-"+genral[5:10]

h=len(g)

print(h)

name = name.replace("-","")[1:11]

firsthalf = name[: len(name)//2]
secondhalf =name[ len(name)//2:]

name =f"{firsthalf}_{secondhalf}"

print(name,len(name))
