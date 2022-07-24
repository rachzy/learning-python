def getSituation(average):
    if(average > 7):
        return "GOOD"
    if(average > 6):
        return "MEDIUM"
    return "BAD"


def grades(* grades, sit=False):
    """
        -> Function to analyze grades and situations of many students
        :param grades: one or more grades of students (works with many)
        :param sit: (optional) indicates if the program have to show or not the class situation
        :return: dict with info about the class in general
    """
    total = len(grades)
    highestGrade = max(grades)
    lowestGrade = min(grades)
    sum = 0
    for grade in grades:
        sum += grade
    average = sum / len(grades)

    finalValue = {"total": total, "highestGrade": highestGrade,
                  "lowestGrade": lowestGrade, "average": average}
    if(sit):
        finalValue["situation"] = getSituation(average)
    return finalValue


# Main
checkGrades = grades(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(checkGrades)