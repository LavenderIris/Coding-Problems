"""
string = "hello my name is"
newstr = []

def reverseString(string):
    for i in range(len(string)-1, -1, -1):
        newstr.append(string[i])
    return newstr

revStr = reverseString(string)

print("".join(revStr))
"""

string = "hello my name is2"
char_array = list(string)

def swapChar(char_array):
    # I will only swap half of my array
    half = int(len(char_array)/ 2)
    print("what" + str(half))    
    for i in range(0, half):
        char_array[i], char_array[len(char_array)-1 - i] = char_array[len(char_array)-1 - i] , char_array[i]    
    return (char_array)

newstr = "".join(swapChar(char_array))
print (newstr)

