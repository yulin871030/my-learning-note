#   linked-list

 ## array: 
 
 - 陣列，連續性的，速度快，所以如果存取的空間沒有連續的位置便無法存取，但其實儲存空間並不是不足，所以便發明了linked-list。
 
 ## linked-list：
 
 - 鍵結串列，不是連續的，速度慢，可以找出儲存空間剩餘的空間來儲存，機靈地利用零碎空間。但若要查詢特定node（節點），因為不是連續性，需要從頭開始找起，搜尋的時間較高。
 
 ## blockchain（區塊鏈）：
 
 - 在linked-list裡面再包一個hash
 
 ## hash：
 
 - 做hash是為了不想讓人知道資料內容，所以故意把資料打亂，所以如果前一份資料更改，hash值便會改變，這也是為何blockchain無法被竄改。

 ## linked-list 優點：
 
  - 不需使用連續記憶體空間，不需事先指定串列大小。

  - 能夠容易的修改指標，插入或移除節點。

 ## linked-list 缺點：

  - 使用額外的記憶體空間紀錄節點指標。

  - 無法快速索引到某個節點，必須迭代搜索。

#     Hash Table（雜湊表）

## 優點：

- 資料量大時，仍然維持常數時間的高效能

- 若資料數量上限已知，就可避免重新配置記憶體，效能更佳

- 若資料形態已知，就可針對該資料形態找尋適合的雜湊函數最佳化

## 缺點：

- 資料量不夠大時，單一操作需要雜湊計算，開銷相對高

- 效能與雜湊函數息息相關，較差的函數容易雜湊碰撞，較佳函數計算成本較高

- 只能以某種偽隨機的順序迭代雜湊表

#   Hash Function  
## 定義

- 是一種輸入字串，然後輸出數字的函數。也就是「將字串對應至數字」。

- 密碼學的觀點：資料進行編碼，以求隱蔽。

- 例： “Apple” → Hash Function → 3

## 概念

- 1：始終將一個特定的名稱對應於相同的數字，每次輸入Apple，都會得到相同的數字(例如 3)。

- 2：將不同的字串對應至不同的索引值。例： Apple 對應至3，Milk 對應至 4

- 3：雜湊函數知道陣列的大小，而且只傳回有效的索引值。

> 透過雜湊函數與陣列的結合，可得到一個Hash Table資料結構。


  
### 優點

 - 非常快速，只要做一次餘數(一次除法)運算即可

### 缺點

- Table大小必須慎選
