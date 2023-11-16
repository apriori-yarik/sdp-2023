## Днес ще разгледаме

- Дървета
- Двоични дървета
- Двоични дървета за търсене (BST)
- Алгоритми за обхождане на дървета

## Tree (Дърво)

- Нелинейна структура от данни, която се състои от възли, подобно на свързания списък. Един възел може да има няколко наследника, но само 1 предшественик.
- Дървото се характеризира с липсата на цикли - *Ацикличен свързан граф*.
- Възли без наследници се наричат *листа*.
- Коренът на дървото е възелът без нито един предшественик.

## Binary Tree (Двоично дърво)

- Дърво, чиито възли имат най-много двама наследника. Най-често се обозначават ляв и десен (left, right).

## Binary Search Tree (Двоично дърво за търсене)

- Дефинира се рекурсивно по следния принцип:
1. Всяко листо е двоично дърво за търсене.
2. Всяко поддърво започващо от даден възел е двоично дърво за търсене, ако:
    - Най-големият елемент в лявото му поддърво е по-малък от стойността в дадения възел.
    - Най-малкият елемент в дясното му поддърво е по-голям от стойността в дадения възел.
    - И лявото поддърво, и дясното поддърво са двоични дървета за търсене.

## Алгоритми за обхождане

### Depth-first search (Обхождане в дълбочина)

- Inorder traversal - извежда във възходящ ред стойностите на дървото
  - Ляво - Корен - Дясно 
- Preorder traversal 
  - Корен - Ляво - Дясно
- Postorder traversal 
  - Ляво - Дясно - Корен
  
### Breadth-first search (Обхождане в широчина)

- Level order traversal
    - корен - дълбочина 1 - дълбочина 2 - ...

## Сложност по време на основните операции:

| Операция | Worst case | Average case |
| --- | --- |  --- |
| търсене | *O(N)* | *Θ(logN)* |
| добавяне | *O(N)* | *Θ(logN)* |
| триене | *O(N)* | *Θ(logN)* |


## Имплементации в Python

Няма вградено двоично дърво за търсене в Python.
Ако искаме да ползваме такова, ще трябва да си го напишем сами.