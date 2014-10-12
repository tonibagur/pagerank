

class Graph(object):
    def __init__(self):
        self.nodes={}
        
    def add_node(self,label):
        self.nodes[label]=Node(self)
        return self
    
    def add_edge(self,source,target):
        self.nodes[source].outcome.add(target)
        self.nodes[target].income.add(source)
        return self

    def copy(self):
        new=Graph()
        new.nodes=dict([(k,self.nodes[k].copy(new)) for k in self.nodes.keys()])
        return new

    def init_page_rank(self,value):
        l=float(len(self.nodes.keys()))
        for k in self.nodes.keys():
            self.nodes[k].value=value/l

    def __str__(self):
        val= "----------------\n"
        for k in self.nodes:
            val+=k + " " + str(self.nodes[k].value) + '\n'
        return val



class Node(object):
    def __init__(self,graph):
        self.graph=graph
        self.income=set()
        self.outcome=set()
        self.value=0

    def copy(self,graph):
        new=Node(graph)
        new.income=self.income.copy()
        new.outcome=self.outcome.copy()
        new.value=self.value
        return new

class PageRankResult(object):
    def __init__(self,other=None,graph=None,total=None):
        if other:
            self.vals=other.vals.copy()
        else:
            node_count=len(graph.nodes.keys())
            node_init=float(total)/float(node_count)
            self.vals=dict([(k,node_init) for k in graph.nodes.keys() ])



def page_rank(g,total,beta):
    g.init_page_rank(total)
    print g
    for i in range(100):
        print "-------",i
        g2=g.copy()
        for k in g2.nodes.keys():
            g2.nodes[k].value=(1 - beta)/float(len(g2.nodes.keys()))
            for n in g.nodes[k].income:
                g2.nodes[k].value+=beta*g.nodes[n].value/float(len(g.nodes[n].outcome))
        totalg=sum([g2.nodes[z].value for z in g2.nodes.keys()])
        for k in g2.nodes.keys():
            g2.nodes[k].value+=(total-totalg)/float(len(g2.nodes.keys()))
        print g2
        g=g2
    return g

'''g=Graph().add_node('a').add_node('b').add_node('c')
g.add_edge('a','c').add_edge('a','b').add_edge('b','c').add_edge('c','c')

g2=page_rank(g,3.,0.7)


g=Graph().add_node('a').add_node('b').add_node('c')
g.add_edge('a','c').add_edge('a','b').add_edge('b','c').add_edge('c','a')

g2=page_rank(g,3.,0.85)
print g2.nodes['a'].value, '=', str(g2.nodes['c'].value + 0.15* g2.nodes['b'].value)
print str(0.85*g2.nodes['c'].value), '=', str(g2.nodes['b'].value + 0.575* g2.nodes['a'].value)
print str(0.95*g2.nodes['c'].value), '=', str(0.9*g2.nodes['b'].value + 0.475* g2.nodes['a'].value)
print str(g2.nodes['a'].value), '=', str(0.9*g2.nodes['c'].value + 0.05* g2.nodes['b'].value)



g=Graph().add_node('a').add_node('b').add_node('c')
g.add_edge('a','c').add_edge('a','b').add_edge('b','c').add_edge('c','a')

g2=page_rank(g,3.,1.)'''