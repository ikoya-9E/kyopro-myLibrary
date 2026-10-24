class SegTreeRMQ:
    def __init__(self, lst):
        self.gen = 0  # 単位元
        self.func = max

        self.n_ = len(lst)
        self.n = 1 << (self.n_ - 1).bit_length()
        self.tree = [self.gen] * (2 * self.n)

        for i in range(self.n_):
            self.tree[self.n + i] = lst[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    # x番目(0-indexed)のデータをaに変更する
    def update(self, x, a):
        x += self.n
        self.tree[x] = a
        while x > 1:
            x >>= 1
            self.tree[x] = self.func(self.tree[2 * x], self.tree[2 * x + 1])
    
    # [l, r) の区間クエリ (0-indexed)
    def query(self, l, r):
        res = self.gen
        l += self.n
        r += self.n
        while l < r:
            if l & 1:  # l が右側の子（奇数）なら
                res = self.func(res, self.tree[l])
                l += 1
            if r & 1:  # r が右側の子（奇数）なら（※開区間なので1引いた要素を見る）
                r -= 1
                res = self.func(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res

    def get(self,x):
        x+=self.n
        return  self.tree[x]