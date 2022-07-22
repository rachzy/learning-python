values = []
for x in range(5):
    num = int(input("Enter a value: "))

    if(x == 0 or num > values[-1]):
        values.append(num)
        print(f"Added on position the end of the list!")
    else:
        insertPos = 0
        while insertPos < len(values):
            if(num <= values[insertPos]):
                values.insert(insertPos, num)
                print(f"Added on position {insertPos}...")
                break
            insertPos += 1
print(values)
