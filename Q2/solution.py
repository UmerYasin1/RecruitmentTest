# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 18:25:32 2022

@author: Umer Yasin
"""
# Question 2

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def display(self):
		header = self.head
		while header != None:
			print(header.data)
			header = header.next

	def deleteNthNodeFromEnd(self, head, n):
		first = head
		secound = head

		for _ in range(n):
			first = first.next

		if not first:
			return head.next

		while first.next:
			first = first.next
			secound = secound.next

		secound.next = secound.next.next
		return head


if __name__ == '__main__':
	Object = LinkedList()
	Object.push(1)
	Object.push(2)
	Object.push(3)
	Object.push(4)
	Object.push(5)
	print('Linked List Before deletion:')
	Object.display()

	print('Delete nth Node from the End:')
	Object.deleteNthNodeFromEnd(Object.head, 2)

	print('Linked List after Deletion:')
	Object.display()

    
    # Video link 
    # https://drive.google.com/file/d/1M4noScDy6Rw_rY1g3CRJRaYWQy-TEJwX/view?usp=sharing
        
