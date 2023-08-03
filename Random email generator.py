#program to generate a random email.
#create a class as random_email.
def random_email():
    import random
     #random first name
    firstname=['arun','anmol','david','dev']
     #random second name
    secondname=['ambani','singh','patel','kumar']
     #random.randit()function chooses numbers between the given range
    number=random.randint(10,99)
     #chooses a random name
    a=random.choice(firstname)
    b=random.choice(secondname)
     #printing the finial output
    print(a+b+str(number)+"@gmail.com")
    another_email()

def another_email():
    print("print more?")
     #options y=yes, n=no
    options=input("y or n\n")
    if options=="y":
        random_email()
    else:
        print("thank you!")
random_email()
