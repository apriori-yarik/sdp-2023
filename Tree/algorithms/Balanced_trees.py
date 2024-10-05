class Node:
    # В сравнение с обикновените двоични дървета - тук ще пазим и височината на всеки връх
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def insert(self, root, key):
        # Изпълняваме обичайното добавяне на елемент при двоичните дървета за търсене
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Обновяваме височината на родителя
        root.height = 1 + max(self.getHeight(root.left), 
                          self.getHeight(root.right))

        # Намираме коефициента на баланс
        balance = self.getBalance(root)

        # Случай Left-Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        
        # Случай: Right-Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
        
        # Случай: Left-Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        # Случай: Right-Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
    
    # x - елемент, спрямо който ротираме
    # Задължително връщаме корена
    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
 
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y
    
    # x - eлемент, спрямо който ротираме
    # Задължително връщаме корена
    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        return x
    
    # Самите изчисления върху височината са направени в insert метода, тъй като тя се извиква винаги при добавяне на връх към балансираното дърво
    def getHeight(self, root):
        if root is None:
            return 0
        
        return root.height
    
    # Балансът се изчислява като разлика между височините на лявото и дясното поддърво
    def getBalance(self, root):
        if not root:
            return 0
        
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    # Обикновен метод за обхождане на дървото
    def preOrder(self, root):
        if root is not None:
            print(root.val, end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)
            





