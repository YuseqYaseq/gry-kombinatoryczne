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
                ak = a1 + r * (self.k - 1)
                if ak > self.values[n - 1]:
                    break
                
                itr = 2
                an = a2
                lastIdx = j

                while itr < self.k:
                    itr = itr + 1
                    an = an + r
                    lastIdx = self.search(an, lastIdx)
                    if lastIdx == -1:
                        break
                
                if lastIdx != -1:
                    return (a1, r)
        return None
    