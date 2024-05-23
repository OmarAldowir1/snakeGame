# x = 5
# if x < 10:
#     print("Smaller")
# if x > 20:
#     print("Bigger")
#
# print("finish")

# x = 5
# if x == 5:
#     print("Equals 5")
# if x > 4:
#     print("Greater than 4")
# if x >= 5:
#     print("Greater than or Equals 5")
# if x < 6:
#     print("Less than 6")
# if x <= 5:
#     print("Less than or Equals 5")
# if x != 6:
#     print("Not Equals 6")

# x = 5
# if x > 2:
#     print("Bigger than 2")
#     print("Still bigger")
# print("Done with 2")
#
# for i in range(x):
#     print(i)

# astr = 'Hello Bob'
# try:
#     istr = int(astr)
# except :
#     istr = -1
# print('First', istr)
# astr = '123'
# try:
#     istr = int(astr)
# except:
#     istr = -1
# print('Second', istr)

# astr = 'Bob'
# try:
#     print('Hello')
#     istr = int(astr)
#     print('There')
# except:
#     istr = -1
#
# print('Done', istr)

##Exercise

hours = int(input("Enter hour: "))
rate = int(input("Enter rate: "))

if hours <= 40:
    pay = hours * rate
else:
    extra = hours - 40
    print(extra)
    payWithExtra = (40 * rate) + (extra * rate * 1.5)

print(hours, rate, extra ,payWithExtra)
print(payWithExtra)