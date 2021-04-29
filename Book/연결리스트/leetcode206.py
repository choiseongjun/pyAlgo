def solution(arr):
    node,prev = head,None

    while node:
        next,node.next = node.next,prev
        prev,node = node,next

    return prev

head = [1, 2, 3, 4, 5]
solution(head)

