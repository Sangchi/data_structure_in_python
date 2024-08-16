class Graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}

        else:
            self.gdict=gdict

    def bfs_traverse(self,vertex):

        visited=set()
        visited.add(vertex)
        queue=[vertex]

        while queue:
            current_vertex=queue.pop(0)
            print(current_vertex)

            for node in self.gdict[current_vertex]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)


custom_dict={

    "A":["B","C"],
    "B":["A","E"],
    "C":["A","D"],
    "D":["C","E"],
    "E":["B","D"]
}

def main():

    graph=Graph(custom_dict)
    graph.bfs_traverse("A")

if __name__ =='__main__':
    main()

            