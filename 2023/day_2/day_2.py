# X = LOSE
# Y = DRAW
# Z = WIN

standard_points = {'A X': 4, 'A Y': 8, 'A Z': 3,
                   'B X': 1, 'B Y': 5, 'B Z': 9,
                   'C X': 7, 'C Y': 2, 'C Z': 6}

second_points = {'A X': 3, 'A Y': 4, 'A Z': 8,
                 'B X': 1, 'B Y': 5, 'B Z': 9,
                 'C X': 2, 'C Y': 6, 'C Z': 7}


with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    print(sum([standard_points[l] for l in lines]))
    print(sum([second_points[l] for l in lines]))
