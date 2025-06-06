from choice import treasure
treasure_choice = int(input("Enter your choise of a chest(1-3): "))
if treasure_choice == treasure:
    print("Congrats! You found the treasure!")
else:
    print("Sorry, you didn't guess the chest")