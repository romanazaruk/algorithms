from collections import defaultdict


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.visited = {} # to separate elements of graph
        self.list = [] # stack for result
        for i in graph.copy():
            #Why i cant use .keys???
            if i not in self.visited:
                self.topological_sort(i)

    def topological_sort(self, vertex):
        self.visited[vertex] = True
        for i in self.graph[vertex]:
            if i not in self.visited.copy():
                self.topological_sort(i)
        self.list.append(vertex)


if __name__ == "__main__":
    documents = defaultdict(list)
    for line in open("in.txt"):
        docs = line.split()
        if len(docs) != 2:
            break
        documents[docs[0]].append(docs[1])
    result_stack = Graph(documents).list
    print(result_stack)
    out = open("out.txt", 'w')
    for result in result_stack:

        out.write(result + "\n")