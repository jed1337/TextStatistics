class MostFrequent:
    def __init__(self, response, result_count = 10):
        self.response = response.split(" ")
        self.result_count = result_count

        self.word_count = self._get_populated_word_count()

    def _get_populated_word_count(self):
        word_count = dict()
        for word in self.response:
            word = word.lower()
            word_count[word] = word_count.get(word, 0) + 1

        del word_count[""]
        return word_count

    @property
    def description(self):
        return "The top {0} frequent words".format(self.result_count)

    @property
    def result(self):
        return sorted(((v, k) for k, v in self.word_count.items()), reverse=True)[0:self.result_count]