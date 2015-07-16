''' Search specification for Word ladder problem '''

import os
import re

class Node(object):
    ''' Represents a node in the word ladder graph i.e. a word '''

    def __init__(self, state, depth):

        self.state = state
        self.depth = depth

        dir_path = os.path.dirname(os.path.abspath(__file__))
        self.dict_path = os.path.join(dir_path, "resources", "wordlist.txt")
        self.dict_path = os.path.normpath(self.dict_path)

    def get_depth(self):
        ''' Returns the depth of the Node in the search tree '''

        return self.depth

    def get_state(self):
        ''' Returns the state of the current node '''

        return self.state

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

        search_regex = re.compile(re_exp)
        matching_words = []

        try:

            f = open(self.dict_path, 'r')

            for word in f:
                if search_regex.search(word):
                    matching_words.append(word)

        except Exception as _:
            pass

        finally:
            f.close()
            return matching_words


    def get_next_nodes(self):
        ''' Returns the next nodes of this node. '''

        next_nodes = []
        search_regex = self.__generate_adj_words_regex__()

        for word in self.__get_matching_words__(search_regex):
            temp = Node(word, self.depth + 1)
            next_nodes.append(temp)

        return next_nodes
        