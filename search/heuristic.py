''' Heuristic class holds the heuristic functions used for A* search '''


def levenshtein_distance(word1, word2, i=None, j=None):
    '''
    Returns the levenshtein distance between the two words
    Args:
        1) word1: 1st word
        2) word2: 2nd word
    '''

    if i is None:
        i = len(word1)
    if j is None:
        j = len(word2)

    if min(i, j) == 0:
        return max(i, j)

    comp1 = levenshtein_distance(word1, word2, i-1, j) + 1
    comp2 = levenshtein_distance(word1, word2, i, j-1) + 1

    indicator = 1

    if word1[i-1] == word2[j-1]:
        indicator = 0

    comp3 = levenshtein_distance(word1, word2, i-1, j-1) + indicator

    return min(comp1, comp2, comp3)
