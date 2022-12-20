file1 = open('input.txt', 'r')
rounds = file1.readlines()

# X - loose
# Y - draw
# Z - win

# rok ->1
# paper -> 2
# scisors -> 3

# A - rock
# B - paper
# C - scisors

total_score = 0

for rnd in rounds:
    oponent = rnd[0]
    me = rnd[2]

    choice_score = 0
    result_score = 0

    my_choise = ""

    #kedy si dam rock
    if (oponent == "A" and me == "Y") or (oponent == "C" and me == "Z") or (oponent == "B" and me == "X"):
        my_choise = "rock"

    #kedy dam paper
    if(oponent == "B" and me == "Y") or (me == "Z" and oponent == "A") or (me == "X" and oponent == "C"):
        my_choise = "paper"
    
    #kedy si dam scisors
    if (me == "Y" and oponent == "C") or (me == "X" and oponent == "A") or (me == "Z" and oponent == "B"):
        my_choise = "scisors"

    match my_choise:
        case "rock":
            choice_score = 1
        case "paper":
            choice_score = 2
        case "scisors":
            choice_score = 3

    
    if (my_choise == "rock" and oponent == "A") or (my_choise == "paper" and oponent == "B") or (my_choise == "scisors" and oponent == "C"):
        result_score = 3
    
    if (my_choise == "rock" and oponent == "C") or (my_choise == "paper" and oponent == "A") or (my_choise == "scisors" and oponent == "B"):
        result_score = 6

    total_score = total_score + result_score + choice_score
    

print(total_score)