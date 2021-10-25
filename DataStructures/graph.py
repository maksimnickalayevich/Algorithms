from typing import List, Union, Dict, Any, Optional, Tuple


class GNode:
    def __init__(self, name: str, neighbours: List):
        self.name = name
        self.neighbours = neighbours


class Graph:
    """
    Implementation on graphs in python with internal dicts
    """
    def __init__(self, graphDict=None):
        if graphDict is None:
            graphDict = {}
        self.relations = graphDict
        self._queue: List = []

    def __repr__(self):
        return str(self.relations)

    def addNode(self, node: GNode):
        self.relations[node.name] = node.neighbours

    def getNodeNeighbours(self, nodeName: str):
        return self.relations.get(nodeName, [])

    def getAllNodeNames(self):
        return list(self.relations.keys())

    def getAllNeighbours(self):
        return list(self.relations.values())

    def addToQueue(self, values: Union[List, str, int, float]):
        if isinstance(values, List):
            self._queue.extend(values)
        else:
            self._queue.append(values)

    # def createHashTables(self, names: List[str]):
    #     for n in names:
    #         setattr(self, n, {})
    #     print(f"Hash tables with names <{', '.join(n for n in names)}> were added")
    #
    # def getHashTable(self, name):
    #     hashTable = getattr(self, name, None)
    #     return hashTable
    #
    # def setValue(self, hashTableName: str, values: List[Tuple]):
    #     hashTable: Optional[Dict] = self.getHashTable(hashTableName)
    #     if hashTable is None:
    #         raise AttributeError(f"No such table with name {hashTable}")
    #     for k, v in values:
    #         hashTable[k] = v
    #     setattr(self, hashTableName, hashTable)
    #
    # def showHashes(self):
    #     return self.__dict__

    def getQueue(self):
        return self._queue
