class Words:
    def __init__(self, response):
        self.word_count = len(response)

    @property
    def description(self):
        return "Word count"

    @property
    def result(self):
        return self.word_count
