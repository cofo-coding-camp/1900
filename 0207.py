def canFinish(self, n, pres):
    from collections import deque
    ind = [[] for _ in xrange(n)]  
    oud = [0] * n  
    for p in pres:
        oud[p[0]] += 1
        ind[p[1]].append(p[0])
    dq = deque()
    for i in xrange(n):
        if oud[i] == 0:
            dq.append(i)
    k = 0
    while dq:
        x = dq.popleft()
        k += 1
        for i in ind[x]:
            oud[i] -= 1
            if oud[i] == 0:
                dq.append(i)
    return k == n
