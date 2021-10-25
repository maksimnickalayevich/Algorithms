from typing import Dict, List, Optional


def dijkstra(graphs: Dict, costs: Dict, parents: Dict):
    """
    Implementation of dijkstra algorithm for finding shortest path
    :param graphs:
    :param costs:
    :param parents:
    :return:
    """
    alreadyChecked = []
    lowest_node = findSmallestCost(costs, alreadyChecked)
    while lowest_node:
        lowest_cost = costs.get(lowest_node)
        neighbs = graphs.get(lowest_node)
        for nodeName in neighbs.keys():
            # Sum lowest cost + cost of the neighbour
            new_cost = lowest_cost + neighbs.get(nodeName)
            if costs[nodeName] > new_cost:
                costs[nodeName] = new_cost
                parents[nodeName] = lowest_node
        alreadyChecked.append(lowest_node)
        lowest_node = findSmallestCost(costs, alreadyChecked)

    return parents


def findSmallestCost(costs: Dict, already_checked: List):
    lowest_cost = float("inf")
    lowest_node = None
    for n, w in costs.items():
        if w < lowest_cost and n not in already_checked:
            lowest_cost = w
            lowest_node = n

    return lowest_node


def prettyShow(graphs: Dict, new_parents: Dict):
    """
    Returns ordered list of path
    :param graphs: initial graph
    :param new_parents: result of the dijkstra algorithm
    :return:
    """
    start_value: str = list(graphs.keys())[0]
    result_path = f"{start_value} --> "
    for i in range(len(new_parents.keys())):
        found_key = getByValue(start_value, new_parents)
        result_path += f"{found_key}"
        if i < len(new_parents.keys()) - 1:
            result_path += " --> "
        start_value = found_key

    return result_path


def getByValue(value: str, new_parents: Dict):
    for k, v in new_parents.items():
        if v == value:
            return k
    return None


def main():
    # init all the necessary data
    graphs: Dict = {"start": {"a": 6, "b": 2}, "a": {"end": 1}, "b": {"a": 3, "end": 5}, "end": {}}
    costs: Dict = {"a": 6, "b": 2, "end": float("inf")}
    parents: Dict = {"a": "start", "b": "start", "end": None}
    # Find shortest path
    new_parents: Dict = dijkstra(graphs, costs, parents)
    # Shows the shortest path prettily
    path: str = prettyShow(graphs, new_parents)
    print(path)


if __name__ == "__main__":
    main()
