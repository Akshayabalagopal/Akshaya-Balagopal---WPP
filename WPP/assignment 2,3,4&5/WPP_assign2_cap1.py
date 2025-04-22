'''Write a program that asks the user to enter a word and then capitalizes every other letter of the word. 
so, if the user enters rhinoceros, the program should print rHiNoCeRoS.
'''

word=input("Enter the word: ")
for i in range(len(word)):
    if i%2==1:
        print(word[i].upper(), end='')
        continue
    else:
        print(word[i], end='')
        continue
