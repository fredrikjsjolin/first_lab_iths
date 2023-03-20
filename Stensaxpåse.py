import random

list = ["sten", "sax", "påse"]

# while x != y:

random_word = random.choice(list)
   
my_choice = input("Sten, sax eller påse: ")
    # int_number = int(number)
    # print("Du skrev in talet", int_number)

print(random_word)

if my_choice == random_word:
    print("oavgjort")

elif random_word == "sten" and my_choice == "påse" or random_word == "sax" and my_choice == "sten":
    print("Du vann!")

elif random_word == "sten" and my_choice == "sax" or random_word == "sax" and my_choice == "påse":
    print("Du förlorade")

# elif random_word == "sax" and my_choice == "påse":
    # print("Du förlorade")

# elif random_word == "sax" and my_choice == "sten":
    # print("Du vann!")

else:
    print("påse ej def...")
