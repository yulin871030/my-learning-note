# Stack&Queue

## Stack 必須有的功能
* **Push(Data)**: 把資料放到最上面(最新)。
* **Pop**: 把資料從最上面(最新)移除。
* **Top**: 回傳最上面(最新)的資料。
* **IsEmpty**: 確認stack 裡面是否有資料。
* **getSize**: 回傳stack 裡的資料個數。

## Stack的應用：
* Stack最主要的功能是「記得先前的資訊」，所以時常用來處理需要「回復到先前的狀態」的問題，也稱為Back-Tracking問題，例如：
　 * 編輯器(如word、sublime等等)中的undo。
   * 網頁瀏覽器的「回到前一頁」功能。
   * 編譯器(compiler)中的Parsing。
   * 任何遞迴(recursion)形式的演算法，都可以用Stack改寫，例如Depth-First Search(DFS，深度優先搜尋)。


## Queue 必須有的功能
* **Push(Data)**: 把資料放到 Queue 的後面，並更新成新的 back。
* **Pop(dequeue)**: 把 front 所指向的資料從 Queue 中移除，並更新front。
* **getFront**: 回傳 front 所指向的資資料。
* **getBack**: 回傳 Back 所指向的資資料。
* **IsEmpty**: 確認 Queue 裡是否有資料。
* **getSize**: 確認 Queue 裡的資料個數。


## Queue的應用
- 因為Queue的「First-In-First-Out」特徵，常用於先到先執行、需要排程(scheduling)的應用：
  - 演算法：Breadth-First Search(廣度優先搜尋)與Tree的Level-Order Traversal會用到Queue。
  - 作業系統：被多個程式共享的資源(例如CPU、印表機、網站伺服器)，一次只能執行一個需求(例如request、interrupt)，因此需要有個Queue來安排多個程式的執行順序(例如device queue、job queue)，請參考：
  - Tutorialspoint：Operating System - Process Scheduling。
  - Stack Overflow：What are practical applications of Queues?。
  - Stack Exchange：Which queue does the long-term scheduler maintain?
