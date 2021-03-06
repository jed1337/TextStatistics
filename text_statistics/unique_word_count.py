class UniqueWordCount:
    def __init__(self, response):
        self.unique_word_count = len(set(response.split()))

    @property
    def description(self):
        return "Unique word count"

    @property
    def result(self):
        return self.unique_word_count
