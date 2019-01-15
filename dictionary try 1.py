import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def Main():

    def retrieve_definition(word):
        word = word.lower()
        if word in data:
            return data[word]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        elif word == "expr":
            return exit() 
        elif len(get_close_matches(word, data.keys())) > 0:
            action = input("Did you mean %s instead?[y or n]" % get_close_matches(word, data.keys())[0])
            if(action=="y"):
                return data[get_close_matches(word,data.keys())[0]]
            elif(action =="n"):
                return ("the word is bad")
            else:
                return("what you sayin")
       

            
    word_user = input("Enter a word or expr to leave program: ")
    output = retrieve_definition(word_user)
   

    if type(output) == list:
        for item in output:
            print("-", item)
    else:
        print("-",output)
    Main()
if __name__ == '__main__':
    Main()
    
        
