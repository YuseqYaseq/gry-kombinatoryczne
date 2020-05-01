class Sequence:
    
    def __init__(self, values, k):
        self.values = values
        self.k = k

    def search(self, val, startIdx):
        left = startIdx
        right = len(self.values) - 1

        while left < right:
            middle = (left + right) / 2
            middle = int(middle)
            
            if self.values[middle] < val:
                left = middle + 1
            else:
                right = middle
        
        if self.values[left] == val:
            return left
        else:
            return -1
    
    def is_term(self):
        return self.find_arithmethic_sequence() is not None
    
    def find_arithmethic_sequence(self):
        n = len(self.values)

        if self.k > n:
            return None
        if self.k == 2:
            return (self.values[0], self.values[1] - self.values[0])
        
        for i in range(0, n - self.k + 1):
            for j in range(i + 1, n - self.k + 2):
                a1 = self.values[i]
                a2 = self.values[j]
                r = a2 - a1

                if self.can_reach_last_element_of_arithmetic_sequence(a1, r):
                    if self.contains_arithmetic_sequence(a2, r, j):
                        return (a1, r)
        return None
    
    def evaluate(self):
        n = len(self.values)

        if self.k > n:
            return 0
        if self.k == 2:
            return (n - 1) / 2 * n
        
        evaluation = 0

        for i in range(0, n - self.k + 1):
            for j in range(i + 1, n - self.k + 2):
                a1 = self.values[i]
                a2 = self.values[j]
                r = a2 - a1

                if self.can_reach_last_element_of_arithmetic_sequence(a1, r):
                    if self.contains_arithmetic_sequence(a2, r, j):
                        evaluation = evaluation + 1

        return evaluation
    
    def contains_arithmetic_sequence(self, a2, r, j):
        itr = 2
        an = a2
        lastIdx = j

        while itr < self.k:
            itr = itr + 1
            an = an + r
            lastIdx = self.search(an, lastIdx + 1)
            if lastIdx == -1:
                return False
        
        return True

    def can_reach_last_element_of_arithmetic_sequence(self, a1, r):
        ak = a1 + r * (self.k - 1)
        return ak <= self.values[len(self.values) - 1]