#program to reverse the letters in a word.
#input the word
sWord = str(input("Please input your word."))
#reverse the word
for char in range(len(sWord) -1, -1, -1):
    print(sWord[char], end="")
print("")