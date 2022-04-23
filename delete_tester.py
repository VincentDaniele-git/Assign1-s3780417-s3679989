import sys
from dictionary.node import Node
from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
from dictionary.list_dictionary import ListDictionary
from dictionary.hashtable_dictionary import HashTableDictionary
from dictionary.ternarysearchtree_dictionary import TernarySearchTreeDictionary
import time
import copy

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
        
        # # Result of TST
    
        # output_file = open(output_filename, 'w')
        
        # output_file.write(f"Length of Hash\tNanoseconds\n")  
        
        
        # deepcopy_words_frequencies = copy.deepcopy(words_frequencies_from_file)
        
        # random.shuffle(deepcopy_words_frequencies)
        
        # start_timer = time.time_ns()
        
        # # for word_freq in deepcopy_words_frequencies:
        #     # print(word_freq.word)
            
        # ##### NEED TO COMPLETE? ######
    
        # # print(len(random_list))
        
        # # for word_freq in random_list:
        # #     print(word_freq)
       
        # # print(len(copy_words_frequencies))
        
        # counter = len(deepcopy_words_frequencies)
        
        # for word_freq in list(deepcopy_words_frequencies):

        #     agent.delete_nodes(agent.rootNode,word_freq.word)
        #     counter -= 1
            
        #     if (counter == 50000 or
        #         counter == 45000 or
        #         counter == 40000 or
        #         counter == 35000 or
        #         counter == 30000 or
        #         counter == 25000 or
        #         counter == 20000 or
        #         counter == 15000 or
        #         counter == 10000 or
        #         counter == 5000 or
        #         counter == 0):

        #         end_timer = time.time_ns()
        #         print("Time Elasped for Deleting word count", counter, "is:\t", end_timer - start_timer)
                
        #         output_file.write(f"{counter}\t{end_timer - start_timer}\n")    
        #         start_timer = time.time_ns()
                

        
        # # Result of HashTable
    
        output_file = open(output_filename, 'w')
        
        output_file.write(f"Length of Hash\tNanoseconds\n")  
        
        start_timer = time.time_ns()
        
        
        # print(list(agent.dict))
        random_list = list(agent.dict)
        random.shuffle(random_list)
        # print(random_list)
        
        for word in random_list:

            agent.delete_word(word)
            
            if (len(agent.dict) == 50000 or
                len(agent.dict) == 45000 or
                len(agent.dict) == 40000 or
                len(agent.dict) == 35000 or
                len(agent.dict) == 30000 or
                len(agent.dict) == 25000 or
                len(agent.dict) == 20000 or
                len(agent.dict) == 15000 or
                len(agent.dict) == 10000 or
                len(agent.dict) == 5000 or
                len(agent.dict) == 0):
        
                end_timer = time.time_ns()
                # print("Number of words remaining:", len(agent.list))
                print("Time Elasped for Deleting word count", len(agent.dict), "is:\t", end_timer - start_timer)
                
                output_file.write(f"{len(agent.dict)}\t{end_timer - start_timer}\n")
                start_timer = time.time_ns()
        

        # Obtaining result of List
        
        
        # word_count = len(agent.list)
        # # start_timer = time.time_ns()
    
        # output_file = open(output_filename, 'w')
        
        # output_file.write(f"Length of List\tNanoseconds\n")
        
        # counter = 0
        # random_list = agent.list
        # random.shuffle(random_list)
        
        # start_timer = time.time_ns()
        
        # #Testing only
        #        # for word_frequency in random_list:
        #        #     print(word_frequency.word)
        #         #     counter += 1
                
        #        # print(counter)
        #        # print(len(random_list))
        # #Testing End
        
        # counter = 50000
        # for word_frequency in list(random_list):
        #     # print(word_frequency.word)
        #     agent.delete_word(word_frequency.word)
        #     counter -= 1
            
        #     if (len(random_list) == 50000 or
        #         len(random_list) == 45000 or
        #         len(random_list) == 40000 or
        #         len(random_list) == 35000 or
        #         len(random_list) == 30000 or
        #         len(random_list) == 25000 or
        #         len(random_list) == 20000 or
        #         len(random_list) == 15000 or
        #         len(random_list) == 10000 or
        #         len(random_list) == 5000 or
        #         len(random_list) == 0):
                
        #         end_timer = time.time_ns()
        #         # print("Number of words remaining:", len(agent.list))
        #         print("Time Elasped for Deleting word count", len(random_list), "is:\t", end_timer - start_timer)
                
        #         output_file.write(f"{len(random_list)}\t{end_timer - start_timer}\n")
        #         start_timer = time.time_ns()
        
        # print(counter)

                
        
        
    except FileNotFoundError as e:
        print("Data file doesn't exist.")
        usage()

  