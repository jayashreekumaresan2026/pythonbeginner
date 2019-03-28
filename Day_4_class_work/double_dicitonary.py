# # dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# # for (k, v) in dict1.items():
# #     dict1[k*2] = v
# # print(dict1)
# # Take user input
# number = 2
#
# # Condition of the while loop
# while number < 5 :
#     print("Thank you")
#     # Increment the value of the variable "number by 1"
#     number = number+1
nested_dict = {'first': {'a': 1}, 'second': {'b': 2}}

for (outer_k, outer_v) in nested_dict.items():
    for (inner_k, inner_v) in outer_v.items():
        outer_v.update({inner_k: float(inner_v)})
nested_dict.update({outer_k: outer_v})

print(nested_dict)
