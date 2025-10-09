# Suffix Automaton (SAM) - Python implementation
# Features:
# 1) build SAM for a string s
# 2) count number of different substrings
# 3) compute occurrences (endpos counts) for each state
# 4) find longest substring that appears at least k times
# 5) longest common substring of two strings (using SAM of first)

from collections import defaultdict, deque

class SuffixAutomaton:
    def __init__(self):
        # each state: length, link, next (dict)
        self.len = [0]
        self.link = [-1]
        self.next = [defaultdict(lambda: -1)]
        self.size = 1
        self.last = 0

    def _new_state(self, length):
        self.len.append(length)
        self.link.append(-1)
        self.next.append(defaultdict(lambda: -1))
        self.size += 1
        return self.size - 1

    def extend(self, c):
        p = self.last
        cur = self._new_state(self.len[p] + 1)
        while p != -1 and self.next[p][c] == -1:
            self.next[p][c] = cur
            p = self.link[p]
        if p == -1:
            self.link[cur] = 0
        else:
            q = self.next[p][c]
            if self.len[p] + 1 == self.len[q]:
                self.link[cur] = q
            else:
                clone = self._new_state(self.len[p] + 1)
                # copy transitions
                self.next[clone] = self.next[q].copy()
                self.link[clone] = self.link[q]
                while p != -1 and self.next[p][c] == q:
                    self.next[p][c] = clone
                    p = self.link[p]
                self.link[q] = self.link[cur] = clone
        self.last = cur

    def build(self, s: str):
        for ch in s:
            self.extend(ch)

    def count_distinct_substrings(self):
        # number of distinct substrings = sum(len[v] - len[link[v]]) over all states v
        total = 0
        for v in range(1, self.size):
            total += self.len[v] - self.len[self.link[v]]
        return total

    def occurrences(self, s: str):
        """
        Compute number of endpos occurrences for each state for the string s
        RETURNS: occ[state] = number of end positions in original string that correspond to that state
        """
        # Initialize counts with 0, then for each position follow transitions to increment terminal state's count
        occ = [0] * self.size
        p = 0
        l = 0
        # For counting occurrences of substrings *of the original built string*, standard approach:
        # mark each position's last state by walking while building; alternate method: when building, increment occ[last] for each character.
        # EASIER: we will recompute using 'last positions' recorded during building.
        # To support that, let's rebuild while tracking last-state per position.
        # (If SAM built using build(s), we can re-scan s to get the corresponding states)
        p = 0
        for ch in s:
            p = self.next[p][ch]
            occ[p] += 1

        # propagate counts in order of decreasing len (topo by len)
        order = list(range(self.size))
        order.sort(key=lambda x: self.len[x], reverse=True)
        for v in order:
            if self.link[v] != -1:
                occ[self.link[v]] += occ[v]
        return occ

    def longest_substring_at_least_k(self, k, s: str):
        """
        Returns (length, substring) of the longest substring that appears at least k times in s.
        If multiple substrings tie, returns one of them.
        """
        occ = self.occurrences(s)
        best_len = 0
        best_state = 0
        for v in range(self.size):
            if occ[v] >= k:
                if self.len[v] > best_len:
                    best_len = self.len[v]
                    best_state = v

        if best_len == 0:
            return 0, ""

        # to extract a substring of length best_len from that state, we can walk back to collect characters.
        # But simpler: scan s and maintain current automaton match to find an occurrence of length best_len.
        p = 0
        cur_len = 0
        for i, ch in enumerate(s):
            while p != -1 and self.next[p][ch] == -1:
                p = self.link[p]
                if p != -1:
                    cur_len = self.len[p]
                else:
                    cur_len = 0
            if p == -1:
                p = 0
                cur_len = 0
            else:
                p = self.next[p][ch]
                cur_len += 1
            if cur_len >= best_len:
                # substring ends at i with length best_len
                return best_len, s[i - best_len + 1 : i + 1]
        return best_len, ""

    def longest_common_substring(self, t: str):
        """
        Given string t, return (length, substring) that is longest common between
        the string for which this SAM was built (call it s) and t.
        """
        v = 0
        l = 0
        best = 0
        best_pos = 0
        for i, ch in enumerate(t):
            if self.next[v].get(ch, -1) != -1:
                v = self.next[v][ch]
                l += 1
            else:
                while v != -1 and self.next[v].get(ch, -1) == -1:
                    v = self.link[v]
                if v == -1:
                    v = 0
                    l = 0
                else:
                    l = self.len[v] + 1
                    v = self.next[v][ch]
            if l > best:
                best = l
                best_pos = i
        return best, t[best_pos - best + 1 : best_pos + 1]

# ----------------------
# Example usage
# ----------------------
if __name__ == "__main__":
    s = "ababaabab"
    sam = SuffixAutomaton()
    sam.build(s)

    print("Distinct substrings:", sam.count_distinct_substrings())

    occ = sam.occurrences(s)
    # show top states by occurrences (state index, len, occ)
    top = sorted([(i, sam.len[i], occ[i]) for i in range(len(occ))], key=lambda x: (-x[2], -x[1]))
    print("Top states by occurrence (state, len, occ):", top[:6])

    # longest substring appearing at least k times
    for k in [2,3,4]:
        length, substr = sam.longest_substring_at_least_k(k, s)
        print(f"Longest substring appearing at least {k} times: length={length}, substr='{substr}'")

    # longest common substring example
    t = "babaac"
    length, substr = sam.longest_common_substring(t)
    print("Longest common substring with", t, "->", length, substr)
