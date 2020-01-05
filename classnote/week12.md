# Breadth-First Search

## 簡介
- 廣度優先搜尋法，是一種圖形(graph)搜索演算法。從圖的某一節點(vertex, node)開始走訪，接著走訪此一節點所有相鄰且未拜訪過的節點，由走訪過的節點繼續進行先廣後深的搜尋。以樹(tree)來說即把同一深度(level)的節點走訪完，再繼續向下一個深度搜尋，直到找到目的節點或遍尋全部節點。

## 步驟

![](https://i.imgur.com/1xkkRtI.png)

## 複雜度分析
- 時間複雜度：O(V+E)（分別遍歷所有節點和各節點的所有鄰居）
- 空間複雜度：O(V)（Queue中最多可能存放所有節點）

## [程式碼](https://github.com/yulin871030/my-learning-note/blob/master/HW5/BFS_06170131.py)

## 參考資料
- https://www.javatpoint.com/breadth-first-search-algorithm
- https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html
- http://simonsays-tw.com/web/DFS-BFS/BreadthFirstSearch.html
