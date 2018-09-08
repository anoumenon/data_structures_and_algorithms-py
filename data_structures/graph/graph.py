class Graph:
    def __init__(self):
        """
        ini
        """
        self.graph = {}

    def __repr__(self):
        """
        IN: self
        OUT: graph dict
        """
        return f'{self.graph}'

    def __str__(self):
        """
        IN: self
        OUT: graph dict
        """
        return f'GRAPH: {self.graph}'

    def __len__(self):
        """
        IN: self
        OUT: vert count
        """
        return len(self.graph.keys())

    def add_vert(self, val):
        """
        IN: val to be added as vert
        OUT: updated graph
        """
        if val not in self.graph:
            self.graph[val] = {}
            return self.graph
        else:
            return False

    def has_vert(self, val):
        """
        IN: vert val to be checked for
        OUT: confirmation
        """
        if val in self.graph:
            return True
        else:
            return False

    def add_edge(self, v1, v2, weight):
        """
        IN: edge to be added between vert one and two
        OUT: updated graph
        """
        if v1 in self.graph:
            self.graph[v1].update({v2: weight})
            return self.graph
        else:
            return False

    def get_neighbors(self, val):
        """
        IN: val of vert
        OUT: edges of selected vert
        """
        return self.graph[val]
