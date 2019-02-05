from collections import Counter
element1 = {'a': 100, 'b': 200, 'c':300}
element2 = {'a': 300, 'b': 200, 'd':400}
sum_of_elements = Counter(element1) + Counter(element2)
print(sum_of_elements)








