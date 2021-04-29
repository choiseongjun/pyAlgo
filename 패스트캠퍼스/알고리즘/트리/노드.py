class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self,head):
        self.head = head

    def insert(self,value):
        self.current_node = self.head
        while True:
            if value <self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left != Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
    def search(self,value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False
    def delete(self,value):
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node=self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if searched==False:
            return False

        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node

if __name__ == '__main__':
    head = Node(1)
    BST = NodeMgmt(head)
    BST.insert(2)
    BST.insert(3)
    BST.insert(0)
    BST.insert(4)
    BST.insert(8)
    BST.search(8)
