class Graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}

        else:
            self.gdict=gdict


    def dfs_traverse(self,vertex):

        visited=set()
        stack=[vertex]

        while stack:
            current_vertex=stack.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)
            for node in self.gdict[current_vertex]:
                if node not  in visited:
                    stack.append(node)


custom_dict={
    "A":["B","C"],
    "B":["A","E"],
    "C":["A","D"],
    "D":["C","E"],
    "E":["B","D"]
}


graph=Graph(custom_dict)
graph.dfs_traverse("A")

