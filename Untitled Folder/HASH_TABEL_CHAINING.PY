
class Node:
    def __init__(self, key ,value):
        self.key  = key 
        self.value = value
        self.next = None
        
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None]* capacity
        
    def _hash(self,key):
        return hash(key) % self.capacity
    
    
    def get(self,key):
        index = self._hash(key)
        if self.table[index] is None:
            return None
        temp = self.table[index]
        while temp:
            if temp.key == key:
                return temp.value
            temp = temp.next 
        return None
    
    def Insert(self,key,value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key,value)
            self.size += 1
        else:
            temp = self.table[index]
            while temp:
                if temp.key == key:
                    temp.value = value
                    return
                temp = temp.next
                    
            new_node = Node(key,value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            
            
    def delete(self,key):
        index = self._hash(key)
        if self.table[index] is None:
            return None
        else:
            temp = self.table[index]
            prev = None
            while temp:
                if temp.key == key:
                    if prev is None:
                        self.table[index] = temp.next
                    else:
                        prev.next = temp.next

                        self.size -= 1
                        return temp.value
                    prev = temp
                    temp = temp.next
        
    def display(self):
        for i in range(self.capacity):
            print(f'Index : {i} |',end='')
            temp = self.table[i]  
            while temp :              
                print(f'{temp.key} : {temp.value} -> ',end='')
                temp = temp.next
            print()
            
ht = HashTable(6)

ht.Insert('Zaheer',18)
ht.Insert('Jayesh',21)
ht.Insert('Hisham',20)
ht.Insert("Farzin",24)
ht.Insert("Shaloof",30)
ht.Insert('Week',30)

print(ht.get('Hisham'))
ht.delete('Jayesh')

ht.display()