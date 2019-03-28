# get the first_kangaroo starting_point
first_kangaroo_starting = 0
# get the distance of the first kangaroo can jump
first_kangaroo_jump = 3
# get the second kangaroo starting_point
second_kangaroo_starting = 4
# get the distance of the second kangaroo can jump
second_kangaroo_jump = 2
result = (first_kangaroo_starting - second_kangaroo_jump) % (first_kangaroo_jump - second_kangaroo_jump)

if result == 0:
    print("yes")
else:
    print("no")
