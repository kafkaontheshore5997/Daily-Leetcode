class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.num2index = collections.defaultdict(set)
        self.counter = 0
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        found = False
        if val in self.num2index:
            found = True
        self.arr.append(val)
        index = len(self.arr) - 1
        
        self.num2index[val].add(index)
        self.counter += 1
        return not found
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.arr:
            return False
        self.counter -= 1
        last_num, last_index = self.arr[-1], len(self.arr) - 1
        if last_num == val:
            self.arr.pop()
            self.num2index[val].remove(last_index)
            return True
        del_index = self.num2index[val].pop()
        self.arr[del_index], self.arr[last_index] = self.arr[last_index], self.arr[del_index]
        self.arr.pop()
        self.num2index[last_num].remove(last_index)
        self.num2index[last_num].add(del_index)
        if not self.num2index[val]:
            del self.num2index[val]
        return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        rand = random.randint(0, self.counter - 1)
        return self.arr[rand] if self.arr else -1
