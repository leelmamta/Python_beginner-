s= "hello mamta"
print(s)
# we can access particular location as s[0]=h , s[1] = e, it does not consider blank spaces 
print(s[6])# accessing particular location 
print(len(s)) # len() is a function in string , calculates length of string including spaces 
print(s[2:7]) # slices strig from 2 loaction to 6 th location includes spaces 
# if position is -ve in slicing then -1= a , a is at -1 t is at -2 and so on 
print(s.upper()) # convert string to upper case letters 
print(s.lower()) # lower() converts strign to lowercase letters 
print(s.replace("m","s")) # it will replace all m word from the string with s .
s1 = "!"
print(s+s1) #  + is used to concate two strings
 #Converts the first character to upper case
print(s.capitalize())
# Converts string into lower case
print(s.casefold())
# 	Returns a centered string
print(s.center(40))
#  there are many operational functios
