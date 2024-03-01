#This section is regarding the message that needs to be encrypted
while True:
	#Requesting what message the user would like encrypted
	user_message = input("What is the message you would like to encrypt using the Caesar Cipher method? ")
	#Used to verify that there are not any digits/integers in the user's message
	if not any(char.isdigit() for char in user_message):
		break
	#Shows this message if there is an digit/integer in the user's message	
	else: 
		print("The string cannot contain integers, please try again.")

#If the user's message contains only strings, this message will appear
print("Thank you for entering a valid message. Let's continue. ")

#This section is regarding the Key
while True:
	#This requests the User to select a Key that is between 1 and 26
	key = input("Enter a Key between 1 and 26: ") 
	#An If Else statement that requires the Integer given to be between 1 and 26
	if key.isdigit():
		key = int(key)
		if 1<= key <=26:
			#If the Integer is between 1 and 26, this prints and the If Else statement ends
			print("Thank you, let's continue.")
			break
		else:
			#If the Integer is not between 1 and 26, the If Else statement loops
			print("It looks like the Key is not between 1 and 26, please try again.")
	#If an invalid Integer is given, such as a string, this is printed
	else:
		print("This is not a valid integer.")

