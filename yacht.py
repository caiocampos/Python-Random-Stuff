# Score categories.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

STRAIGHT = [1, 2, 3, 4, 5, 6]


def score(dice, category):
    if category == YACHT:
        return 50 if dice.count(dice[0]) == 5 else 0
    if category == CHOICE:
        return sum(dice)
    if category >= ONES and category <= SIXES:
        return category * dice.count(category)
    if category == FULL_HOUSE or category == FOUR_OF_A_KIND:
        d0 = dice[0]
        d1, c0, c1 = 0, 0, 0
        for d in dice:
            if d == d0:
                c0 += 1
                continue
            if d == d1:
                c1 += 1
                continue
            if d1 == 0:
                d1 = d
                c1 = 1
            else:
                return 0
        if category == FOUR_OF_A_KIND:
            if c0 >= 4:
                return 4 * d0
            if c1 >= 4:
                return 4 * d1
            return 0
        return sum(dice) if c0 == 3 or c1 == 3 else 0
    dice.sort()
    if category == LITTLE_STRAIGHT:
        return 30 if STRAIGHT[0:5] == dice else 0
    return 30 if STRAIGHT[1:6] == dice else 0
