class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        if endWord not in wordList:
            return 0
        
        nei = defaultdict(list)
        for word in wordList:
            for j in range(n):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        q = deque([beginWord])
        depth = 0
        visit = set()
        find = False

        while q:
            depth += 1
            lenq = len(q)
            for _ in range(lenq):
                word = q.popleft()
                if word == endWord:
                    return depth
                for j in range(n):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for w in nei[pattern]:
                        if w not in visit:
                            visit.add(w)
                            q.append(w)
        return 0
