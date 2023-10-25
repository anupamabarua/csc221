string=input("Enter a string: ")
letter=input("Enter a letter to remove: ")

if letter in string:
    nstring = string.replace(letter, "")
    print(nstring)
else:
    print('Your letter is not there')
