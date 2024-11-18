#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #: W0198745
#Student Name:  Jenille Cheney 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    phrase=""
    
    redactLetters=[]
    #get input from user  Use a WHILE loop!
    while (True):          # used true so i could do an infinite loop to BREAK when using quit so that the user doesnt have to answer the redact input to end program
        phrase= input("Type a phrase (or quit to exit program): ".lower())
        if phrase == "quit":
            break

        redact= input("\nType a comma - seperated list of letters to redact: ".lower()) #need to figure out how to make this not happen when quit is typed
        #make it a list 
        redactLetters=redact.split(",") # originally had for loops to seperate but learned with W3schools that string can be read as a list .
    
        #print(redactLetters) - was checking output
        count=0
        #.replace goes in a loop using the redactedLetters list BOOM!
        for letter in phrase:    # FOR EACH LOOP!
            if letter.lower() in redactLetters: # fail safe for the input .lower()
                #replace removed letters with underscore 
                phrase=phrase.replace(letter, "_") # using the right variables took me FOREVER
                count+=1
        # print(phrase)  - used these to check output
        # print(count)
    
        #print redacted input 
        print(f"Number of letters redacted: {count}")
        print(f"Redacted phrase: {phrase}")






    # YOUR CODE ENDS HERE

main()