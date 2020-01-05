# Heap Sort 

## What is Heap?
Heap(Binary Heap) 是以 tree(樹) 為基礎的資料結構, 他有以下特點:

* Shape Property: Heap 的資料結構永遠都是 完全二元樹  Complete Binary Tree, 也就是在每個 level ，由左至右都有 Node，但是如果是同層級的左至右少一個結點，就不是完全二元樹了。
* Heap Property: 所有節點再初始狀態下沒有大小排序. 但是當所有 parent nodes> 所有的 child nodes, 就會稱作 Max-Heap。反之當所有 parent nodes< 所有的 child nodes 稱為Min-Heap。

- 它是 linked 的進化版，一般在 linked-List 裡的 Node 裡面，只會包含 value 和 pointer。但是它把在 heap 裡面，它限制只能往一個方向


## 複雜度分析
* 時間複雜度 : O(n*log n)

* 空間複雜度 : O(1)

## 特性
- 不穩定
- 需要連續的空間
- 速度快，被廣泛運用
- 是一個 in-place 演算法




##  Heap Sort  step-by-step
### Initial Elements (初始元素)

<img src='https://i.imgur.com/eBDrKvL.png' height=200 weight=750>

### Step 0
> 將其轉換為 max heap

<img src='https://i.imgur.com/BOy1IvU.png' height=330 weight=720>

### Step 1

> 8 與 5 交換。>>  8 與 heap 切斷連結，此時 8 已經為排序過的 element。

<img src='https://i.imgur.com/Xy2r7Cu.png' height=330 weight=720>

### Step 2
> 建立 Max-heap >> 7 與 3 交換 >> 7 與 heap 切斷連結。

<img src='https://i.imgur.com/LlgrgNf.png' height=330 weight=720>

### Step 3
> 建立 Max heap  >> 5 與 1 交換 >> 5 與 heap 切斷連結。

<img src='https://i.imgur.com/ccgbPsl.png' height=330 weight=720>

### Step 4
> 建立 Max heap >> 4 與 3 交換 >> 4 與 heap 切斷連結。

<img src='https://i.imgur.com/gDYAi3D.png' height=330 weight=720>

### Step 5
> 建立 Max heap >> 3 與 1 交換 >> 3 與 heap 切斷連結。

<img src='https://i.imgur.com/N7IFaUW.png' height=330 weight=720>

### Result

![](https://i.imgur.com/sJeGPoz.png)
## 參考網站
* https://en.wikipedia.org/wiki/Heapsort
* https://www.geeksforgeeks.org/heap-sort/
* https://www.hackerearth.com/zh/practice/algorithms/sorting/heap-sort/tutorial/
* https://www.studytonight.com/data-structures/heap-sort
* https://www.youtube.com/watch?v=MtQL_ll5KhQ
