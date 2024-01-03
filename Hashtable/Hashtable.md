# Хештаблица

## Днес ще разгледаме

- Хештаблица (Hashtable)
- Справяне с колизии
- Структури в Python, които са имплементирани чрез хештаблица

## Hashtable (Хештаблица)

Основната идея на хештаблицата е да се възползва от бързия достъп до последователна памет както при списъка. За да е възможно това обаче, трябва да се използва метод за транслиране на обектите до цели положителни числа.

### Пример

Ако имаме низ *"abd"*, то той може лесно да бъде хеширан до цяло положително число. На всеки символ съпоставяме по едно число *("a" -> 1, "b" -> 2, "d" -> 4)* и събираме получените числа. Тогава нашият низ ще се хешира до стойността *7*.

Но ако низът ни е *"bad"*, то той ще има същата хеш стойност, което води до колизия, за които ще говорим по-нататък. 

Свеждането на конкретен обект до цяло число е работа на хеш функциите. 

### Хеш функции
Основните характеристиките на хеш функциите са:

- Да бъдат бързи за изчисление.
- Да създават минимален брой колизии. Справянето с колизиите увеличава средното време за изпълнение на заявка.
- Когато хешират един и същи обект, винаги да връщат една и съща стойност - да няма елемент на случайност или някакво състояние, което да повлияе на резултата от функцията (*stateless*).

## Справяне с колизии
Колизиите са неизбежна част от хеширането. Това са случаите, когато два **различни** обекта имат **една и съща** хеш стойност, след като биват прекарани през хеш функцията.
Съществуват няколко начина за справяне с колизии:

### Separate chaining
- Това е най-популярният метод за справяне с колизии.
- Когато обект представен като цяло число, принадлежи на заета клетка - същото цяло число, двата обекта се нареждат в свързан списък. 
- Проверката дали елемент принадлежи в списъка се извършва линейно.
- Използва се свързан списък, защото бързо се добавя елемент в края и премахва елемент от средата.

### Linear Probing
- Ако обект се хешира до дадено цяло число *x*, но то вече е заето, то тогава ще бъде попълнено първото число по-голямо от *x*, което е свободно. 
- Ако например обект се хешира до числото 5 и то е заето, то тогава се започва търсене в 6, 7 и т.н.
- Не толкова предпочитан метод, поради наличието на *clustering*.

### Double Hashing
- Използва 2 хеширащи функции, през които да прекарва даден обект.
- При заета клетка, отговаряща на стойността от първата хеш функция, се търси свободна клетка спрямо втората хеш функция.
- Не се наблюдава *clustering*, както при *Linear probing* метода.

## Имплементации в Python

Основните стурктури в Python, които са имплементирани чрез хештаблица, са *set* и *dictionary*.

### Set

Представлява множество, в което всеки елемент е хеширан. За амортизирано константно време - *О(1\*)*, може да извършва операциите:
1) Да провери дали съществува даден елемент в множество.
2) Да добави елемент в множеството.
3) Да премахне елемент в множеството.
4) Да вземе броя на елементите в множеството.

### Dictionary

Aналогична на *set*-a, но се състои от ключове, които сочат към стойности.
- Ключовете биват хеширани - отговарят на горепосочените характеристики на *set*-a.
- Не предоставя възможност за константа проверка дали дадена стойност съществува - единствено ключ.