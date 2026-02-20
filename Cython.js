# Typically in a .pyx file
def fast_sum(int n):
    cdef int i
    cdef double s = 0
    for i in range(n):
        s += i
    return s
