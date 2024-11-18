#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #: W0198745
#Student Name:  Jenille Cheney 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    phrase=""
    
    redactLetters=[]

    while (phrase != "quit"):
        phrase= input("Type a phrase (or quit to exit program): ".lower())
        redact= input("Type a comma - seperated list of letters to redact: ".lower())
        redactLetters = redact.split(",")
    
        print(redactLetters)
        count=0
        for letter in phrase:
            if letter in redactLetters:
                phrase=phrase.replace(letter, "_")
                count+=1
        print(phrase)


        #.replace goes in a loop using the redactedLetters list BOOM!
        
    #get input from user  Use a WHILE loop!
    #make it a list 
    #remove desired letters
    #replace removed letters with underscore 
    #print redacted input 
    #print(f"Number of letters redacted: {}")






    # YOUR CODE ENDS HERE

main()