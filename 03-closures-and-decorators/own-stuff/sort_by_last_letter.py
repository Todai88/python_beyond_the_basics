## Here I will show how to use a local function


def sort_by_last_letter(list_of_words):
    """
    @param list_of_words: a list containing words
    @return: the passed list sorted on their last character.
    """
    def last_letter(s):
        """
        :param s: a string 
        :return:  the last character in parameter s. 
        """
        return s[-1]
    return sorted(list_of_words, key=last_letter)