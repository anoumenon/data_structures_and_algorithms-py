class Graph:
    def __init__(self):
        self.graph = {}

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass

    def add_vert(self, val):
        """
        """
        if val not in self.graph:
            self.graph[val] = {}

    def has_vert(self, val):
        """
        """
        if val in self.graph:
            return True
        else:
            return False

    def add_edge(self, v1, v2, weight):
        """
        """
        if v1 in self.graph:
            self.graph[v1].update({v2: weight})

    def get_neighbors(self, val):
        """
        """
        return self.graph[val]
