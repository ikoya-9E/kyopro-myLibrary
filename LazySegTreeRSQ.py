#ToDo 計算式の変更（4箇所）
class LazySegTreeRSQ:
    def __init__(self, lst):
        self.gen = 0  # 単位元

        self.n_ = len(lst)
        self.n = 1 << (self.n_ - 1).bit_length()
        self.tree = [self.gen] * (2 * self.n)
        self.data

        for i in range(self.n_):
            self.tree[self.n + i] = lst[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]  #ToDo1

    # x番目(0-indexed)のデータをaに変更する
    def update(self, x, a):
        x += self.n
        self.tree[x] = a
        while x > 1:
            x >>= 1
            self.tree[x] = self.tree[2 * x] + self.tree[2 * x + 1]  #ToDo2
    
    # [l, r) の区間クエリ (0-indexed)
    def query(self, l, r):
        res = self.gen
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = res + self.tree[l]    #ToDo3
                l += 1
            if r & 1:
                r -= 1
                res = res + self.tree[r]    #ToDo4
            l >>= 1
            r >>= 1
        return res