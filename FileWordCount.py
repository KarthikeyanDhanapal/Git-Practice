#This program takes input as text file and prints the total word count
#it does not count the very first word in each new line - need to use REGEX
import sys

def word_count(inputfile):
   with open(inputfile,'r') as file:  #with handles exceptions automatically
     data = file.read()
     data.replace(","," ")            #Just "" will have no delimiter, have it as " "
     blank=len(data.split(" "))
     newline=len(data.split("\n"))
   return(int(blank+newline))    #As the count is based on blank space, the very first word is to be accounted

print("Total word count of the file "+str(sys.argv[1])+ " is " + str(word_count(sys.argv[1])))