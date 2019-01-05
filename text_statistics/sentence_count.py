class SentenceCount:
    def __init__(self, response):
        self.sentence_count = len(response.split("."))

    @property
    def description(self):
        return "Sentences"

    @property
    def result(self):
        return self.sentence_count
