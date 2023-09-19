# Names: Gerardo Pineda, Sebastian Wong, Issac Mugre, JeSUS Rizz "Chewy"
#######################paired programmming###############################

# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.
magic = 'abracadabra'
print(magic[5])
print(magic[-2])
print(magic.find ("c"))

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicing.
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet.find("h"))
print(alphabet[7:9])
alphabet2 = "abcdefghijklm"
print(alphabet2[0::2])
print(alphabet[::-1])

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
speech = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(speech.find('John F. Kennedy'))
print(speech.find('dy'))
print(speech[83:98])

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
info = "Python is fun. Fun is good. Good is subjective."
print(info[-11:-1])
words = info.split() # Split the variable and then printed the third words alone.
third_word = words[2::3]
print(third_word)
reversed_words = ' '.join(words[::-1]) # Joined the split words but in reverse.
print(reversed_words)

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
sentence3 = "MAY THE FORCE BE WITH YOU"
print(sentence3.upper())
print(sentence3.lower())

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.
motto = ["Make", "haste", "slowly."]
finalstring = ' '.join(motto)
print(finalstring) #a
print(finalstring.split('a')) #b

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
sen = "Life is what happens when you are busy making other plans."
print(sen.replace('busy', 'distracted'))
print(sen.replace('plans', 'mistakes'))

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
print('Iteration' * 7)