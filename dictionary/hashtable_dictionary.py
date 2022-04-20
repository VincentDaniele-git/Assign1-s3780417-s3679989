from typing import List
from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. HashTable-based dictionary implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class HashTableDictionary(BaseDictionary):

    def build_dictionary(self, words_frequencies: List[WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        self.dict = {}
        for word in words_frequencies:
            self.dict[word.word] = word.frequency
        
        

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        # place holder for return
        
        for dictWord in self.dict:
            if dictWord == word:
                return self.dict[dictWord]
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        # place holder for return
        for dictWord in self.dict:
            if dictWord == word_frequency.word:
                return False
            else:
                self.dict[word_frequency.word] = word_frequency.frequency
                return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # TO BE IMPLEMENTED
        # place holder for return
        
        for dictWord in self.dict:
            if dictWord == word:
                del self.dict[dictWord]
                return True
        return False

    def autocomplete(self, prefix_word: str) -> List[WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        # TO BE IMPLEMENTED
        # place holder for return
        
        autoList = []
        for word in self.dict:
            if word.startswith(prefix_word):
                autoList.append(WordFrequency(word, self.dict[word]))
        autoList.sort(key=lambda WordFrequency: WordFrequency.frequency, reverse=True)
        del autoList[3:len(autoList)]
        
        return autoList
