from email.errors import NonPrintableDefect
from platform import node
from typing import List
from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
from dictionary.node import Node


# ------------------------------------------------------------------------
# This class is required to be implemented. Ternary Search Tree implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


class TernarySearchTreeDictionary(BaseDictionary):

    def build_dictionary(self, words_frequencies: List[WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        firstWord = words_frequencies[0].word
        self.rootNode = Node(firstWord[0])
        for word in words_frequencies:
            self.add_word_frequency(word)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """

        return self.search_nodes(self.rootNode, word)
    
    def search_nodes(self, node: Node, word: str) -> int:
        if node is None or len(word) == 0:
            return 0
        
        head = word[0]
        tail = word[1:]
        if head < node.letter:
            return self.search_nodes(node.left, word)
        elif head > node.letter:
            return self.search_nodes(node.right, word)
        else:
            if len(tail) == 0 and node.end_word == True:
                return node.frequency
            return self.search_nodes(node.middle, tail)

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        # place holder for return
        self.add_node(word_frequency.word, self.rootNode, word_frequency.frequency)
        
        return True
        
        
    def add_node(self, word: str, node: Node, frequency: int):
        if len(word) == 0:
            return node
        
        head = word[0]
        tail = word[1:]
        if node is None:
            node = Node(head)
        
        if head < node.letter:
            node.left = self.add_node(word, node.left, frequency)
        elif head > node.letter:
            node.right = self.add_node(word, node.right, frequency)
        else:
            if len(tail) == 0:
                node.end_word = True
                node.frequency = frequency
            else:
                node.middle = self.add_node(tail, node.middle, frequency)
        
        return node


    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # TO BE IMPLEMENTED
        # place holder for return
        if self.delete_nodes(self.rootNode, word):
            return True
        else:
            return False
        
    
    def delete_nodes(self, node: Node, word: str):
        if node == None:
            return False
        
        head = word[0]
        tail = word[1:]
        
        if head < node.letter:
            node.left = self.delete_nodes(node.left, word)
        elif head > node.letter:
            node.right = self.delete_nodes(node.right, word)
        else:
            if len(tail) != 0:
                node.middle = self.delete_nodes(node.middle, tail)
            elif node.end_word == True:
                node.end_word = False
            else:
                return None
        
        return node

    def autocomplete(self, word: str) -> List[WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        # TO BE IMPLEMENTED
        # place holder for return
        
        self.autocompletes(self.rootNode, word)
        
        autoList = []
        for suffixes in self.autocompletes(self.rootNode, word):
            autoList.append(WordFrequency(word+suffixes, self.search(word+suffixes)))
        
        autoList.sort(key=lambda WordFrequency: WordFrequency.frequency, reverse=True)
        del autoList[3:len(autoList)]
        
        return autoList
    
    def autocompletes(self, node: Node, word: str):
        if node is None or len(word) == 0:
            return []
        
        head = word[0]
        tail = word[1:]
        
        if head < node.letter:
            return self.autocompletes(node.left, word)
        elif head > node.letter:
            return self.autocompletes(node.right, word)
        else:
            if len(tail) == 0:
                return self.suffixes(node.middle)
            return self.autocompletes(node.middle, tail)
    
    def suffixes(self, node: Node):
        if node is not None:
            if node.end_word:
                yield node.letter

            if node.left:
                for s in self.suffixes(node.left):
                    yield s
            if node.right:
                for s in self.suffixes(node.right):
                    yield s
            if node.middle:
                for s in self.suffixes(node.middle):
                    yield node.letter + s