def listtoString(s):                    # method declaration for conversion of list to string   
    str1=""                             # declaring an empty string
    for x in s:                         # take an element from the list
        str1+=x                         # append it with the empty string
    return str1                         # once the process is completed return the string
f1=open("myfile.txt",'r')              # open the text file, file path, and r indiyates that i am opening the file in read mode
line=f1.readlines()                     # read the complete text file into a list such that each element denotee corresponding line
f1.close()                              # once all content is transfered from text file to list close the file
i=0                                     # variable declaration used for iterating
while i < len(line):                    # while the iterator is less than the length of the list
    a=line[i].replace("\n","")          # access the variable of the list(specific line) and remove all "\n" characters and assign it to variable a
    line[i]=a                           # assign variable a to the specific list variable in that position
    i+=1                                # increment the iterator
str2=listtoString(line)                 # convert list to string
correct=str2.split(".")                 # as each sentences' profanity needs to be checked, as a sentence closes with a full stop we will divide the string into a list by splitting the string at '.' fullstop
diy1={"idiot":1,"stupid":1,"donkey":1}  # profanity level1
diy2={"shrewd":3,"cunning":3,"demagouge":3}# profanity level 2
diy3={"monkey":10,"rat":10}                # profanity level 3
prof=0                                  # profanity variable assigned to zero initially
for i in correct:                      # access the element in the list 'correct'
    prof=0                              # profanity variable assigned to zero initially
    for word in diy3:                   # access the key value in the harsh diytionary
        if word in i:                   # check if the word exists in the selected list value(sentence)
            prof+=diy3[word]            # if exists then assign profainity word value to prof variable
            break                       # once we have determined the hiegest level profainity in a sentence we dont need to go further
        else:                           # if word does not exist then continue to next word in the diytionary
            continue
    for word in diy2:                   # access the key value in the medium diytionary
        if word in i:                   # check if the word exists in the selected list value(sentence)
            prof+=diy2[word]            # once we have determined the hiegest level profainity in a sentence we dont need to go further
            break                       
        else:                           # if word does not exist then continue to next word in the diytionary
            continue
    for word in diy1:                   # access the key value in the mild diytionary
        if word in i:                   # check if the word exists in the selected list value(sentence)
            prof+=diy1[word]            # once we have determined the hiegest level profainity in a sentence we dont need to go further
        else:
            continue                    # if word does not exist then continue to next word in the diytionary
    if (prof>0)&(prof<2):               # if profanity is 1 then sentence contains mild profanity
        print(i,"-- Sentence is Mild Profanity\n")  # print the premise with conclusion
    elif (prof>2)&(prof<5):             # if profanity is 5 then sentence contains medium profanity
        print(i,"-- Sentence is Medium Profanity\n")# print the premise with conclusion
    elif (prof>9)&(prof<11):            # if profanity is 10 then sentence contains harsh profanity
        print(i,"-- Sentence is Harsh Profanity\n") # print the premise with conclusion
    elif (prof<1)&(i!=""):               # if profanity is 0 then sentence contains no profanity
        print(i,"-- this sentence has no profanity\n") # print the premise with conclusion
   
