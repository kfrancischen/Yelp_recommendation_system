"""The classic MapReduce job: count the frequency of words.
"""
import sys
sys.path.append("/Library/Python/2.7/site-packages")
sys.path.append("/usr/local/bin")

from mrjob.job import MRJob
import re


WORD_RE = re.compile(r"[\w']+")


class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    def combiner(self, word, counts):
        yield (word, sum(counts))

    def reducer(self, word, counts):
        yield (word, sum(counts))


if __name__ == '__main__':
     MRWordFreqCount.run()