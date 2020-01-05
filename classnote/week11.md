# Hash table

## Hash table的概念
hash table 是一個資料結構，用來儲存一對 keys & value 。他使用 hash function 將 key 轉換成 array 對應的位置(index) 。而該位置就是用來儲存 value 的。
使用的 hash function 好壞是 hash table 關鍵。 在一般情況下，hash table 搜尋特定的物件的時間複雜度平均為 O(1).


![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/473px-Hash_table_3_1_1_0_1_0_0_SP.svg.png)

將特定字串轉換得到特定編號，並存到對應位置的資料結構，hash table 由下列三者組成：

- keys
  - 作為獨立的索引，通常為字串，也就是應用端輸入的東西。
- hash function
  - 通過某些算式或是方法，將 keys 轉換成能對應特定的 index 的。
  - 他的設計理念是一個key會有對應的且獨立的 bucket，但是目前大多數的設計都會有碰撞問題，也就是不同的 keys 經過轉換後會對應到一樣的 bucket。
- bucket
  - 他是一個 array ，有多個位置可以儲存資料，在裡面可以是空的可以存一筆資料，甚至也可以放其它資料結構，例如：linked-list

## 優點
- 以Division Method實現Hash Function的優點就是非常快，只要做一次餘數(一次除法)運算即可。

## 缺點
- key值是以hash tabale的形式儲存下來，這表格當然是有所限制的。而如果表格小一點，占用的空間可以少一點，但是相對的資料碰撞的機會就增加；反之，表格大一點，減少了資料碰撞，但是也造成空間的浪費。

## [程式碼](https://github.com/yulin871030/my-learning-note/blob/master/HW4/hash_table_06170131.py)

## 參考資料
- https://toyo0103.blogspot.com/2018/04/hash-table.html
- http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
- https://ithelp.ithome.com.tw/articles/10058078
