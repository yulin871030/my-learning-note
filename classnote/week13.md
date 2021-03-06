# Depth-First Search

## 簡介
- DFS (Depth-First-Search)——深度優先搜尋，是從根節點開始， 逐個訪問每一條路徑， 對於具有多子節點的節點而言，先搜尋到某一條子路的最深處，再逐個回 溯前驅節點。DFS使用棧(stack) 這一種資料結構來儲存未訪問的節點，節點按照深度優先的次序被訪問並依次被壓入棧中，並以相反的次序出棧進行新的檢測。

![](https://i.imgur.com/Z6SIeJv.png)

## BFS與DFS比較

- BFS
  - 時間複雜度：O(V+E)（分別遍歷所有節點和各節點的所有鄰居）
  - 空間複雜度：O(V)（Queue中最多可能存放所有節點）
- DFS
  - 時間複雜度：O(V+E)
  - 空間複雜度：O(logV)
- dfs使用遞迴函式程式可以簡潔地進行書寫，並且狀態管理也很簡單，所以大多數情況還是用dfs來實現相關問題。反之，在求最短路問題時，dfs需要反覆經過同樣的狀 態，所以此時使用bfs為好。
- bfs會把狀態逐個加入佇列，因此通常需要與狀態數成正比的記憶體空間。反之，dfs是與遞迴深度成正比的。一般與狀態數相比，遞迴深度並不會太大，所以dfs更加省 記憶體。
### BFS 的重點在於佇列，而 DFS 的重點在於遞迴。這是它們的本質區別

## [程式碼](https://github.com/yulin871030/my-learning-note/blob/master/HW5/BFS_06170131.py)

## 參考資料
- https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html
- https://en.wikipedia.org/wiki/Depth-first_search
- https://www.youtube.com/watch?v=pcKY4hjDrxk
