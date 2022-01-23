MyDic = {                 # -: first of all creat dictionary
    "Pankha" : "Fan",
    "Aam" : "Mango",
    "Kursi" : "Chair",
    "Mej" : "Table"
}

print("options are",MyDic.keys())       # this syntax will show all keys of the dictionary
a = input("Enter the hindi word\n")       # take keys from tha users by this 

print("The meaning of your word is :",MyDic.get(a))      #this syntax throw (none) instead of an error, if the word is not present in the dictionary.
