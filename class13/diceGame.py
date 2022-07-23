from operator import itemgetter
from random import randint
from time import sleep

players = dict()

print("=-" * 5, end=' ')
print("VALORES SORTEADOS", end=' ')
print("=-" * 5)
for i in range(4):
    players[f"player{i}"] = randint(1, 6)

for k, v in players.items():
    sleep(0.5)
    print(f">> {k} got {v} points")

sleep(1)

ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print("=-" * 5, end=' ')
print("RANKING", end=' ')
print("=-" * 5)
for pos, player in enumerate(ranking):
    print(f"{pos + 1} place: {player[0]} with {player[1]} points")
