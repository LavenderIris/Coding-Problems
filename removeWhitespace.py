string = "A corgi is cuter than black cat"
char_array = list(string)

"""def removeWhitespace(string):
    newstr = [" "] * len(string)
    index = 0
    for i in range (0, len(string)):
        if (string[i]!=" "):
            newstr[index] = string[i]
            index = index + 1
       
    return newstr[:index]
"""


def swapWhitespace(char_array):
    for i in range(0, len(char_array)-1):
        if ( (char_array[i] == " ") ):
            char_array[i],char_array[i+1] =  char_array[i+1], char_array[i]
    print (char_array)

swapWhitespace(char_array)
