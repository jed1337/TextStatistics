import urllib.request

from text_statistics.length import Length
from text_statistics.length_without_spaces import LengthWithoutSpaces
from text_statistics.lines import Lines
from text_statistics.word_count import WordCount
from text_statistics.unique_word_count import UniqueWordCount
from text_statistics.sentence_count import SentenceCount
from text_statistics.most_frquent import MostFrequent
from text_statistics.unique_word_percentage import UniqueWordPercentage

text_statistics = [Length, LengthWithoutSpaces, Lines, WordCount, UniqueWordCount, SentenceCount, MostFrequent, UniqueWordPercentage]

# http://www.gutenberg.org/files/20/20-0.txt
with urllib.request.urlopen("https://www.w3.org/TR/PNG/iso_8859-1.txt") as response:
    response = response.read().decode()

for text_statistic in text_statistics:
    text_statistic = text_statistic(response)
    print(text_statistic.description)
    print(text_statistic.result)
    print()
