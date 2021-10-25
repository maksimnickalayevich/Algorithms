from typing import Any, Dict, List
from DataStructures.graph import Graph, GNode


def breadthFirstSearch(gr: Graph, queue, searchValue: Any):
    """
    Implementation of Breadth-First-Search for graphs
    :param gr:
    :param queue:
    :param searchValue:
    :return:
    """
    already_checked: List = []
    searched_person: str = ""
    while queue:
        candidate: Dict[str, bool] = queue.pop(0)
        name = list(candidate.keys())[0]
        if name in already_checked:
            continue
        seller: bool = is_seller(candidate)
        if seller == searchValue:
            searched_person = name
            break
        # Avoid checking 1 person several times
        already_checked.append(name)

        neighbs: List = gr.getNodeNeighbours(name)
        queue.extend(neighbs)

    return searched_person


def is_seller(person: Dict[str, bool]):
    result: bool = person.get(list(person.keys())[0], None)
    return result



# Create Graph
# gr = Graph()
# Populate it with values
# gr.addNode(GNode("Me", [{"Alice": False}, {"Bob": False}, {"Claire": False}]))
# gr.addNode(GNode("Alice", [{"Kristie": True}, {"John": False}]))
# gr.addNode(GNode("Bob", [{"Alex": False}, {"Rebecca": True}]))

# Create queue for searching
# gr.addToQueue(gr.getNodeNeighbours("Me"))
# searchQueue = gr.getQueue()
# Search for  mango seller
# If seller = name, if not = ""
# mango_seller = breadthFirstSearch(gr, searchQueue, True)
# print(mango_seller)

