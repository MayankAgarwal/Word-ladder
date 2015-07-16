''' Implements various search mechanisms '''

from node import Node

class Search(object):
    ''' Contains search methods '''

    def __init__(self, start_state, end_state):
        self.start_state = start_state
        self.end_state = end_state


    def astar_search(self):
        ''' Implements A-star search '''

        visited_words = []

        start_node = Node(self.start_state, 0, self.end_state)

        current_node = start_node

        fringe = [current_node]

        while not current_node.is_state_result():

            if not fringe:
                return "ERROR: No path exists"

            visited_words.append(current_node.state)

            next_nodes = current_node.get_next_nodes()

            for node in next_nodes:
                if node.state in visited_words:
                    continue
                else:
                    fringe.append(node)

            fringe.remove(current_node)
            current_node = self.__get_least_cost_astar(fringe)

        return current_node


    @classmethod
    def __get_least_cost_astar(cls, fringe):
        ''' Returns the least costing element from fringe '''

        return sorted(fringe, key=lambda node: node.depth + node.h_distance)[0]


if __name__ == '__main__':
    word1 = raw_input("Enter 1st word: ")
    word2 = raw_input("Enter 2nd word: ")

    temp = Search(word1, word2)
    result = temp.astar_search()
    path = []

    while result is not None:
        path.insert(0, result.state)
        result = result.parent


    print " -> ".join(path)
