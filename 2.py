number = []
while True:
    try:
        number.append(int(input("enter the number to insert in list:")))
        answer = input("Are you done inserting in the list\nEnter yes/no\n")
        if answer == "yes":break
        else:continue
    except:
        print("Error")
        continue
print(number)
num = int(input("Enter the number to be searched\n"))
if num in number:
    print("The index position is:", number.index(num))
else:
    print(-1)
