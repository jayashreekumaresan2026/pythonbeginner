def user_input():
    first_split="A,600,B,C,B"
    second_split="B,400,C,E"
    third_split="C,800,A,B,C,D,E"

def splitwise_problem(first_split,second_split,third_split):
    dict={"A":0,"B":0,"C":0,"D":0,"E":0}
    element=dict.split(",")

    amount=first_split

    for key in element:
        dict[key]=dict[key]+amount
