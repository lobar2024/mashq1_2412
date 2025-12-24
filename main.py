# 1) 1 dan 20 gacha bo‘lgan juft sonlar
list1 = [i for i in range(1, 21) if i % 2 == 0]

# 2) nums ichidan toq sonlarning kvadrati
nums = [3, 6, 1, 8, 4, 9]
list2 = [i**2 for i in nums if i % 2 != 0]

# 3) katta harf bilan boshlanadigan so‘zlar
names = ["Ali", "olma", "Salom", "python"]
list3 = [word for word in names if word[0].isupper()]

# 4) musbat sonlar
numbers = [-5, 3, -2, 8, 0]
list4 = [i for i in numbers if i > 0]

print(list1, list2, list3, list4)
