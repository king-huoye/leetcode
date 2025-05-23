class WordsFrequency:

    def __init__(self, book: List[str]):
        self.count=Counter(book)

    def get(self, word: str) -> int:
        if word not in self.count:
            return 0
        return self.count[word]


# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)
