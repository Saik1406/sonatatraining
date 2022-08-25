def myfile():
    try:
        c=open("sai.txt.txt", 'r')
        print(c.read())
    except(FileNotFoundError):
        return "not exists"
f=myfile()
print(f)