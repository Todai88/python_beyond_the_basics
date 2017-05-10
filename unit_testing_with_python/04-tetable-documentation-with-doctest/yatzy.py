def get_highest_individual_score(dice):
    """
    @param 
        dice: a dictionary with the each key being a side of a dice and value being their occurrence.
    @return: the highest possible score where side * occurrence
    """
    return max([key * value for key, value in dice_counts(dice).items()])

def dice_counts(dice):
    """
    @param 
        dice: takes a collection of integers indicating the dice(s) rolled 
    @return: a dictionary showing how many times every dice has been rolled.
    """
    return {x: dice.count(x) for x in range(1, 7)}

def yatzy(dice):
    """
    @param 
        dice: a collection of integers indicating the dice(s) rolled 
    @return:  an integer score
    """
    if 5 in dice_counts(dice).values():
        return 50
    return 0




def small_straight(dice):
    """
    @param 
        dice: a list of 5 integers indicating the dice rolled 
        
    @return: 
        an integer score
    """
    if sorted(dice) == [1,2,3,4,5]:
        return sum(dice)
    else:
        return 0


def full_house(dice):
    """
    @param 
        dice: a collection of integers indicating the dice(s) rolled.
    @return: 
        an integer score
    """
    tmp_count = dice_counts(dice)
    if 2 in tmp_count.values() and 3 in tmp_count.values():
        return sum(dice)
    return 0


ALL_CATEGORIES = [full_house, yatzy, small_straight, get_highest_individual_score]

def scores_in_categories(dice, categories=ALL_CATEGORIES):
    """
    @param 
        dice: a collection of integers indicating the dice(s) rolled   
    @param 
        categories: an optional category, by default ALL_CATEGORIES
    @return: the optimized score for your dice
    """

    from operator import itemgetter
    scores = [(category(dice), category.__name__)
                for category in categories
                    if category(dice) > 0]
    return sorted(scores, reverse=True, key=itemgetter(0))
