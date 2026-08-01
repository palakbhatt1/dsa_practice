from typing import List
from heapq import heappush, heappop

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:

        n = len(online)

        graph = [[] for _ in range(n)]

        left = float("inf")
        right = 0

        # Build graph (ignore offline nodes)
        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue

            graph[u].append((v, w))
            left = min(left, w)
            right = max(right, w)

        if left == float("inf"):
            return -1

        def check(mid):

            INF = float("inf")
            dist = [INF] * n
            dist[0] = 0

            pq = [(0, 0)]   # (distance, node)

            while pq:
                d, u = heappop(pq)

                if d > dist[u]:
                    continue

                if d > k:
                    return False

                if u == n - 1:
                    return True

                for v, w in graph[u]:

                    if w < mid:
                        continue

                    nd = d + w

                    if nd < dist[v]:
                        dist[v] = nd
                        heappush(pq, (nd, v))

            return False

        ans = -1

        while left <= right:

            mid = (left + right) // 2

            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans