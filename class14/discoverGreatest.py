from time import sleep


def discoverGreatest(*nums):
    print("=-" * 20)
    print("Analysing entered values...")

    for num in nums:
        print(num, end=' ', flush=True)
        sleep(0.3)
    print(f"A total of {len(nums)} values were entered")
    sleep(0.5)

    if(len(nums) == 0):
        nums = [0]
    print(f"The greatest value entered was {max(nums)}")
    sleep(1)

#Main
discoverGreatest(2, 9, 4, 5, 7, 1)
discoverGreatest(4, 7, 0)
discoverGreatest(1, 2)
discoverGreatest(6)
discoverGreatest()