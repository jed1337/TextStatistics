import urllib.request

from text_statistics.most_frquent import MostFrequent
from text_statistics.length import Length
from text_statistics.unique_words import UniqueWords
from text_statistics.words import Words
from text_statistics.unique_word_percentage import UniqueWordPercentage

text_statistics = [Length, MostFrequent, Words, UniqueWords, UniqueWordPercentage]

# with urllib.request.urlopen("http://www.gutenberg.org/files/20/20-0.txt") as response:
response = "Of Mans First Disobedience, and the Fruit Of that Forbidden Tree, whose mortal tast Brought Death into the World, and all our woe, With loss of _Eden_, till one greater Man Restore us, and regain the blissful Seat, Sing Heav’nly Muse, that on the secret top Of _Oreb_, or of _Sinai_, didst inspire That Shepherd, who first taught the chosen Seed, In the Beginning how the Heav’ns and Earth Rose out of _Chaos_: Or if _Sion_ Hill Delight thee more, and _Siloa’s_ Brook that flow’d Fast by the Oracle of God; I thence Invoke thy aid to my adventrous Song, That with no middle flight intends to soar Above th’ _Aonian_ Mount, while it pursues Things unattempted yet in Prose or Rhime. And chiefly Thou O Spirit, that dost prefer Before all Temples th’ upright heart and pure, Instruct me, for Thou know’st; Thou from the first Wast present, and with mighty wings outspread Dove-like satst brooding on the vast Abyss And mad’st it pregnant: What in me is dark Illumine, what is low raise and support; That to the highth of this great Argument I may assert th’ Eternal Providence, And justifie the wayes of God to men."\
    .split()
for text_statistic in text_statistics:
    text_statistic = text_statistic(response)
    print(text_statistic.description)
    print(text_statistic.result)
    print()

print("done")