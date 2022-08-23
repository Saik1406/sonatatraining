def count_words(name):
    result=name.split()
    return len(result)
name=input("enter a name:")
print(count_words(name))