class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Binary Search Tree - двоично дърво, при което:
# 1) лявото поддърво на всеки връх съдържа само върхове със стойност по-малка от тази на върха
# 2) дясното поддърво на всеки връх съдържа само върхове със стойност по-голяма от тази на върха
# 3) лявото и дясното поддърво на всеки връх са BST (отговарят на условия 1 и 2)
class BST:
    def __init__(self):
        self.root = None
    
    # Обхождане в дълбочина тип корен-ляво дърво-дясно дърво
    def preorder(self, root):
        if root is not None:
            print(root.val, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def search(self, value):
        return self.__search(self.root, value)
    
    # Идея зад search:
    # Алгоритъмът е рекурсивен, като на всяка стъпка се гледа коренът на текущото 
    # поддърво, който се сравнява със стойността, която търсим. Ако тя е по-малка, 
    # то пускаме рекурсия по лявото поддърво, а ако е по-голямо - по-дясното. Дъното на 
    # на рекурсията има два случая:
    # 1) стойността на корена съвпада с търсената стойност - значи тя е намерена
    # 2) стойността на корена е None - т.е. не сме намерили търсената стойност
    def __search(self, root, value):
        if root is None or root.val == value:
            return root
        
        if root.val < value:
            return self.__search(root.right, value)
        return self.__search(root.left, value)

    def insert(self, value):
        self.root = self.__insert(self.root, value)

    # Идея зад insert:
    # Подобно на search, движим се рекурсивно по дървото, като ако стойността, която искаме
    # да добавим, е по-малка от корена на текущото поддърво - викаме рекурсията върху 
    # лявото поддърво, иначе - върху дясното поддърво. Дъното на рекурсията представлява
    # моментът, в който коренът е None - това означава, че сме намерили мястото, където да
    # добавим новия връх. Създаваме го там и с това алгоритъмът приключва. Накрая връщаме
    # root, за да обновим корена на нашето BST
    def __insert(self, node, value):
        if node is None:
            node = Node(value)
        if value < node.val:
            node.left = self.__insert(node.left, value)
        elif value > node.val:
            node.right = self.__insert(node.right, value)
        
        return node
    
    def delete(self, value):
        self.root = self.__delete(self.root, value)
    
    # Идея зад delete:
    # Отново рекурсивен алгоритъм, който се състои от две части:
    # 1) Първо намираме върха, който искаме да изтрием (правим го аналогично на логиката 
    # зад search и insert)
    # 2) Осъществяваме триенето. Имаме три случая според това какви наследници има 
    # елементът, който трябва да изтрием:
    # 1-ви случай: нямаме ляв наследник - трием корена, а неговия десен наследник идва на
    # негово място
    # 2-ри случай: нямаме десен наследник - трием корена, а неговия ляв наследник идва на
    # негово място
    # 3-ти случай (внимание): коренът има два наследника - тогава трябва да намерим  
    # върха, който ще се обходи непосредствено след този корен при inorder обхождане. 
    # След като го намерим, копираме стойността на новооткрития връх, записваме я на
    # мястото на стойността на корена и трием новооткрития връх
    
    def __delete(self, root, value):
        if root is None:
            return root
        
        if root.val > value:
            root.left = self.__delete(root.left, value)
            return root
        elif root.val < value:
            root.right = self.__delete(root.right, value)
            return root
        
        if root.left is None:
            temp = root.right
            del root
            return temp
        elif root.right is None:
            temp = root.left
            del root
            return temp
        else:
            succParent = root
            succ = root.right
            while succ.left is not None:
                succParent = succ
                succ = succ.left

            if succParent != root:
                succParent.left = succ.right
            else:
                succParent.right = succ.right

            root.val = succ.val

            del succ
            return root

    
    
bst = BST()
bst.insert(27)
bst.insert(14)
bst.insert(35)
bst.insert(10)
bst.insert(19)
bst.insert(31)    
bst.insert(42)

bst.preorder(bst.root)

print()

check_35 = bst.search(35)
check_19 = bst.search(19)
check_11 = bst.search(11)

if check_35 is None:
    print("35 not found")
else:
    print("35 found")
if check_19 is None:
    print("19 not found")
else:
    print("19 found")
if check_11 is None:
    print("11 not found")
else:
    print("11 found")

bst.delete(19)

check_19 = bst.search(19)
if check_19 is None:
    print("19 was deleted")
bst.preorder(bst.root)

