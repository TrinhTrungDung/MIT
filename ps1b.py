###########################
# 6.0002 Problem Set 1b: Space Change
# Name: Trinh Trung Dung
# Time: 1 hour
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # initializing a list of lists in which columns are from 0 to target_weight
    dynamic_table = []
    # initializing a list representing each row in the drownamic_table
    row = []
    # initializing the first row in which each entry is equal to the fewest number of eggs can be brought back
    # by dividing the target_weight by the smallest egg weight
    for i in range(target_weight + 1):
        row.append(i // egg_weights[0])
    dynamic_table.append(row)
    # initializing remain entries which are equal to 0
    for i in range(len(egg_weights) - 1):
        row = []
        for j in range(target_weight + 1):
            row.append(0)
        dynamic_table.append(row)
    # for each entry from 2nd row to last row, we calculate the smallest number of eggs by these conditions:
    # if the column (fitted weight) is greater than or equal to the egg weight,
    # then we take the minimum of the top value or go back "egg weight" column value then + 1
    # else we just take the top value
    for i in range(1, len(egg_weights)):
        for j in range(target_weight + 1):
            if j >= egg_weights[i]:
                dynamic_table[i][j] = min(dynamic_table[i - 1][j], dynamic_table[i][j - egg_weights[i]] + 1)
            else:
                dynamic_table[i][j] = dynamic_table[i - 1][j]
    # return the smallest number of eggs by taking the last entry of the table
    return dynamic_table[len(egg_weights) - 1][target_weight]

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
