# This code helps in reading the contents stored in a file, it also helps in getting the amount of
# times a particular unique word occurs in the file
import os
os.chdir('C:\\Users\\MY PC\\Desktop')
my_file = input('Enter name of file(remember to add the file extension): ')


def read_file_content(filename):
    """function to help read the contents stored in a .txt file"""
    with open(str(filename), 'r') as file:
        content = file.read()
        return content# returning the content of a file as a string


print(read_file_content(my_file))
print()


def count_words(filename):
    """function to help calculate the amount of times a particular word occus in the file"""
    with open(filename, 'r') as name_of_file:
        file_content = name_of_file.read()
        list_of_words = file_content.split()# spliting the contents in the file and converting to a list
        occurence_counter = {} # creating an empty list 
        for word in list_of_words:
            if word in occurence_counter: # adding each word as a key into the dictionary
                occurence_counter[word] += 1 # increasing the value by 1 on every new occurences
            else:
                occurence_counter[word] = 1 # retaining it as 1 if there is no new occurences
        return occurence_counter


print(count_words('story.txt')) 
