# Time:  O(n * logk) ~ O(n * k)
# Space: O(n + k)

# Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all 
# prime factors are in the given prime list primes of size k.
# For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
# is the sequence of the first 12 super ugly numbers given 
# primes = [2, 7, 13, 19] of size 4.
#
# Note:
# (1) 1 is a super ugly number for any given primes.
# (2) The given numbers in primes are in ascending order.
# (3) 0 < k <= 100, 0 < n <= 106, 0 < primes[i] < 1000.

# Heap solution. (620ms)
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        heap, uglies, idx, ugly_by_last_prime = [], [0] * n, [0] * len(primes), [0] * n
        uglies[0] = 1

        for k, p in enumerate(primes):
            heapq.heappush(heap, (p, k))

        for i in xrange(1, n):
            uglies[i], k = heapq.heappop(heap)
            ugly_by_last_prime[i] = k
            idx[k] += 1
            while ugly_by_last_prime[idx[k]] > k:
                idx[k] += 1
            heapq.heappush(heap, (primes[k] * uglies[idx[k]], k))

        return uglies[-1]

# Time:  O(n * k)
# Space: O(n + k)
# Hash solution. (932ms)
class Solution2(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies, idx, heap, ugly_set = [0] * n, [0] * len(primes), [], set([1])
        uglies[0] = 1

        for k, p in enumerate(primes):
            heapq.heappush(heap, (p, k))
            ugly_set.add(p)

        for i in xrange(1, n):
            uglies[i], k = heapq.heappop(heap)
            while (primes[k] * uglies[idx[k]]) in ugly_set:
                idx[k] += 1
            heapq.heappush(heap, (primes[k] * uglies[idx[k]], k))
            ugly_set.add(primes[k] * uglies[idx[k]])

        return uglies[-1]

# Time:  O(n * logk) ~ O(n * klogk)
# Space: O(n + k)
class Solution3(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies, idx, heap = [1], [0] * len(primes), []
        for k, p in enumerate(primes):
            heapq.heappush(heap, (p, k))

        for i in xrange(1, n):
            min_val, k = heap[0]
            uglies += [min_val]

            while heap[0][0] == min_val:  # worst time: O(klogk)
                min_val, k = heapq.heappop(heap)
                idx[k] += 1
                heapq.heappush(heap, (primes[k] * uglies[idx[k]], k))

        return uglies[-1]

# Time:  O(n * k)
# Space: O(n + k)
# TLE due to the last test case, but it passess and performs the best in C++.
class Solution4(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [0] * n
        uglies[0] = 1
        ugly_by_prime = list(primes)
        idx = [0] * len(primes)

        for i in xrange(1, n):
            uglies[i] = min(ugly_by_prime)
            for k in xrange(len(primes)):
                if uglies[i] == ugly_by_prime[k]:
                    idx[k] += 1
                    ugly_by_prime[k] = primes[k] * uglies[idx[k]]
    
        return uglies[-1]

# Time:  O(n * logk) ~ O(n * klogk)
# Space: O(k^2)
# TLE due to the last test case, but it passess and performs well in C++.
class Solution5(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly_number = 0

        heap = []
        heapq.heappush(heap, 1)
        for p in primes:
            heapq.heappush(heap, p)
        for _ in xrange(n):
            ugly_number = heapq.heappop(heap)
            for i in xrange(len(primes)):
                if ugly_number % primes[i] == 0:
                    for j in xrange(i + 1):
                        heapq.heappush(heap, ugly_number * primes[j])
                    break

        return ugly_number
