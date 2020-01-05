# 紅黑樹（Red Black Tree）
 
## 簡介
- 紅黑樹（Red Black Tree）是一棵二叉查詢樹，在每個節點增加一個屬性表示節點顏色，值為紅色（Red）或者黑色（Black）。紅黑樹也是“平衡”樹中的一種，通過對任何一條從根到葉子的路徑上各個節點的顏色來進行約束，確保沒有一條路徑會比其他路徑長出2倍，因而是“近似平衡”的。對平衡性的要求相較於AVL樹更寬鬆。

## 紅黑樹性質
- 一棵紅黑樹是滿足下面5條紅黑性質的二叉查詢樹：
  - 1. 每個節點要麼是紅色，要麼是黑色
  - 2. 根節點是黑色
  - 3. 每個葉節點（NIL或者空節點）是黑色
  - 4. 如果一個節點是紅色，則它的兩個子節點都是黑色
  - 5. 對於每個節點，從該節點到其所有後代葉節點的路徑上，均包含相同數目的黑色節點。
- 下圖就是一棵紅黑樹：

![](https://img-blog.csdn.net/20180914131136476?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTQxNjU2MjA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

- 插入一個新節點或者刪除一個節點時，可能會導致違反上述紅黑樹性質，所以需要通過改變節點顏色和旋轉來維護這些性質。
- 旋轉直觀效果如下：
 - 左旋：

![](https://img-blog.csdn.net/20170323102309404)

 - 右旋：
 
![](https://img-blog.csdn.net/20180914133836881?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTQxNjU2MjA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
