import random
countries = ["IRAN","ENGLAND","NETHERLANDS","TURKEY","RUSSIA","INDIA","IRAQ","GERMANY","CANADA","AMERICA" ]
fruits = [ "ORANGE","APPLE","BANANA","CUCUMBER","PINEAPPLE","PEACH","CHERRY","APRICOT","STRAWBERRY","POMEGRANATE" ]
logos = [ "C++","PYTHON","JAVA","JAVASCRIPT","PHP","SQL","SWIFT","RUBY","HTML","CSS" ]
objects = [ "DESK","GLASS","SOAP","TOWEL","TOOTHBRUSH","STOVE","LAMP","TELEVISION","CLOCK","MIRROR" ]
animals = [ "SHEEP","WOLF","ANT","LION","BUTTERFLY","CROW","COW","DOG","CAT","FISH" ]
colors = [ "ORANGE","YELLOW","BLUE","GREEN","BROWN","GRAY","BLACK","WHITE","RED","PINK" ]
while(True):
    print("""Choose the number of subject : 
    1. Country 
    2. Fruit 
    3. Logo 
    4. Object 
    5. Animal 
    6. Color """)
    n=int(input())
    #words=[" "," "," "," "," "," "," "," "," "," "]
    if(n==1):
        words=countries
    elif(n==2):
        words=fruits
    elif(n==3):
        words=logos
    elif(n==4):
        words=objects
    elif(n==5):
        words=animals
    elif(n==6):
        words=colors
    num=random.randint(0,9)
    w=words[num]
    score=len(w)
    count=0
    count=int(count)
    null=[]
    while(True):
        guess = False
        for char in w:
            if char in null:
                print(char,end=' ')
            else:
                print('_',end=' ')
        letter=input("\n\nPlease enter a letter : ")[0]
        asc=ord(letter)
        if (asc >= 97 and asc <= 123):
            asc -= 32
            letter=chr(asc)
        for i in range(len(w)):
            if (letter == w[i]):
                null.append(letter)
                count+=1
                guess = True
        if (guess == False):
              score-=1
              print("\nWRONG GUESS!!\nNOW....You have " ,score," opportunities")
        if (count == len(w)):
            print("The word is: ",w)
            print("\nCONGRATULATION....YOU WIN\n")
            print("Do you want to play again? 1.YES   2.NO")
            break
        if (score == 0):
            print("The word is: ",w)
            print("\nSORRY.....YOU LOOSE!!")
            print("Do you want to play again? 1.YES   2.NO")
            break