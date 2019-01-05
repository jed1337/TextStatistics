class UniqueWordPercentage:
    def __init__(self, response):
        word_count = len(response.split())
        unique_word_count = len(set(response.split()))
        self.unique_word_percentage = unique_word_count/word_count

    @property
    def description(self):
        return "Percentage of unique words"

    @property
    def result(self):
        return self.unique_word_percentage
