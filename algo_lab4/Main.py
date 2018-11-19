input1 = "NNYN NNYN NNNN NYYN"
input2 = "NNNN NNNN NNNN NNNN"
input3 = "NNN NNN NNN"

class Graph:
    def __init__(self, size):
        self.vertexes = {}
        for i in range(size):
            self.vertexes[i] = []

    def add_vertex(self, v1, v2):
        self.vertexes[v1].append(v2)

    def get_salary(self, elem):
        salary = 0

        if len(self.vertexes[elem]) == 0:
            return 1

        for neighbor in self.vertexes[elem]:
            salary += self.get_salary(neighbor)
        return salary


def count_all_salaries(m):
    graph = Graph(m.__len__())

    for i in range(m.__len__()):
        for j in range(m.__len__()):
            if m[i][j] is 'Y':
                graph.add_vertex(i, j)

    all_salaries = 0
    for i in range(m.__len__()):
        all_salaries += graph.get_salary(i)

    print(all_salaries)


def parse_string(str):
    rows = str.split(" ")
    matrix = []
    for i in range(rows.__len__()):
        matrix.append(list(rows[i]))
    return matrix


matrix = parse_string(input1)
count_all_salaries(matrix)
