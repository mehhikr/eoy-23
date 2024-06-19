counter = 0
wordlist = []
consocount = 0
vowellist = "aeiouAEIOU"
while counter < 3:
    x = input("Enter a string\n")
    if x == "qqq":
        print("Program early termination! Mimi terminated Program Early!")
        print(wordlist)
        print(consocount)
        break
    if len(x) > 5 and x.isalpha():
        vowelcounter = 0
        for letter in x:
            if letter in vowellist:
                vowelcounter += 1
        if vowelcounter < 5:
            wordlist.append(x)
            print(wordlist) #by leefy
            counter += 1
            for letter in x:
                if letter not in vowellist:
                    consocount += 1

if counter == 3:
    print(wordlist)
    print(consocount)

#words used
#Round 1- elephant, vice (rejected), hello123 (rejected),delicacies (rejected), computer, pencilcase
#Round 2 -elephant, delicacies (rejected), pencilcase, qqq

#Marking points - infinite loop program

#validate for 6 letters or more -1 (1)
#validate for only letters -1 (1)
#validate for not more than 4 vowels, but accept 4 vowels -1 (1)
#accepts only 3 words -1   (1)
#prompt for re entry if validation fails with correct continue structure -1 (1)
#collect 3 words in an array - 1 (1)
#implement 'qqq' to terminate program - 1 (1)
#after 'qqq'is entered will print out the number of consonants that are so far collected - 1 (1)
#nested for loop to do the count of the consonants -1 (1)
#initialise the counter for consonants, increment and print out the correct count of consonants - 1 (1)

#total = 10
