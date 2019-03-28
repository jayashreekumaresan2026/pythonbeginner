# def picking_number():
#
#     l = [4,6,5,3,3,1]
#     maximum = 0
#     for i in l:
#         c = l.count(i)
#         d = l.count(i - 1)
#         c = c + d
#         if c > maximum:
#             maximum = c
#     print(maximum)
#
# picking_number()
def picking_number():
    l = [1 ,2, 2, 3, 1, 2]
    l.sort()
    maximum_count = 0
    for i in range(0, len(l)+1):
        count = 0
        for j in range(i + 1, len(l)):
            if abs(l[i] - l[j]) <= 1:
                count = count + 1
                if count > maximum_count:
                    maximum_count = count
    print(maximum_count+1)


picking_number()
