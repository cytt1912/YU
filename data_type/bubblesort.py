##±È½ÏÅÅĞò
# list = [1,3,5,7,0,4,9]
# lenth = len(list)
# j = 0
# while j < lenth:
#     for a in range(lenth-1-j):
#         if list[j] > list[lenth-1-a]:
#             list[j],list[lenth-1-a] = list[lenth-1-a],list[j]
#         print(list)
#     j = j +1
#     print("############")
# print(list)
#
#bubblesort
list1 = [1,3,9,6,2,5,7]
for i in range(len(list1)-1):
    for j in range(len(list1)-1-i):
        if list1[j] >list1[j+1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]
print(list1)

