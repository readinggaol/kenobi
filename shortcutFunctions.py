import os

"""Generates in-house list for selected file"""
def listGen(target):
	with open(target) as file_object:
		newList = []
		for line in file_object:
			newList.append(line)
	return newList

"""Collects all files from current directory"""
def collectFiles():
	var = os.listdir('.')
	filelist = []
	for thing in var:
		if thing.endswith("#"):
			filelist.append(thing)
	return filelist
		
"""Prints current list of programs"""
def printNames(masterlist):
	print("\n--CURRENTLY MANAGED FILES--")
	for item in masterlist:
		print(item.upper().rstrip("#"))
		
"""Prints all shortcuts in a given list"""
def printShortcuts(target, program):
	print(target.upper())
	print("___________")
	for shortcut in program:
		print(shortcut)
	
"""Submenu - intermediary that allows user to select file to search through"""
def viewAllShortcuts(masterlist):
	ctr = 0
	selector = []
	for item in masterlist:
		print(ctr,item.upper().rstrip("#"))
		selector.append(item)
		ctr += 1
	select = input("Which program would you like to search through? ")
	while select >= len(masterlist):
		select = input("Please select an option from the list of available programs: ")
	printShortcuts(selector[select],listGen(masterlist[select]))
	
"""Finds all files that contain this particular entry"""
def searchByEntry(masterlist):
	entry = raw_input("Which entry would you like to search for?")
	for item in masterlist:
		with open(item) as file_object:
			for line in file_object:
				if line.startswith(str(entry)):
					print(item.upper())

"""Takes data and appends to file"""
def appendNewShortcut(masterlist):
	
	ctr = 0
	selector = []
	for item in masterlist:
		print(ctr,item.upper().rstrip("#"))
		selector.append(item)
		ctr += 1
	select = raw_input("Please choose a program to edit: ")
	while select > len(masterlist) - 1:
		select = input("Please select an option from the list of available programs: ")
	
	print("Please remember to enter use this format: shortcut name shortcut keys!")
	newKey = raw_input("Enter the new shortcut: ")
	
	with open(selector[select], 'a') as file_object:
		file_object.write(newKey)

"""Creates a new file"""
def createNewFile():
	target = raw_input("Please enter the name of the program with no file extension: ")
	target = target.lower()
	target = target + "#"
	with open(target, 'w') as file_object:
		print("File successfully created.\n")
