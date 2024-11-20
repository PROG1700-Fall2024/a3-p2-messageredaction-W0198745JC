#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #: W0198745
#Student Name:  Jenille Cheney 
def phraseInput():
    return input("Type a phrase (or quit to exit program): ".lower())

def redactInput():
    while (True):
        letterChoice=input("\nType a comma - seperated list of letters to redact: ".lower())
        if all(char.isalpha() or char == "," for char in letterChoice):  #brought what i learned from program 3 error checking here!
            return letterChoice
        else:
            print("Invalid entry. Please enter letters seperated by a comma (ex. a,b,c)")

def redactPhrase(_phrase,_letter):      #Parameters are my friend!
    return _phrase.replace(_letter, "_")

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    phrase=""
    
    redactLetters=[]
    #get input from user  Use a WHILE loop!
    while (True):          # used true so i could do an infinite loop to BREAK when using quit so that the user doesnt have to answer the redact input to end program
        phrase= phraseInput()
        if phrase=="quit":
            break

        redact=redactInput()  #need to figure out how to make this not happen when quit is typed
        #make it a list 
        redactLetters=redact.split(",") # originally had for loops to seperate but learned with W3schools that string can be read as a list .
    
        #print(redactLetters) - was checking output
        count=0
        #.replace goes in a loop using the redactedLetters list BOOM!
        for letter in phrase:    # FOR EACH LOOP!
            if letter.lower() in redactLetters: # fail safe for the input .lower()
                #replace removed letters with underscore 
                phrase=redactPhrase(phrase,letter) # using the right variables took me FOREVER
                count+=1
        # print(phrase)  - used these to check output
        # print(count)
    
        #print redacted input 
        print(f"Number of letters redacted: {count}")
        print(f"Redacted phrase: {phrase}")



    #really struggled with this program at first but I have finally had my lightbulb moment with functions and loops !!

    # YOUR CODE ENDS HERE

main()