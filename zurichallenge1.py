# This code helps in calculating the amount of words in a given text
while True:
	try:
		print('This program helps in getting the amount of words in a given text')
		user_text = input('Enter text: ').strip()


		def no_of_words(text):
			"""function to help get the amount of words in a text"""
			list_of_words = text.split(' ')  # method to help separate each words after a space
			counter = 0
			for i in list_of_words:
				counter += 1
			return counter  # result of loop and amount of words in text.
		print(no_of_words(user_text))
		

	except ValueError:
		print('Make sure you separate each words in text by a space, check your entry and retry: ')

	rerun_program = input('Would you like to run program again(y/n): ').lower()
	if rerun_program == 'y':
		continue
	else:
		break
