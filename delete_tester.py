import sys
from dictionary.node import Node
from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
from dictionary.list_dictionary import ListDictionary
from dictionary.hashtable_dictionary import HashTableDictionary
from dictionary.ternarysearchtree_dictionary import TernarySearchTreeDictionary
import time

import random

def usage():
    """
    Print help/usage message.
    """
    print('python3 dictionary_file_based.py', '<approach> [data fileName] [command fileName] [output fileName]')
    print('<approach> = <list | hashtable | tst>')
    sys.exit(1)


if __name__ == '__main__':
    # Fetch the command line arguments
    args = sys.argv

    if len(args) != 3:
        print('Incorrect number of arguments.')
        usage()

    # initialise search agent
    agent: BaseDictionary = None
    if args[1] == 'list':
        agent = ListDictionary()
    elif args[1] == 'hashtable':
        agent = HashTableDictionary()
    elif args[1] == 'tst':
        agent = TernarySearchTreeDictionary()
    else:
        print('Incorrect argument value.')
        usage()

    # read from data file to populate the initial set of points
    data_filename = args[2]
    words_frequencies_from_file = []
    try:
        data_file = open(data_filename, 'r')
        for line in data_file:
            values = line.split()
            word = values[0]
            frequency = int(values[1])
            word_frequency = WordFrequency(word, frequency)  # each line contains a word and its frequency
            words_frequencies_from_file.append(word_frequency)
        data_file.close()
        agent.build_dictionary(words_frequencies_from_file)
        
        ##At this point dictionary of 50k has been built...
        
        
        word_count = len(agent.list)
        
        # select_element = random(0,len(agent.list)-1)
        
        start_timer = time.time_ns()
        
        
        
        for line in agent.list: # (word, frequency)
   
            agent.delete_word(line.word)
            
            
            if (word_count == 0 or
                word_count == 250 or 
                word_count == 500 or
                word_count == 1000 or 
                word_count == 2500 or
                word_count == 2750 or 
                word_count == 10000 or 
                word_count == 25000 or 
                word_count == 35000 or
                word_count == 40000 or
                word_count == 49500 or
                word_count == 50000):
                
                end_timer = time.time_ns()
                
                print("Time Elasped for Deleting word count", word_count, "is: ", end_timer - start_timer)
                
            word_count -= 1
        
        
    except FileNotFoundError as e:
        print("Data file doesn't exist.")
        usage()

  