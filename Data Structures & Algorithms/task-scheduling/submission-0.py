from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks, n):
        # Count frequency of each task
        freq = Counter(tasks)

        # Max Heap (store negative frequencies)
        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)

        # Queue for cooldown tasks
        # (remaining_frequency, available_time)
        cooldown = deque()

        time = 0

        while maxHeap or cooldown:
            time += 1

            # Execute highest frequency task
            if maxHeap:
                count = heapq.heappop(maxHeap)
                count += 1          # One occurrence completed

                if count != 0:
                    cooldown.append((count, time + n))

            # Move tasks whose cooldown is finished
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(maxHeap, cooldown.popleft()[0])

        return time
        