import random

def RollDie(size):
    random.seed()
    die = random.randint(1, size)
    return die

def RollStats():
    stats = [0, 0, 0, 0, 0, 0]
    attempts = 0

    statsNotFound = True
    while statsNotFound == True:
        stats = [0, 0, 0, 0, 0, 0]
        for statIndex, stat in enumerate(stats):
            dice = [0, 0, 0, 0]
            for dieIndex, die in enumerate(dice):
                dice[dieIndex] = RollDie(6)
            dice.remove(min(dice))
            stats[statIndex] = sum(dice)

        attempts += 1
        print(f"\n")
        print(f"Attempt #{attempts}:")
        print(f"\t{stats[0]}\t{stats[1]}\t{stats[2]}\t{stats[3]}\t{stats[4]}\t{stats[5]}")

        # Uses list comprehension to find the number of elements in the list that meet the condition (ex: stat <= 8).
        numEQorLess8 = len([stat for stat in stats if stat <= 8])
        numGreaterorEQ15 = len([stat for stat in stats if stat >= 15])

        if numEQorLess8 <= 2 and numGreaterorEQ15 >= 2:
            statsNotFound = False
            print("Found good stats!")

    return stats
"""
This program can be expanded to function as a text-based character stat and skill builder.
I could do this in the future by adding support for multiple saved character sheets and by
adding proficiencies, skills, and features from 5E.
Right now, though, it's just gonna be a basic stat roller that will roll until certain
conditions are met.
Specifically:
    1. 4d6 per stat (drop the lowest).
    2. Reroll if more than two stats 8 or lower.
    3. Reroll if less than two stats 15 or higher.
"""
def main():
    isRunning = True

    print("Welcome to Dicer: The Dice Rolling Simulator!")
    print("")
    while isRunning == True:
        print("Please choose a command (type the number of the command)")
        print(f"\t1. Roll for stats.")
        print(f"\t2. Quit.")
        print("")
        choice = int(input("Please enter your choice: "))
        print("")
        if choice == 1:
            print("Rolling Stats...")
            stats = RollStats()
            print(f"\t{stats[0]}\t{stats[1]}\t{stats[2]}\t{stats[3]}\t{stats[4]}\t{stats[5]}")
        elif choice == 2:
            print("Goodbye :)")
            isRunning = False;
        else:
            print(f"Invalid command entered!")
        print("")

if __name__ == "__main__":
    main()