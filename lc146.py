class ListNode(object):
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class LRUCache(object):
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.key2prev = {}
        self.dummyHead = ListNode(-1, -1)
        self.tail = self.dummyHead

    def get(self, key):
        if key not in self.key2prev:
            return -1
        prev = self.key2prev[key]
        node = prev.next
        self.move_to_tail(prev)
        return node.value
    
    def put(self, key, value):
        if key in self.key2prev:
            prev = self.key2prev[key]
            self.move_to_tail(prev)
            self.key2prev[key].next.value = value
            return 
        
        self.push_back(ListNode(key, value))
        if len(self.key2prev) > self.capacity:
            self.pop_front()
        return
        
    def pop_front(self):
        head = self.dummyHead.next
        del self.key2prev[head.key]
        self.dummyHead.next = head.next
        self.key2prev[head.next.key] = self.dummyHead
        return
            
    def move_to_tail(self, prev):
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        self.key2prev[node.next.key] = prev
        self.push_back(node)
        
    def push_back(self, node):
        self.key2prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node 
        node.next = None
        return
