class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = list(Counter(tasks).values())       
        heapq.heapify_max(freq)

        time = 0
        wait = deque()

        while freq or wait:
            time += 1

            while wait and wait[0][1] <= time:
                cnt, _ = wait.popleft()
                heapq.heappush_max(freq, cnt)
            
            if freq:
                cnt = heapq.heappop_max(freq) - 1
                if cnt > 0:
                    wait.append((cnt, time + n + 1))
        
        return time