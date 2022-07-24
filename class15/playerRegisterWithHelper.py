def registerPlayer(name="<unknown>", goals=0):
    print(f"The player {name} scored {goals} in the tournament.")


# Main
name = input("Player's name: ").strip()
goals = input("Amount of goals: ").strip()

if(goals.isnumeric()):
    goals = int(goals)
else:
    goals = 0

if(name == ""):
    registerPlayer(goals=goals)
else:
    registerPlayer(name, goals)
