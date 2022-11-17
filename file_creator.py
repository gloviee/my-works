#my first work at all include work with files after reading the book about python language by "Erric Mattes"
#NOW i read 200 pages and at the moment i'm able to do something like this 
#english can be crooked enough, sorry if there is a problem while reading

#author 'exluse'

filenames = []

def format_text_file():
	'''Input name of file and add it to the library'''
	while True:
		filename = input('Filename: ')
		if filename == 'q':
			break
		filenames.append(filename)

	for filename in filenames:
		formmated_text_file = f"text/{filename}.txt"
		create_file(formmated_text_file)

def create_file(filename):
	'''Create file with name which user would like to'''
	with open(filename, 'a') as f:
		a = ''
		f.write(a)

def operations_with_files(add_data_to_formmated_text_file):
	'''Determine operation with file'''
	try:
		with open(add_data_to_formmated_text_file) as f:
			content = f.read()
	except FileNotFoundError:
		print(f"The '{add_data_to_formmated_text_file}' does not exist.")
	else:
		OPERATIONS = ['r', 'a', 'r and a']
		operation = input("Do you want reset file or add some data? Choose 'r' to reset and 'a' to add, you can also reset and add new data with 'r and a': ")
		while operation not in OPERATIONS:
			operation = input("Do you want reset file or add some data? Choose 'r' to reset and 'a' to add, you can also reset and add new data with 'r and a': ")
		
		if operation == 'r':
			reset_file_data(add_data_to_formmated_text_file)
		elif operation == 'r and a':
			reset_and_add_new_data_to_file(add_data_to_formmated_text_file)
		elif operation == 'a':
			add_data_to_text_file(add_data_to_formmated_text_file)
		else:
			print("Uncorrect operation value. ")

def add_data_to_text_file(add_data_to_formmated_text_file):
	'''Add some data to the text file'''
	with open(add_data_to_formmated_text_file, 'a') as f:
		data = input('What do you want add to this file? ')
		f.write(f"\n{data}")

	print("Your new data succssesfully added!")	

def reset_file_data(add_data_to_formmated_text_file):
	'''Reset file data'''
	with open(add_data_to_formmated_text_file, 'w') as f:
		a = ''
		f.write(a)

	print("Your data has been already deleted")

def reset_and_add_new_data_to_file(add_data_to_formmated_text_file):
	'''Reset and add new data to the specific file.'''
	with open(add_data_to_formmated_text_file, 'w') as f:
		a = input("Enter text you wont to change. ")
		f.write(a)

	print("Your file contains new data now.")


format_text_file()

add_data_to_formmated_text_file = input('Enter file name which you want to add data: ')
operations_with_files(f"text/{add_data_to_formmated_text_file}.txt")