from time import sleep


def counter(start, end, step):
    if(step < 0):
        step *= -1

    if(step == 0):
        step = 1

    print("\n")
    print("=-" * 20)
    print(f"Counting from {start} to {end} ({step} by {step})")
    print("=-" * 20)

    stepDirection = 1
    if (start > end):
        stepDirection = -1

    for i in range(start, end + stepDirection, (step * stepDirection)):
        print(i, end=' ', flush=True)
        sleep(0.2)


counter(1, 10, 1)
counter(10, 0, 2)

print("\n")
print("=-" * 20)
print("Your turn now!")
startNum = int(input("Start: "))
endNum = int(input("End: "))
stepNum = int(input("Step: "))
counter(startNum, endNum, stepNum)
