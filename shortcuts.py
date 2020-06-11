import shortcutFunctions as sf

def mainMenu():
	print("--------------------------")
	print("Hello there! My name is Kenobi! I like to manage files!")
	print("How can I help you today?\n\n")
	print("--OPTIONS--")
	print("1. Show me the files you're currently managing")
	print("2. Show me the entries in a file")
	print("3. Show me the files that have this particular entry")
	print("4. Allow me to add a new line to a file")
	print("5. Allow me to add a new file\n")
	select = input("Enter selection and press 'Enter': ")
	while int(select) > 5 or int(select) <= 0:
		select = input("Please enter a number from the menu: ")
	if select == 1:
		sf.printNames(sf.collectFiles())
		mainMenu()
	elif select == 2:
		sf.viewAllShortcuts(sf.collectFiles())
		mainMenu()
	elif select == 3:
		sf.searchByEntry(sf.collectFiles())
		mainMenu()
	elif select == 4:
		sf.appendNewShortcut(sf.collectFiles())
		mainMenu()
	elif select == 5:
		sf.createNewFile()
		mainMenu()
		
mainMenu()




	


