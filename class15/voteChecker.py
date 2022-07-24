from datetime import date


def checkIfUserCanVote(birthYear):
    age = date.today().year - birthYear
    print(f"You're {age} years old")
    if(age < 16):
        return "YOU CAN'T VOTE"
    if(age < 18):
        return "YOU MAY VOTE"
    return "YOU HAVE TO VOTE"


# Main
print(checkIfUserCanVote(int(input("Enter your birth year: "))))
