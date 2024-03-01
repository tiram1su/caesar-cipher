def shift_text(text, key):
    return ''.join(shift_letter(char, key) for char in text)

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

def shift_letter(char, key):
	#Makes sure that any single character in the string is from the alphabet
    if char.isalpha():
        base = ord('a') if char.islower() else ord('A')
        #Determines how far to shift each letter based on the Key var
        shifted_char = chr(((ord(char) - base + key) % 26) + base)
        return shifted_char
    else:
    	#Returns the variable if it is not from the alphabet and does not do anything with it or change it
        return char

#Shifts the user_message var by the number of spots right that the User entered in the Key var
shifted_text = shift_text(user_message, key)
#Prints the output
print("Shifted text:", shifted_text)

# Stops program from closing automatically and allows User to initiate by pressing Enter
input("Press Enter to exit...")
