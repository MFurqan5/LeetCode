from bisect import bisect_right

class Solution(object):
    def maximumWeight(self, intervals):
        n = len(intervals)
        arr = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)])
        starts = [x[0] for x in arr]

        next_idx = [0] * n
        for i in range(n):
            next_idx[i] = bisect_right(starts, arr[i][1])

        memo = {}

        def dp(i, k):
            if i >= n or k == 0:
                return (0, ())
            key = (i, k)
            if key in memo:
                return memo[key]

            best = dp(i + 1, k)
            w, ids = dp(next_idx[i], k - 1)
            taken_weight = arr[i][2] + w
            taken_ids = tuple(sorted(ids + (arr[i][3],)))

            if taken_weight > best[0]:
                best = (taken_weight, taken_ids)
            elif taken_weight == best[0] and taken_ids < best[1]:
                best = (taken_weight, taken_ids)

            memo[key] = best
            return best

        return list(dp(0, 4)[1])