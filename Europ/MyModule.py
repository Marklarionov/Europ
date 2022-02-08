from random import *
def file_read():
    dict = {}
    file = open("Country.txt","r",encoding = "utf-8-sig")
    for line in file:
        town,count = line.strip().split(":")
        dict[town.strip()] = count.strip()
    file.close()
    return dict

def new_word(dict):
    word = input("Enter the country you want to add >>> ")
    word2 = input("Enter the capital you want to add >>> ")
    with open("Country.txt","a",encoding = "utf-8-sig") as fail:
        fail.write(word + ":" + word2 + "\n")
    dict[word] = word2
    print(f"Country {word} and its capital {word2} added")

def test(score:int,l:list,l2:list)->int:
    word = choice(l)
    otvet = input(f"{word} -- ")
    if otvet in l2: 
        if l2.index(otvet) == l.index(word):
            score += 1
            print("Good")
    else:
        print("Bad")
    return score