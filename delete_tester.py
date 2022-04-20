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
    print('python3 dictionary_file_based.py', '<approach> [output fileName]')
    print('<approach> = <list | hashtable | tst>')
    sys.exit(1)


if __name__ == '__main__':
    # Fetch the command line arguments
    args = sys.argv

    if len(args) != 4:
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
    output_filename = args[3]
    
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
        
        # Result of TST
    
        output_file = open(output_filename, 'w')
        
        output_file.write(f"Length of Hash\tNanoseconds\n")  
        
        start_timer = time.time_ns()
        
        print(len(agent.tst))
        
        # for word in list(agent.dict):
        #     agent.delete_word(word)
            
            # if (len(agent.dict) == 50000 or
            #     len(agent.dict) == 45000 or
            #     len(agent.dict) == 40000 or
            #     len(agent.dict) == 35000 or
            #     len(agent.dict) == 30000 or
            #     len(agent.dict) == 25000 or
            #     len(agent.dict) == 20000 or
            #     len(agent.dict) == 15000 or
            #     len(agent.dict) == 10000 or
            #     len(agent.dict) == 5000 or
            #     len(agent.dict) == 0):
        
            #     end_timer = time.time_ns()
            #     # print("Number of words remaining:", len(agent.list))
            #     print("Time Elasped for Deleting word count", len(agent.dict), "is:\t", end_timer - start_timer)
                
            #     output_file.write(f"{len(agent.dict)}\t{end_timer - start_timer}\n")
        
        
        
        # # Result of HashTable
    
        # output_file = open(output_filename, 'w')
        
        # output_file.write(f"Length of Hash\tNanoseconds\n")  
        
        # start_timer = time.time_ns()
        
        # print(len(agent.dict))
        
        # for word in list(agent.dict):
        #     agent.delete_word(word)
            
        #     if (len(agent.dict) == 50000 or
        #         len(agent.dict) == 45000 or
        #         len(agent.dict) == 40000 or
        #         len(agent.dict) == 35000 or
        #         len(agent.dict) == 30000 or
        #         len(agent.dict) == 25000 or
        #         len(agent.dict) == 20000 or
        #         len(agent.dict) == 15000 or
        #         len(agent.dict) == 10000 or
        #         len(agent.dict) == 5000 or
        #         len(agent.dict) == 0):
        
        #         end_timer = time.time_ns()
        #         # print("Number of words remaining:", len(agent.list))
        #         print("Time Elasped for Deleting word count", len(agent.dict), "is:\t", end_timer - start_timer)
                
        #         output_file.write(f"{len(agent.dict)}\t{end_timer - start_timer}\n")
        

        # # Obtaining result of List
        
        # word_count = len(agent.list)
        # start_timer = time.time_ns()
    
        # output_file = open(output_filename, 'w')
        
        # output_file.write(f"Length of List\tNanoseconds\n")
        
        # for line in list(agent.list):
        #     agent.delete_word(line.word)
        
        #     if (len(agent.list) == 50000 or
        #         len(agent.list) == 45000 or
        #         len(agent.list) == 40000 or
        #         len(agent.list) == 35000 or
        #         len(agent.list) == 30000 or
        #         len(agent.list) == 25000 or
        #         len(agent.list) == 20000 or
        #         len(agent.list) == 15000 or
        #         len(agent.list) == 10000 or
        #         len(agent.list) == 5000 or
        #         len(agent.list) == 0):
                
        #         end_timer = time.time_ns()
        #         # print("Number of words remaining:", len(agent.list))
        #         print("Time Elasped for Deleting word count", len(agent.list), "is:\t", end_timer - start_timer)
                
        #         output_file.write(f"{len(agent.list)}\t{end_timer - start_timer}\n")
                

                
        
        
    except FileNotFoundError as e:
        print("Data file doesn't exist.")
        usage()

  