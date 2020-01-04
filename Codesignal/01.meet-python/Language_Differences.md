Your friend, an experienced coder, has just started to learn Python. Since he is already proficient in Java and C++, he decided to write all his snippets in all three languages to test his Python code. Here's the very first function your friend wrote in Python and Java (the C++ version is the same as Java one):

```python
def division(x, y):
    return x // y
```

```java
in division(int x, int y) {
    return x / y;
}
```

You noticed that the functions aren't quite the same: they won't produce the same result for some valid values of x and y. Which ones?

- a. x = 15, y = -4 [check]
- b. x = -8, y = 2
- c. x = -8, y = 2
- d. x = 17, y = 13
- e. x = 5, y = 10

Java中的(/)結果是只取整數位;Python中的(//)則是會將取到的商的小數位無條件取小一位整數(也就是往負的方向進位)，所以15/-4=-3但15//-4=-4
