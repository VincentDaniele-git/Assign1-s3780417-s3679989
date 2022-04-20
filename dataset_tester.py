import sys
from dictionary.node import Node
from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
from dictionary.list_dictionary import ListDictionary
from dictionary.hashtable_dictionary import HashTableDictionary
from dictionary.ternarysearchtree_dictionary import TernarySearchTreeDictionary
import time

def usage():
    """
    Print help/usage message.
    """
    print('python3 dataset_tester.py', '<approach> [data fileName] [command fileName] [output fileName]')
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
        
        start_timer = time.time_ns() # Begin Timer
        word_count = 0
        agent.list = []
        
        for line in data_file:
            values = line.split()
            word = values[0]
            frequency = int(values[1])
            word_frequency = WordFrequency(word, frequency)  # each line contains a word and its frequency
        
            
            agent.add_word_frequency(word_frequency)
            
            # words_frequencies_from_file.append(word_frequency)
            
            word_count += 1
            
            if (word_count == 250 or 
                word_count == 500 or
                word_count == 1000 or 
                word_count == 2500 or
                word_count == 2750 or 
                word_count == 10000 or 
                word_count == 25000 or 
                word_count == 49500 or
                word_count == 50000):

                end_timer = time.time_ns()
                print("Time Elasped for word count", word_count, "is: ", end_timer - start_timer)
                
                
        data_file.close()
        
        word_delete_counter = 50000
        
        start_timer = time.time_ns()
        
        for line in agent.list: # (word, frequency)
            
            agent.delete_word(line[0])
            word_delete_counter -= 1
            
            if (word_count == 0 or
                word_count == 250 or 
                word_count == 500 or
                word_count == 1000 or 
                word_count == 2500 or
                word_count == 2750 or 
                word_count == 10000 or 
                word_count == 25000 or 
                word_count == 49500 or
                word_count == 50000):
                
                end_timer = time.time_ns()
                print("Time Elasped for Deleting word count", word_count, "is: ", end_timer - start_timer)
        
        
        # agent.build_dictionary(words_frequencies_from_file)
        
        #timing from this point onwards
        # print(agent.search("tbc"))
        
        
    except FileNotFoundError as e:
        print("Data file doesn't exist.")
        usage()

    # command_filename = args[3]
    # output_filename = args[4]
    # # Parse the commands in command file
    # try:
    #     command_file = open(command_filename, 'r')
    #     output_file = open(output_filename, 'w')

    #     for line in command_file:
    #         command_values = line.split()
    #         command = command_values[0]
    #         # search
    #         if command == 'S':
    #             word = command_values[1]
    #             search_result = agent.search(word)
    #             if search_result > 0:
    #                 output_file.write(f"Found '{word}' with frequency {search_result}\n")
    #             else:
    #                 output_file.write(f"NOT Found '{word}'\n")

    #         # add
    #         elif command == 'A':
    #             word = command_values[1]
    #             frequency = int(command_values[2])
    #             word_frequency = WordFrequency(word, frequency)
    #             if not agent.add_word_frequency(word_frequency):
    #                 output_file.write(f"Add '{word}' failed\n")
    #             else:
    #                 output_file.write(f"Add '{word}' succeeded\n")

    #         # delete
    #         elif command == 'D':
    #             word = command_values[1]
    #             if not agent.delete_word(word):
    #                 output_file.write(f"Delete '{word}' failed\n")
    #             else:
    #                 output_file.write(f"Delete '{word}' succeeded\n")

    #         # check
    #         elif command == 'AC':
    #             word = command_values[1]
    #             list_words = agent.autocomplete(word)
    #             line = "Autocomplete for '" + word + "': [ "
    #             for item in list_words:
    #                 line = line + item.word + ": " + str(item.frequency) + "  "
    #             output_file.write(line + ']\n')
    #         else:
    #             print('Unknown command.')
    #             print(line)

    #     output_file.close()
    #     command_file.close()
        
        
    # except FileNotFoundError as e:
    #     print("Command file doesn't exist.")
    #     usage()