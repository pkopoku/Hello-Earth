#We received an email from earth, we want to count the number of words in it
#Yes, we're weird like that

email = open("email.txt","r+")

#Create a dictionary to store every word
wordcount = {}

#Loop through the file and count every word

for word in email.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

print(wordcount)
