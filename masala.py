# # 1
#
#
#
# print("1 dan 10 gacha sonlar:")
#
# for i in range(1, 11):
#     print(i)

# # 2
# ismlar = ["Ali", "Vali", "Hasan", "Malika", "Zuhra"]
#
# for ism in ismlar:
#     print(f"Salom {ism}!")

# # 3
# print("1 dan 100 gacha bolgan sonlar:")
# for son in range(0,101,2):
#     print(son)

# # 4
# son = 0
# for son1 in range(1,51):
#     son = son + son1
#     print(son)

# # 5
# matn = input("Matn kiriting:")
# uznlikk = 0
# for belgi in matn:
#     uznlikk = uznlikk + 1
# print("Matn uzunligi:",uznlikk, "belgi")

# # 6
# print("/n1 dan 50 gacha 3 ga bolinadigan sonlar")
# ozgaruvchi = 0
# for son in range(1, 50):
#     if son % 3 == 0:
#         print(son)
#         ozgaruvchi = ozgaruvchi + 1
#         print("Jami son:", ozgaruvchi , "son")

# # 7
# matn = input("\n Matn kiriting: ")
# unlilar = "asdfghjkllqwwerty"
# sanoq = 0
# for belgi in matn.lower():
#     if belgi in unlilar:
#         sanoq = sanoq + 1
# print("Jami unli harflar:", sanoq, "ta")

# # 8
# sonlar = [23, 67, 12, 89, 45, 34, 91, 56, 78]
#
# eng_katta = sonlar[0]
#
# for son in sonlar:
#     if son > eng_katta:
#         eng_katta = son
#
# print("Eng katta son:", eng_katta)

# # 9
#
# son = input("Son kiriting: ")
#
#
# yigindi = 0
#
# for belgi in son:
#     if belgi.isdigit():
#         yigindi += int(belgi)
#
# print(f"{son} sonining raqamlari yig'indisi: {yigindi}")

# # 10
#
# son = int(input("Son kiriting: "))
#
# if son < 0:
#     print("Manfiy sonlar uchun faktorial aniqlanmagan!")
#
# elif son == 0 or son == 1:
#     print(f"{son}! = 1")
#
# else:
#     faktorial = 1
#     for i in range(1, son + 1):
#         faktorial *= i
#     print(f"{son}! = {faktorial}")

# # 11
# print("Multiplikatsiya jadvali (1–10)\n")
#
# print("   ", end="")
# for i in range(1, 11):
#     print(f"{i:4}", end="")
# print()
#
# print("   " + "-" * 40)
# for i in range(1, 11):
#
#     print(f"{i:2} |", end="")
#
#
#     for j in range(1, 11):
#         print(f"{i * j:4}", end="")


