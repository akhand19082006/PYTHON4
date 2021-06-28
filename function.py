def countWords():
    a=input("Enter the file Name :")
    b=open(a,'r')
    count=0
    for c in b:
        word = c.split()
        count=count+len(word)
    print("Number of Words:")
    print(count)
countWords()