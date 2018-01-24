#
# <Andy Pham>
# <101006098>
#
#<Gaddis, T.(2015). "Starting Out With Python">
#<Smith, J. (Personal Communication, 2016-12-03)>
#

from random import *

file = open("your-assigned-glyphs.dat", "r")
string = file.read()
file.close()


dict = {} 
list = "" #Storing values for the keys in the dictionary


#myAdd Function
def myAdd(dict_add, key, value):
	if len(dict_add[key]) >= 2:
		for check in range(len(dict_add[key])):
			if value == dict_add[key][check]:
				print("\nNo changes have been made since that value already exists.")
				return len(dict_add[key])
				break
				
		dict_add[key].append(value)
		print("\nValue '", value, "' has been added to key '", key, "'.", sep="")
		print("UPDATED KEY = dict['", key, "'] = ", dict_add[key], "\n", sep="")
		return len(dict_add[key])
				
	else:
		if dict_add[key][0] != value:
			dict_add[key].append(value)
			print("\nValue '", value, "' has been added to key '", key, "'.", sep="")	
			print("UPDATED KEY = dict['", key, "'] = ", dict_add[key], "\n", sep="")
			return len(dict_add[key])
		else:
			print("\nNo changes have been made since that value already exists.")
			return len(dict_add[key])
		
		
#myUpdate Function
def myUpdate(dict_update, key, old, new):
	if old != new:
		if len(dict_update[key]) >= 2:
			for check in range(len(dict_update[key])):
				if old == dict_update[key][check]:
					dict_update[key][check] = new			
					print("\nValue '", old, "' has been updated to '", new, "'.", sep="")
					print("UPDATED KEY = dict['", key, "'] = ", dict_update[key], "\n\n", sep="")
					print("DICTIONARY =", dict, "\n")

		else:
			dict_update[key][0] = new
			print("\nValue '", old, "' has been updated to '", new, "'.", sep="")
			print("UPDATED KEY = dict['", key, "'] = ", dict_update[key], "\n\n", sep="")
			print("DICTIONARY =", dict, "\n")
	else:
		print("\nBoth values are the same so no changes have been made.\n\n")
		print("DICTIONARY =", dict, "\n")
		
		
#Translation Function
def myTranslate(trans_string):
	marker = 0
	for key in dict:
		marker = trans_string.find(key)
		while marker != -1:
			num = randint(0,len(dict[trans_string[marker]])-1) #Randomizes the range for values to pick from in key of dictionary 
			trans_string = trans_string[:marker] + dict[trans_string[marker]][num] + trans_string[marker + 1:]
			marker = trans_string.find(key)
	print("\nThe translated string is ", trans_string, ".\n\n", sep="")
	
	
#Dictionary
string = string.strip(":&")

for loop in range(len(string)):
	if string[loop] == "#":
		list = list + string[loop]
	elif string[loop] == "~":
		list = list.split("#")
		if list[0] in dict:
			dict[list[0]].append(list[1])
			list= ""
		else:
			dict[list[0]] = list[1]	
			dict[list[0]] = [list[1]]
			list = ""
	else:
		list = list + string[loop]


#Menu
print("DICTIONARY =", dict, "\n")
print("Would you like to (quit), (translate) a random string, (update), or (add) to the dictionary?")
user = input("Type in the whole word please: ")


main = 0
while main == 0:
	
	#Translation Option
	if user == 'translate':
		print("\n\n\n***TRANSLATION***")
		string2 = input("Enter in a string please: ")
		
		myTranslate(string2)
		
		
		print("DICTIONARY =", dict, "\n")
		print("Would you like to (quit), (translate) a random string, (update), or (add) to the dictionary?")
		user = input("Type in the whole word please: ")
		
		
	#Addition to Dictionary Option
	elif user == 'add':
		entries = 0
		print("\n\n\n***ADDING TO DICTIONARY***")
		key_add = input("Enter what key you want to insert your new value in: ")
		
		while key_add not in dict:
			key_add = input("Key does not exist in dictionary. Try again: ")
		
		value_add = input("Enter in the value: ")
		entries = myAdd(dict,key_add,value_add)
		
		if entries == 0 or entries >= 2:
			print("There are ", entries, " entries in the list at dict['", key_add, "'].\n\n", sep="")
		else:
			print("There is only ", entries, " entry in the list at dict['", key_add, "'].\n\n", sep="")
			
			
		print("DICTIONARY =", dict, "\n")
		print("Would you like to (quit), (translate) a random string, (update), or (add) to the dictionary?")
		user = input("Type in the whole word please: ")
		
		
	#Updating the Dictionary Option
	elif user == 'update':
		print("\n\n\n***UPDATING THE DICTIONARY***")
		key_update = input("Enter what key you want to update: ")
		
		while key_update not in dict:
			key_update = input("Key does not exist in dictionary. Try again: ")
		
		old_update = input("Enter in the value from that key you want to replace: ")
		
		while old_update not in dict[key_update]:
			old_update = input("Value does not exist in key. Try again: ")
		
		new_update = input("Enter in the new value: ")	
		myUpdate(dict, key_update, old_update, new_update)
		

		print("Would you like to (quit), (translate) a random string, (update), or (add) to the dictionary?")
		user = input("Type in the whole word please: ")

		
	#Quit Option	
	elif user == 'quit':
		print("\nGoodbye. Exiting program.")
		main = 1

		
	#Incorrect Input Sequence	
	else:
		user = input("Incorrect input. Try again: ")

	

		
		
	