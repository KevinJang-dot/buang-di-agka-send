userdata = int(input("Enter how many numbers: "))
user_nums = []

for i in range(userdata):
    numbers = int(input("numbers:"))
    user_nums.append(numbers)

print(user_nums)

for x in user_nums:
    users_Answer = input("Do you want to clear the numbers or leave it unchanged, yes if you want, no if not: ")
    if users_Answer == "yes":
        user_nums.clear()
        print(user_nums)
    elif users_Answer == "no":
        print(user_nums)
