# Shortest Path - Dijkstra
 
## Shortest Path
- 「最短路徑」是由起點到終點、權重最小的路徑，可能有許多條，也可能不存在。起點到終點不通、不存在路徑的時候，就沒有最短路徑。

## Dijkstra

- 其基本原理是：每次新擴展一個距離最短的點，更新與其相鄰的點的距離。當所有邊權都為正時，由於不會存在一個距離更短的沒擴展過的點，所以這個點的距離永遠不會再被改變，因而保證了演算法的正確性。不過根據這個原理，用Dijkstra求最短路的圖不能有負權邊，因為擴展到負權邊的時候會產生更短的距離，有可能就破壞了已經更新的點距離不會改變的性質。Dijkstra演算法的輸入包含了一個有權重的有向圖G，以及G中的一個來源頂點S。我們以V表示G中所有頂點的集合。每一個圖中的邊，都是兩個頂點所形成的有序元素對。(u,v)表示從頂點u到v有路徑相連。我們以E所有邊的集合，而邊的權重則由權重函數w: E → [0, ∞]定義。因此，w(u,v)就是從頂點u到頂點v的非負花費值(cost)。 邊的花費可以想像成兩個頂點之間的距離。任兩點間路徑的花費值，就是該路徑上所有邊的花費值總和。已知有V中有頂點s及t，Dijkstra演算法可以找到s到t的最低花費路徑(i.e. 最短路徑)。這個演算法也可以在一個圖中，找到從一個頂點s到任何其他頂點的最短路徑。  

![](/images/Dijkstra.png)

![](https://i.imgur.com/IhJfge5.png)

## [程式碼](https://github.com/yulin871030/my-learning-note/blob/master/HW6/Dijkstra_06170131.py)

## 參考資料
- https://www.youtube.com/watch?v=_lHSawdgXpI&feature=emb_rel_pause
- https://www.youtube.com/watch?v=5GT5hYzjNoo
- https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
