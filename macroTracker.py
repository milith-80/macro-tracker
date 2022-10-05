from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

proteinGoal = int(input("Enter your desired intake of protein (grams): "))
carbsGoal = int(input("Enter your desired intake of carbohydrates (grams): "))
fatsGoal = int(input("Enter your desired intake of fats: (grams) "))

macroLog = []


@dataclass
class Macros:
    name: str
    protein: int
    fat: int
    carbs: int


terminate = False

while not terminate:
    print("""
       (1) Add a new food
       (2) Visualize progress 
       (0) Quit
       **At least 2 foods required to view Macro Goal Over Time data (graphs on bottom row)
       ***Maximize data/output window for best experience
       """)

    choice = input("Choose an option: ")

    if choice == "1":
        print("Adding a new food!")
        name = input("Name of food: ")
        proteins = int(input("Protein (g): "))
        fats = int(input("Fats (g): "))
        carbs = int(input("Carbs (g): "))
        food = Macros(name, proteins, fats, carbs)
        macroLog.append(food)
        print("Successfully added!")
    elif choice == "2":

        protein_sum = sum(food.protein for food in macroLog)
        fats_sum = sum(food.fat for food in macroLog)
        carbs_sum = sum(food.carbs for food in macroLog)

        fig, macroChart = plt.subplots(3, 3)
        macroChart[0, 0].pie([protein_sum, fats_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"], autopct="%1.1f%%")
        macroChart[0, 0].set_title("Macronutrients\n Consumption Distribution (g)", fontweight="bold")

        macroChart[0, 1].bar_label(macroChart[0, 1].barh(["Protein Consumed", "Fat Consumed", "Carbs Consumed"], [protein_sum, fats_sum, carbs_sum]))
        macroChart[0, 1].bar_label(macroChart[0, 1].barh(["Protein Goal", "Fat Goal", "Carbs Goal"], [proteinGoal, fatsGoal, carbsGoal]))
        macroChart[0, 1].set_title("Macronutrients Progress (g)", fontweight="bold")

        macroChart[0, 2].pie([proteinGoal, fatsGoal, carbsGoal], labels=["Proteins", "Fats", "Carbs"], autopct="%1.1f%%")
        macroChart[0, 2].set_title("Macronutrients Goals Distribution (g)", fontweight="bold")

        proteinRemain = 0
        carbsRemain = 0
        fatsRemain = 0

        if proteinGoal > protein_sum:
            macroChart[1, 0].pie([protein_sum, proteinGoal - protein_sum], labels=["Protein Consumed", "Remaining"],
                          autopct="%1.1f%%")
        else:
            proteinRemain = 0
            macroChart[1, 0].pie([protein_sum, proteinRemain], labels=["Protein Consumed", "Remaining"], autopct="%1.1f%%")
        macroChart[1, 0].set_title("Protein Goal Progress (g)", fontweight="bold")

        if carbsGoal > carbs_sum:
            macroChart[1, 1].pie([carbs_sum, carbsGoal - carbs_sum], labels=["Carbs Consumed", "Remaining"],
                          autopct="%1.1f%%")
        else:
            carbsRemain = 0
            macroChart[1, 1].pie([carbs_sum, carbsRemain], labels=["Carbs Consumed", "Remaining"], autopct="%1.1f%%")
        macroChart[1, 1].set_title("Carbs Goal Progress (g)", fontweight="bold")

        if fatsGoal > fats_sum:
            macroChart[1, 2].pie([fats_sum, fatsGoal - fats_sum], labels=["Fats Consumed", "Remaining"],
                          autopct="%1.1f%%")
        else:
            fatsRemain = 0
            macroChart[1, 2].pie([fats_sum, fatsRemain], labels=["Fats Consumed", "Remaining"], autopct="%1.1f%%")
        macroChart[1, 2].set_title("Fats Goal Progress (g)", fontweight="bold")

        macroChart[2, 0].plot(list(range(len(macroLog))), np.cumsum([food.protein for food in macroLog]),label="Protein Eaten")
        macroChart[2, 0].plot(list(range(len(macroLog))), [proteinGoal] * len(macroLog), label="Protein Goal\n Limit")
        macroChart[2, 0].legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize= "xx-small")
        macroChart[2, 0].set_title("Protein Goal Over Time (g)", fontweight="bold")

        macroChart[2, 1].plot(list(range(len(macroLog))), np.cumsum([food.carbs for food in macroLog]), label="Carbs Eaten")
        macroChart[2, 1].plot(list(range(len(macroLog))), [carbsGoal] * len(macroLog), label="Carbs Goal\n Limit")
        macroChart[2, 1].legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize= "xx-small")
        macroChart[2, 1].set_title("Carbs Goal Over Time (g)", fontweight="bold")

        macroChart[2, 2].plot(list(range(len(macroLog))), np.cumsum([food.fat for food in macroLog]), label="Fats Eaten")
        macroChart[2, 2].plot(list(range(len(macroLog))), [fatsGoal] * len(macroLog), label="Fat Goal\n Limit")
        macroChart[2, 2].legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize= "xx-small")
        macroChart[2, 2].set_title("Fats Goal Over Time (g)", fontweight="bold")

        fig.tight_layout()
        plt.show()


    elif choice == "0":
        terminate = True
    else:
        print("Invalid Choice!")
