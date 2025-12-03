class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg = [0] * (4*self.n)
        self.lazy = [0] * (4*self.n)
        self.build(1, 0, self.n-1, arr)

    def build(self, idx, l, r, arr):
        if l == r:
            self.seg[idx] = arr[l]
            return
        mid = (l+r)//2
        self.build(idx*2, l, mid, arr)
        self.build(idx*2+1, mid+1, r, arr)
        self.seg[idx] = self.seg[idx*2] + self.seg[idx*2+1]

    def push(self, idx, l, r):
        if self.lazy[idx] != 0:
            self.seg[idx] += (r-l+1) * self.lazy[idx]
            if l != r:
                self.lazy[idx*2] += self.lazy[idx]
                self.lazy[idx*2+1] += self.lazy[idx]
            self.lazy[idx] = 0

    def update(self, idx, l, r, ql, qr, val):
        self.push(idx, l, r)
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            self.lazy[idx] += val
            self.push(idx, l, r)
            return
        mid = (l+r)//2
        self.update(idx*2, l, mid, ql, qr, val)
        self.update(idx*2+1, mid+1, r, ql, qr, val)
        self.seg[idx] = self.seg[idx*2] + self.seg[idx*2+1]

    def query(self, idx, l, r, ql, qr):
        self.push(idx, l, r)
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.seg[idx]
        mid = (l+r)//2
        return self.query(idx*2, l, mid, ql, qr) + \
               self.query(idx*2+1, mid+1, r, ql, qr)


# Usage
arr = [1,2,3,4,5]
st = SegmentTree(arr)
st.update(1,0,4,1,3,10)
print(st.query(1,0,4,1,3))
