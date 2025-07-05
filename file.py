# this is a simple Python script to read the contents of a file and print it.
# It reads the file 'devops.txt' and prints its content to the console.
file=open('devops.txt','r')
# r == read mode
# w == write mode
# a == append mode
content =file.read()
print (content)
