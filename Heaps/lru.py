class ListNode:
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.prev = None
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, node):
		if self.head is None:
			self.head = node
		else:
			self.tail.next = node
			node.prev = self.tail
		self.tail = node		
	
	def delete(self, node):
		if node.next:
			node.next.prev = node.prev
		else:
			self.tail = node.prev
		if node.prev:
			node.prev.next = node.next
		else:
			self.head = node.next
		del node

class LRUCache:
	def __init__(self, capacity):
		self.capacity = capacity
		self.list = LinkedList()
		self.dict = {}

	def _insert(self, key, val):
		node = ListNode(key, val)
		self.list.insert(node)
		self.dict[key] = node

	def get(self, key):
		if key in self.dict:
			val = self.dict[key].val
			self.list.delete(self.dict[key])
			self._insert(key, val)
			return val
		return -1

	def set(self, key, val):
		if key in self.dict:
			self.list.delete(self.dict[key])
		elif len(self.dict) == self.capacity:
			del self.dict[self.list.head.key]
			self.list.delete(self.list.head)
		self._insert(key, val)

if __name__ == "__main__":	
    cache = LRUCache(3)
    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    print cache.get(1)
    cache.set(4, 4)
    print cache.get(2)

				
