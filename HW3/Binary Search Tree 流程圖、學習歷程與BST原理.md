  # BST-insert
## 流程圖
<img src='https://github.com/eter0000/learningnotes/blob/master/images/insert.png'>
  
  * insert的概念其實很簡單，它會逐一比較，之後再到他應該待的地方。所以在寫insert的時候，一開始也很順，直到我遇到一個問題是**我丟進去的是值而不是root的位置**，後來發現我必須要用treenode的方式賦予值才會符合格式的
 
<img src='https://github.com/eter0000/learningnotes/blob/master/images/insert2.jpg'>
 
  * 所以我就先修改了一下

<img src='https://github.com/eter0000/learningnotes/blob/master/images/Insert1.jpg' weight=400 height=100>
  
  * 結果跑出來也沒問題，那太好了，於是我又再做微調，不管是None的判斷或是什麼時候要return都有卡了一陣子，過了大概五小時，最後終於完成了
  
  <img src='https://github.com/eter0000/learningnotes/blob/master/images/insert3.jpg'>
  
  * 原本以為四個Def已經完成一個了，距離結束應該不遠了，殊不知delete才是地獄的開始……
  
  # BST-search
## 流程圖
<img src='https://github.com/eter0000/learningnotes/blob/master/images/search.png'>

  * Search應該是我覺得最簡單的一個Def，因為其實寫法跟insert很像，大概花半小時就完成了，雖然沒有到很快，但跟其他幾個Def相比，search算是很快的了，以下是程式碼：
  <img src='https://github.com/eter0000/learningnotes/blob/master/images/search1.jpg'>
  
  * 需要用到遞迴的關係，不過前幾次作業有做過類似的，所以沒有卡太久
  
  # BST-delete
  ## 流程圖
  <img src='https://github.com/eter0000/learningnotes/blob/master/images/delete.png'>
  
  * 在開始打程式碼之前我有先在腦海中想像，如果有這個delete功能，它應該是要長怎樣？但想著想著，還是覺得老老實實的上網看介紹吧～於是我看了幾個網站的介紹，大概了解七成了，剩下那三成可能要在變做邊理解了，抱持著我有信心能在一天內寫完的心情，好，那我就開始寫了，第一次寫出來長這樣
  
  <img src='https://github.com/eter0000/learningnotes/blob/master/images/delete3.jpg'>
  
  * 一樣透過遞迴來比較大小，再來找到要刪除的值的位置，不過這樣少設一個條件就是當`root.val=target`時的狀況，所以我後來再把它加上去
  * delete會遇到的狀況就三種：
    * 沒有child
    * 只有一個child
    * 有兩個child
  * 當我遇到第一個狀況就比較單純，只需要把原本的root刪掉就好，不用再補其他值，而後兩種情況就得遇到「誰來當root」的問題，一般來說有兩種方法：
    * 在左邊的sub-tree找最大值
    * 在右邊的sub-tree找最小值
  * 因為只有找這兩者當中的值來當root會變動最小，而我選擇找右邊的sub-tree的最小值，所以我另外建立了minnode這個function
  
  <img src='https://github.com/eter0000/learningnotes/blob/master/images/minnode.jpg'>
  
  * 接下來我就繼續打我的delete，大概是長這樣
  
  <img src='https://github.com/eter0000/learningnotes/blob/master/images/delete4.jpg'>
  
  
  * 後來我發現我這個delete漏洞太多，包括沒辦法一次刪除重複的數、還有一些特殊情況沒考慮到等等，導致我的code時而對時而錯，心情像在洗三溫暖。
  最後我加上了while迴圈變解決了這個問題
  
  # BST-modify
  ## 流程圖
  
  <img src='https://github.com/eter0000/learningnotes/blob/master/images/modify.png'>
  
  
  # 參考資料
   * https://www.youtube.com/watch?v=YlgPi75hIBc
