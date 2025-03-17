from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()  # 有序字典，维护插入顺序
        self.capacity = capacity  # 最大容量

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 访问后，移动到队尾
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 直接更新值，并移到队尾
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # 删除最久未使用的（队头）
