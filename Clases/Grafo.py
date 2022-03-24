class Grafo(object):
   
    def __init__(self, id='grafo', dirigido=False):
        self.id =       id
        self.dirigido = dirigido
        self.V =        dict()
        self.E =        dict()
        self.attr =     dict()

    def __repr__(self):
      
        return str("id: " + str(self.id) + '\n'
                   + 'nodos: ' + str(self.V.values()) + '\n'
                   + 'aristas: ' + str(self.E.values()))

    def add_nodo(self, nodo):
       
        self.V[nodo.id] = nodo

    def add_arista(self, arista):
       
        if self.get_arista(arista.id):
            return False

        self.E[arista.id] = arista
        return True

    def get_arista(self, arista_id):
       
        if self.dirigido:
            return arista_id in self.E
        else:
            u, v = arista_id
            return (u, v) in self.E or (v, u) in self.E

    def to_graphviz(self, filename):
       
        edge_connector = "--"
        graph_directive = "graph"
        if self.dirigido:
            edge_connector = "->"
            graph_directive = "digraph"

        with open(filename, 'w') as f:
            f.write(f"{graph_directive} {self.id} " + " {\n")
            for nodo in self.V:
                f.write(f"{nodo};\n")
            for arista in self.E.values():
                f.write(f"{arista.u} {edge_connector} {arista.v};\n")
            f.write("}")