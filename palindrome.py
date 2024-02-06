fh = open('output.txt','w')

a = input("Enter the string : ")
reverse = a[::-1]

fh.write("The String is : " + a + '\n')
if reverse == a:
    fh.write("palindrone " + '\n')
else:
    fh.write("it's not" + '\n')

