
anagram_string = input("Enter your word: ")
#remove empty spaces
anagram_string = anagram_string.replace(" ","").upper()

remove_letters = input("remove letters: ")
remove_letters = remove_letters.upper()

#initialize with my string
newstr = anagram_string
for x in range (0, len(remove_letters)):
    newstr = newstr.replace(remove_letters[x],"",1)

print (newstr)
