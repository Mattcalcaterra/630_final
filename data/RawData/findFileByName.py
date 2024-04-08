import os
from glob import glob
from nltk.tokenize import sent_tokenize, word_tokenize
numberSen = 0
numberWord = 0
prefixPath = "/Users/sarahmasudpreum/Dropbox/PerComJournal/drug_data/"
suffixPath = "/handout.txt"

files = []
start_dir = os.getcwd()
pattern   = "handout.txt"
#'/Users/sarahmasudpreum/Dropbox/PerComJournal/drug_data/Zonegran/handout.txt'
for dir,_,_ in os.walk(start_dir):
    path = glob(os.path.join(dir,pattern))
    files.append(path)
    print(path)
    pathS = "".join(path)
    temp = pathS.split('/')
##    print(temp)
    counter = 0
    for item in temp:
        counter += 1
        if (counter == 7):
            pathF =  prefixPath + item + suffixPath
            print(pathF)
            rfile = open(pathF, "r")
            for line in rfile:
                    for sent in sent_tokenize(line):
                        numberSen += 1
                        for word in word_tokenize (sent):
                                           numberWord += 1

            
print(len(files))
print (numberSen)
print (numberWord)
