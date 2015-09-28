import string
d = dict.fromkeys(string.ascii_lowercase, 0)

mystr = "We promptly judged antique ivory buckles for the  prize"
mystr = mystr.replace(" ", "").lower()

#setting everything
for i in range(0, len(mystr)):
    d[mystr[i]] = 1    

if 0 in d.values():
    print ("not a pangram")
else:
    print ("pangram")
