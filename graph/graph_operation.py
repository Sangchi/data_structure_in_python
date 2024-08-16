class graph:

    def __init__(self,gdict=None):

        if gdict is None:
            gdict={}
        else:
            self.gdict=gdict

    def add_vertex(self,vertex):

        if vertex not in self.gdict.keys():
            self.gdict[vertex]=[]
            return True
        else:
            return False


    def add_ege(self,vertex,edge):

        self.gdict[vertex].append(edge)


    def print_dict(self):

        for vertex in self.gdict:
            print(vertex,":",self.gdict[vertex])

    def remove_ege(self,vertex,edge):

        if vertex in self.gdict:
            self.gdict[vertex].remove(edge)
            return True
        else:
            return f"edge connection not there in vertex!!"
        
    def remove_vertex(self,vertex):
        if vertex in self.gdict:
            for v in self.gdict:
                if vertex in self.gdict[v]:
                    self.gdict[v].remove(vertex)

            del self.gdict[vertex]


customdict={
    "a":["b","c"],
    "b":["a","d","f"],
    "c":["a","b","f"],
    "d":["b","e"],
    "e":["d","f"],
    "f":["b","c","e"]
}

obj=graph(customdict)
obj.add_vertex("g")
obj.add_ege("e","b")
obj.print_dict()
obj.remove_ege("e","f")
obj.print_dict()
obj.remove_vertex("g")
obj.print_dict()
