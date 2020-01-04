from collections import defaultdict 

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.dict = defaultdict(list) 
    def addEdge(self,u,v,w): 
        self.dict[w].append([u,v])
    def Dijkstra(self, s): 
        answer = {}
        for num in range(self.V):
            final = self.graph[num]
            for i in range(self.V):
                for each in range(len(final)):
                    if final[each] != 0:
                        nextlist = self.graph[each]
                        for deep in range(len(nextlist)):
                            if nextlist[deep] != 0:
                                if final[deep] == 0 or final[deep] > final[each] + nextlist[deep]:
                                    final[deep] = final[each] + nextlist[deep]
            self.graph[num] = final
        
        for i in range(self.V):
            self.graph[i][i] = 0
            
        for i in range(self.V):
            answer[str(i)] = self.graph[s][i]
            
        return answer
    def Kruskal(self):
        answer={}
        check = [column for column in range(self.V)]  
        val = sorted(self.dict)
        for i in val:
            for f,s in self.dict[i]:
                if check[f] == check[s]:
                    pass
                else:
                    check = [check[f] if x==check[s] else x for x in check]
                    answer[str(f)+'-'+str(s)] = i
        return answer
