# 流程圖

![](/images/BFS.jpg)




# BFS與DFS原理

* BFS原理

   * BFS (Breadth-First-Search) ——廣度優先搜尋, 是從根節點開始，遍歷完畢整張圖，不考慮結果所在的位置， 無論如何都要遍歷完畢整張地圖才終止。 按照就近      原則進行， 距離原點相同的節點的訪問順序是相近的。


     BFS使用　'queue'　來進行儲存未被檢測的節點，利用佇列的先進先出的特點來按照寬度訪問查詢等待計算的節點。
    
* DFS原理

   * DFS (Depth-First-Search)——深度優先搜尋，是從根節點開始， 逐個訪問每一條路徑， 對於具有多子節點的節點而言，先搜尋到某一條子路的最深處，再逐個回        溯前驅節點。

     DFS使用棧(stack) 這一種資料結構來儲存未訪問的節點，節點按照深度優先的次序被訪問並依次被壓入棧中，並以相反的次序出棧進行新的檢測。
     
     
* BFS與DFS比較

   **BFS**
   * 時間複雜度：O(V+E)（分別遍歷所有節點和各節點的所有鄰居）
   * 空間複雜度：O(V)（Queue中最多可能存放所有節點） 
   
   **DFS**
   * 時間複雜度：O(V+E)
   * 空間複雜度：O(logV)
   
   dfs使用遞迴函式程式可以簡潔地進行書寫，並且狀態管理也很簡單，所以大多數情況還是用dfs來實現相關問題。反之，在求最短路問題時，dfs需要反覆經過同樣的狀    態，所以此時使用bfs為好。

   bfs會把狀態逐個加入佇列，因此通常需要與狀態數成正比的記憶體空間。反之，dfs是與遞迴深度成正比的。一般與狀態數相比，遞迴深度並不會太大，所以dfs更加省    記憶體。
   
  **BFS 的重點在於佇列，而 DFS 的重點在於遞迴。這是它們的本質區別**
  
  
# 學習歷程




```python
 def __init__(self): 
    self.graph = defaultdict(list) 
 
 def addEdge(self,u,v): 
    self.graph[u].append(v)
```

參考完網路上作品開始上工
這兩段是不用添加任何東西的，在設定初始init跟addedge


```python
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
                    plus.remove(i)
            for i in plus:
                if i in final:
                    plus.remove(i)
            queue = queue+plus
        return final
```

先設定一個final及一個bfs重要因子queue序列空間，原本忘記pop這個用法，上網搜尋了一下重拾記憶，照著流程圖真的很快擁有邏輯，再一步一步換成程式碼


```python
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
                    plus.remove(i)
            for i in plus:
                if i in final:
                    plus.remove(i)
            stack = stack+plus
        return final
```

這段跟bfs大同小異，畢竟這兩樣幾乎同個概念，只差在queue變stack跟pop的順序，而原因在流程圖即比較那邊有較詳盡的說明，在這就先不做贅述。
主要這次程式碼能完成，要感謝蔡老師上課教學的改變，使我流程圖及邏輯更能掌握，不再那麼抽象，讓我懂更快速。
  
  
  
  



**參考網站**

https://www.itread01.com/content/1541297601.html

https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/102866/

