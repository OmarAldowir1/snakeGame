# x = 0
# while x <= 10:
#     print(x)
#     x += 1

# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends:
#     print("Hello: ", friend)
# print("Done")

largest_number = -1
print('before: ', largest_number)
for i in [9, 41, 12, 3, 74, 15]:
    if i > largest_number:
        largest_number = i
    print(largest_number, i)
print('after: ', largest_number)