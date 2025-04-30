# ##For Loop
# ## for item in list_of_items:
# #       do something:

# fruits = ["apple","peach","pear"]
# for fruit in fruits:
#     print(fruit)
# scores = [87, 73, 65, 92, 48, 77, 81, 69, 54, 100, 39, 62, 85, 71, 58, 93, 44, 66, 79, 88, 51, 60, 90, 83, 75, 68, 57, 46, 99, 74]
# total_exam_score = sum(scores)
# print(total_exam_score)

# summ = 0

# for score in scores:
#     summ += score

# print(summ)
scores = [87, 73, 65, 92, 48, 77, 81, 69, 54, 100, 39, 62, 85, 71, 58, 93, 44, 66, 79, 88, 51, 60, 90, 83, 75, 68, 57, 46, 99, 74, 10000]
max = 0
for score in scores:
    if(score>max):
        max = score
print (max)
        