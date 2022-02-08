from MyModule import *
from random import *
dict = file_read()
country = [i for i in dict.keys()]
capitals = [i for i in dict.keys()]
print("This is a dictionary where all the countries of Europe and their capitals are recorded")
while True:
    print("""Choose what you want to do
    1 - Show all countries
    2 - Search for countries and capitals
    3 - New country and capital
    4 - Error correction
    5 - Test
    6 - To exit the dictionary""")
    menu=int(input("Your choise: "))
    if menu==1:
        for key, value in dict.items():
            print(key + " - " + value)
    elif menu==2:
        word = input(" ")
        if word in capitals:
            print(word + " - " + dict[word])
        elif word in country:
            print(word + " - " + capitals[country.index(word)])
        else:
            print(f"countries or capitals {word} not in the dictionary")
    elif menu==3:
        new_word(dict)
    #elif menu==4:
    elif menu==5:
        print("Enter the correct answers")
        score = 0
        for i in range(5):
            number = randint(1,2)
            if number == 1:
                score = test(score,capitals,country)
            else:
                score = test(score,country,capitals)
        mark = score * 100 / 5
        print(f"Your {score}/5 points")
        if mark >= 90:
            print("Good, mark 5!")
        elif mark >= 75 and mark <= 90:
            print("Good, mark 4!")
        elif mark >= 50 and mark <= 75:
            print("Good, mark 3!")
        else:
            print("2 is bad, try better!")
        print()
    elif menu==6:
        exit()     
    else:
        print("Invalid data type!")
