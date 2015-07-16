''' Search specification for Word ladder problem '''

import os
import re
import heuristic

class Node(object):
    ''' Represents a node in the word ladder graph i.e. a word '''

    def __init__(self, state, depth, result_state, parent=None):

        self.state = state     # current state
        self.depth = depth          # Depth of the current state in search graph
        self.result_state = result_state    # Result state the search is looking for

        # parent node of the current state
        self.parent = parent

        # Heuristic distance between current state and result state
        self.h_distance = heuristic.levenshtein_distance(self.state, self.result_state)

        # Path to absolute english dictionary
        dir_path = os.path.dirname(os.path.abspath(__file__))
        self.dict_path = os.path.join(dir_path, "resources", "wordlist.txt")
        self.dict_path = os.path.normpath(self.dict_path)


    def is_state_result(self):
        ''' Returns True if the current state is the result state '''

        return self.state.strip().lower() == self.result_state.strip().lower()

    def __generate_adj_words_regex__(self):
        ''' 
        Generates a regex that matches words adjacent (one character modification away 
        from state)
        '''

        regex = []

        start_regex = r"^\w" + self.state + r"$"
        end_regex = r"^" + self.state + r"\w$"

        regex.append(start_regex)
        regex.append(end_regex)

        state_temp = "^" + self.state + "$"

        for i in xrange(1, len(state_temp)-1):
            mid_pos_regex = state_temp[0:i] + r"\w" + state_temp[i+1:]
            regex.append(mid_pos_regex)

        return "|".join(regex)


    def __get_matching_words__(self, re_exp):
        ''' Returns a list of words matching the passed regular expression '''

        search_regex = re.compile(re_exp, re.IGNORECASE)
        matching_words = []

        try:

            f = open(self.dict_path, 'r')

            for word in f:
                if search_regex.search(word) and word.strip().lower() != self.state.strip().lower():
                    matching_words.append(word.strip())

        except Exception as _:
            pass

        finally:
            f.close()
            return matching_words


    def get_next_nodes(self):
        ''' Returns the next nodes of this node. '''

        adjacent_nodes = []
        search_regex = self.__generate_adj_words_regex__()

        for matched_word in self.__get_matching_words__(search_regex):
            node_temp = Node(matched_word, self.depth + 1, self.result_state, self)
            adjacent_nodes.append(node_temp)

        return adjacent_nodes
    