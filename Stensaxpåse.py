import random

list = ["sten", "sax", "påse"]

random_word = random.choice(list)
   
my_choice = input("Sten, sax eller påse: ")

print("Datorns val: ", random_word)

if my_choice == random_word:
    print("Oavgjort")

elif random_word == "sten" and my_choice == "påse" or random_word == "sax" and my_choice == "sten" or random_word == "påse" and my_choice == "sax":
    print("Du vann!")

# elif random_word == "sten" and my_choice == "sax" or random_word == "sax" and my_choice == "påse" or random_word == "påse" and my_choice == "sten":
    # print("Du förlorade..")

else:
    print("Du förlorade..")


