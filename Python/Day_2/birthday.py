def dictionary(dict):
    print('We know the birthdays of:')
    for key in dict:
        print(key)
def main():
    Bdays = {"sai": "14-06-2001","pavan": "25/10/2000","Tharun": "22/07/1999"}
    print('>>> Welcome to the birthday dictionary.')
    dictionary(Bdays)
    a = input(">>> Who's birthday do you want to look up?\n")
    result = Bdays[a] if a in Bdays else None
    if result == None:
        print('No Data')
    else:
        print(">>> {}'s birthday is {}".format(a, Bdays[a]))

if __name__ == "__main__":
    main()