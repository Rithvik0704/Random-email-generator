def random_email():
    import random
    firstname=['arun','anmol','david','dev']
    secondname=['ambani','singh','patel','kumar']
    number=random.randint(10,99)
    a=random.choice(firstname)
    b=random.choice(secondname)
    print(a+b+str(number)+"@gmail.com")
    another_email()

def another_email():
    print("print more?")
    options=input("y or n\n")
    if options=="y":
        random_email()
    else:
        print("thank you!")
random_email()
