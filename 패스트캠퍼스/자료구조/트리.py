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
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
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
            elif value<self.current_node.value:
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
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if searched == False:
            return False
        ## 이후부터 Case 3개

        #case1 :삭제할 Node가 Leaf Node인 경우
        #self.current_node가 삭제할 Node,self.parent는 삭제 Node의 Parent Node인 상태
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node
        #case 2 : 삭제할 Node가 Child Node를 한개 가지고 있을 경우 근데 여기서 왼쪽 자식인지 오른쪽 자식인지 체크한다
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.node_left
            else:
                self.parent.right = self.current_node.left
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right
        #case 3: 삭제할 Node가 Child Node를 두 개 가지고있을 경우
        if self.current_node.left!=None and self.current_node.right!=None:
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right !=None:
                    self.change_node_parent.left=self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left=self.change_node
                self.change_node.right=self.current_node.right
                self.change_node.left = self.change_node.left






head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)
print(BST.search(8))