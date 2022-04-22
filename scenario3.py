

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
        
# TST

        output_file = open(output_filename, 'w')
        output_file.write(f"\tNanoseconds\n")  
        
        selected_word_list = []

        copy_words_frequencies = words_frequencies_from_file
                
        x = copy_words_frequencies
                
        random.shuffle(x)
                
        # counter = 100
        # while counter != 0:
        #     for word_freq in x:
        #         selected_word_list.append(word_freq.word)
        #         counter -= 1
                
        counter = 0 
        
        while counter < 100:
            selected_word_list.append(x[counter].word)
            counter += 1
        
        start_timer = time.time_ns()
        
        for word in selected_word_list: 
            
            # agent.search(word)
            
            #autocomplete - find prefix
            max_num = random.randint(1, 4) 
            agent.autocomplete(word[0:max_num]) 
            
        end_timer = time.time_ns()
        
        print(end_timer - start_timer)
        output_file.write(f"{end_timer - start_timer}")
          



# # LIST
# # Select 100 random words 

    
#         selected_word_list = []

#         copy_words_frequencies = words_frequencies_from_file
                
#         x = copy_words_frequencies
                
#         random.shuffle(x)
                
#         # counter = 100
#         # while counter != 0:
#         #     for word_freq in x:
#         #         selected_word_list.append(word_freq.word)
#         #         counter -= 1
                
#         counter = 0 
        
#         while counter < 100:
#             selected_word_list.append(x[counter].word)
#             counter += 1
        
#         start_timer = time.time_ns()
        
#         for word in selected_word_list:
#             agent.search(word)
            
#         end_timer = time.time_ns()
        
#         print(end_timer - start_timer)
          
        
    except FileNotFoundError as e:
        print("Data file doesn't exist.")
        usage()
