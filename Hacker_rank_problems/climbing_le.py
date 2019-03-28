def climbingLeaderboard(scores, alice):
    scores = sorted(set(scores))
    index = 0
    rank_list = []
    n = len(scores)
    for i in alice:
        while (n > index and i >= scores[index]):
            index += 1
        rank_list.append(n +1 - index)
        print(rank_list)
    return rank_list


scores = [100, 100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]
print(climbingLeaderboard(scores, alice))
