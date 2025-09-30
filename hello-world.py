#This program will write Hello World!


#This function tells the computer to print Hello World!
# "def" is used to define a function
# Functions perform tasks
def PrintHelloWorld():
	print("Hello World!")


#This defines out main()function for our program
# The "main" program calls other functions in the program
# Functions perform tasks
def main():
	PrintHelloWorld()


#When we run the program, this executes first
# Python has a failsafe to allow complicated programs
# This statement executes first
if __name__=="__main__":
	main()