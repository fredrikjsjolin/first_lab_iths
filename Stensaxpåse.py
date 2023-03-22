import random

list = ["sten", "sax", "påse"]

random_word = random.choice(list)
   
my_choice = input("Sten, sax eller påse: ")

print("Datorns val:", random_word)

while my_choice == random_word:
    print("Oavgjort, försök igen")

    random_word = random.choice(list)
   
    my_choice = input("Sten, sax eller påse: ")

    print("Datorns val:", random_word)

if random_word == "sten" and my_choice == "påse" or random_word == "sax" and my_choice == "sten" or random_word == "påse" and my_choice == "sax":
        print("Du vann!")

else:
        print("Du förlorade..")
