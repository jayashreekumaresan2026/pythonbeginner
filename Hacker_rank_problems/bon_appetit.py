# get the total item eaten by both the people
total_item_eaten = 4
# get the index of the item which anna did not eaten
index_of_item_anna_not_taken = 1
# get the cost of the each item eaten by the both user
cost_of_the_item = [3, 10, 2, 9]
# get the charged amount
charged_amount = 12
# remove the cost does not eaten by anna
del cost_of_the_item[index_of_item_anna_not_taken]
# add the cost in the final_list
sum_the_item = 0
for i in range(0, len(cost_of_the_item)):
    # get the each and every item and sum the cost
    sum_the_item = sum_the_item + cost_of_the_item[i]
# divide the item for the check per cost
each_person_cost = sum_the_item // 2
actual_cost = charged_amount - each_person_cost
# check the actual_cost is equal to the sum_cost
if actual_cost != 0:
    # print the cost if no equal to zero
    print(actual_cost)
else:
    # print the word if the charge_amount_equal_to_actual_cost
    print("Bon Appetit")
