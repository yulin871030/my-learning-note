from collections import defaultdict 

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def BFS(self, s): 
        queue = []
        final = []
        final.append(s)
        queue = queue+self.graph[s]
        while len(queue) != 0:
            s = queue.pop(0)
            final.append(s)
            plus = []
            plus = plus+self.graph[s]
            for i in plus:
                if i in queue:
                    plus = [n for n in plus if n != i]
            for i in plus:
                if i in final:
                    plus = [n for n in plus if n != i]
            queue = queue+plus
        return final
    def DFS(self, s):
        stack = []
        final = []
        final.append(s)
        stack = stack+self.graph[s]
        while len(stack) != 0:
            s = stack.pop()
            final.append(s)
            plus = []
            plus = plus+self.graph[s]
            for i in plus:
                if i in stack:
                    plus = [n for n in plus if n != i]
            for i in plus:
                if i in final:
                    plus = [n for n in plus if n != i]
            stack = stack+plus
        return final
