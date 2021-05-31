#This program takes input as text file and prints the total word count
import sys

def word_count(inputfile):
   with open(inputfile,'r') as file:
     data = file.read()
     data.replace(","," ")
   return (len(data.split(" "))+1)

print("Total word count of the file "+str(sys.argv[1])+ " is " + str(word_count(sys.argv[1])))