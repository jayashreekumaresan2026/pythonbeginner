def compare_triplets(persons1, persons2):
    person1_points = 0
    person2_points = 0
    for num in range(0, len(persons1)):
        if persons1[num] > persons2[num]:
            person1_points = person1_points + 1
        elif persons1[num] == persons2[num]:
            continue
        else:
            person2_points = person2_points + 1

    print(person1_points, person2_points)


compare_triplets([5, 6, 7], [3, 6, 10])
