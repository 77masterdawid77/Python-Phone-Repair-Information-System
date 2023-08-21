file1 = open('Screen.txt', 'r')
file2 = open('Battery.txt', 'r')
words1 = str(file1.read().split())
words2 = str(file2.read().split())
user = str.lower(str.split(input[("type one word which is the main problem of your phone?")])
if user in words1:
    ans1 = str.lower(input("is the problem with the screen?"))
    if ans1 == "yes":
        import Screen
    elif ans1 == "no":
        print ("plz try to explain again")
    else:
        print("error, plz try again")
elif user in words2:
    ans2 = str.lower(input("is the problem with the battery?"))
    if ans2 == "yes":
        import Battery
    elif ans1 == "no":
        print ("plz try to explain again")
        fileChecker()
    else:
        print("error, plz try again")
        fileChecker()
else:
    print ("did not understand, plz type again")
