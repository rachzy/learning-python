player = dict()
player["name"] = str(input("Player's name: "))
player["amountOfMatches"] = int(input("Matches played: "))
player["amountOfGoals"] = 0
player["matches"] = list()

for i in range(player["amountOfMatches"]):
    match = dict()
    match["id"] = i + 1
    match["scoredGoals"] = int(input(f"Amount of goals scored in match {i + 1}: "))
    player["matches"].append(match.copy())
    player["amountOfGoals"] += match["scoredGoals"]

print('=-' * 30)
print(player)
print('=-' * 30)
for k, v in player.items():
    if(k != "matches"):
        print(f"{k}: {v}")
    else:
        for match in player["matches"]:
            print(f"=> In match {match['id']}, scored {match['scoredGoals']} goals.")
print('=-' * 30)