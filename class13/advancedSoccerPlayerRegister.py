players = list()
player = dict()

while True:
    player["id"] = len(players)
    player["name"] = str(input("Player's name: "))
    amountOfMatches = int(input("Matches played: "))
    player["matches"] = list()
    player["amountOfGoals"] = 0

    for i in range(amountOfMatches):
        scoredGoals = int(input(f"Amount of goals scored in match {i + 1}: "))
        player["matches"].append(scoredGoals)
        player["amountOfGoals"] += scoredGoals
    players.append(player.copy())
    player.clear()

    choice = str(input("Wanna keep entering data? [Y/N]: ")).upper()
    if(choice == "N"):
        break

print('=-' * 50)
print('ID', end=' ' * 12)
print('NAME', end=' ' * 10)
print('GOALS', end=' ' * 9)
print('TOTAL')
print('-' * 50)

for player in players:
    for v in player.values():
        print(v, end=' ' * (14 - len(str(v))))
    print('\n')
print('=-' * 50)

choice = int(input("Show data of which player? (Enter their ID): "))

while choice != 999:
    if choice > len(players) - 1:
        print("Player not found")
    else:
        print(f"-- PLAYER {players[choice]['name']}")

        for pos, goals in enumerate(players[choice]["matches"]):
            print(f"=> In match {pos + 1}, scored {goals} goals.")
        
        print('-' * 20)

    choice = int(input("Show data of which player? (Enter their ID): "))
