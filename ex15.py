#imports argv module
from sys import argv
#sets up a variable for argv
script, filename = argv
#sets up txt as a variable eqauling filename from argv input
txt = open(filename)
#prints the file name and the text from file
print(f"Here's your file {filename}:")
print(txt.read())

#prints a prompt to ask for the filename in an input 
print("Type the filename again:")
file_again = input("> ")
print(open(file_again).read())



