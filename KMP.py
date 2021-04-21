# search for occurences of a pattern string within a main text
# the main idea is to find the next list to decrease the times of comparing
# the next list is produced by PMT (Partial Match Table)
# PMT is constructed by the max length of the same part between prefix and ending of the pattern string
# A good explanation of KMP: https://www.zhihu.com/question/21923021


class KMP():
    def __init__(self, p, m=""):
        self.pattern = p
        self.main = m
        self.next = self._getNext()


    def _getNext(self):
        next = [-1 for i in range(len(self.pattern))]
        j = -1
        i = 0

        while i < len(self.pattern):
            if(j == -1 or self.pattern[i] == self.pattern[j]):
                i += 1
                j += 1
                if i < len(self.pattern):
                    next[i] = j
            else:
                j = next[j]
        return next


    def compare(self, m=""):
        if m: self.main = m

        i = 0
        j = 0
        while i < len(self.main) and j < len(self.pattern):
            if j == -1 or self.main[i] == self.pattern[j]:
                i += 1
                j += 1
            else:
                j = self.next[j]
        if j == len(self.pattern):
            return i - j if i >= j else -1
        return -1


if __name__ == '__main__':
    test_p = "abcdab"
    test_m = "sadefasabcdabsadaw"
    KMP_instance = KMP(test_p, test_m)
    print(KMP_instance.compare())
    print(KMP_instance.compare("sadaweabcdbsaea"))
