### String Creation ###

# single_quote = 'Hello'
# double_quote = "World"
# triple_quote = """
# multi-line
# string
# value
# """

# print(single_quote)
# print(double_quote)
# print(triple_quote)

#####################################################################################################################
### String indexing and slicing ###

# text = "Python Programing"

# print(text[0]) # (first character)
# print(text[-1]) # (last character)
# print(text[0:6]) # (slice 0 to 5)
# print(text[:2]) # (from start to 2)
# print(text[7:]) # (7 to end)

#####################################################################################################################
### String Methods ###

# name = " bob the builder "

# print(len(name)) # length
# print(name.strip()) # remove whitespace
# print(name.upper()) # uppercase
# print(name.lower()) # lowercase
# print(name.title()) # title case, every first of word capital letter
#                     # output : Bob The Builder
# print(name.replace("bob", "jane")) # replace
# print(name.strip().replace("bob","peter").upper()) 

#####################################################################################################################
### String Formatting ###

name = "John Doe"
age = 30

message_1 = f"My name is {name} and I am {age} years old." # f-string
message_2 = "My name is {} and I am {} years old.".format(name, age) # str.format()
message_3 = "My name is %s and I am %d years old"%(name, age) # %-formatting


print(message_1)
print(message_2)
print(message_3)


text= """Python is a powerful language.It's easy to learn and versatile!"""


