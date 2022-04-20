

import time
import sys
from tracemalloc import start
from typing import List
from dictionary.node import Node
from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
from dictionary.list_dictionary import ListDictionary
from dictionary.hashtable_dictionary import HashTableDictionary
from dictionary.ternarysearchtree_dictionary import TernarySearchTreeDictionary

if __name__ == '__main__':
    data_filename = 'sampleData.txt'
    words_frequencies_from_file = []
    agent = ListDictionary()
    
    data_file = open(data_filename, 'r')
    for line in data_file:
        while len(words_frequencies_from_file) < 50:
            values = line.split()
            word = values[0]
            frequency = int(values[1])
            word_frequency = WordFrequency(word, frequency)  # each line contains a word and its frequency
            words_frequencies_from_file.append(word_frequency)
    agent.build_dictionary(words_frequencies_from_file)
    
    print(len(words_frequencies_from_file))