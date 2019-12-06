# Hash Table
## 流程圖
![](/images/hash_table.PNG)
## 學習歷程
- 剛開始要下手做的時候，只知道這個演算法是，給一些key，然後經過進位的轉換後再加密，最後做出表，那肯定最重要的就是轉換進位和加密的部分，所以我想了一下加密的過程中會經過哪些程序，並依照流程來下手。所以我第一個做的事contains，經過老師上課後，得知有MD5這個東西，所以馬上就先把輸入的key轉成可以計算的值找出餘數讓函數可以分組，這樣可以依照組別快速找出自己的目標，過程中沒有什麼卡住的地方，因為上次的經驗，這次沒有再搞錯不同類型的東西不能相比和計算，所以一下就過去了。

- 接下來做的是add，就是把在contains沒有找到的值加進去他該待在的表裡就行了，但在如何確定整個list是不是空的的部分卡了一陣子。

- 最後是remove，這兩次作業最麻煩的部分都是刪除的這個動作，因為同一組間假如有值被移除，next值要補上，所以條件要設更多，這邊我一直卡在不知道該如何用後面的值補上前面被移除的值，所以後來看了同學的程式碼才了解該如何設立while迴圈，最後花了好久才完成這次的作業。

## Hash Table與Hash function 原理
### Hash Table(雜湊表、哈希表）
#### 1、儲存實際資料的，是Entry物件。
#### 2、主要方法為，put、get、remove等。
#### 3、根據Key直接查詢資料結構內的內存位置。
#### 4、透過函數計算鍵值，將所查詢的數據放置到表中的位置來查詢記錄。
#### 5、存放記錄的數組稱做Hash Table，加速了尋找的速度，簡單說就是將資料分類，方便查詢。
### Hash function(雜湊函數、雜湊演算法）
#### 1、壓縮資料，將資料變小，固定資料的格式。
#### 2、將資料打亂混合，重新建立雜湊值。
#### 3、雜湊值通常用一個短的字母和數字組成的字串來表示。
#### 4、雜湊值當作陣列的索引，資料儲存在這個索引中。
#### 5、性質：運算速度快、不可逆性。
## 參考資料
#### https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm
#### http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
#### https://zh.wikipedia.org/wiki/散列函數
#### https://github.com/wellslu/DSA
#### https://stackoverflow.com/questions/10039788/what-does-distribution-of-the-hash-function-mean

