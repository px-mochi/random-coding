'''
Question: We are given a mapping of
A:1
B:2
C:3
...
Z:26

Given an input, find out how many possible encrypted solutions there are of the input.
EG: 123 --> 3 # [1,2,3] [1,23] [12,3]

Initial thought: 
- Simply search for every occurrences of the encrypted string value
- Issue: This would result in duplicates, and does not give me the total number of possible outcomes  

Next steps:
- I realised that only the larger encrypted values will result in potential other solutions.
- This means that numbers [11,12,13,14,15,16,17,18,19,21,22,23,24,25,26] will have 2 solutions.
- 10 and 20 are excluded as 10 can only be split into 1, and 0, and 0 is not one of the mappings.


1223  = 1 2 2 3 | 12 23 | 12 2 3 | 1 2 23 | 1 22 3 | 
123423 = 1 2 3 4 2 3 | 12 3 4 2 3 | 1 23 4 2 3 | 1 23 4 23 | 12 3 4 23 |

Realised this is still another potential issue:
- This doesn't mean that all numbers will split nicely. 
- This will leave out individual digits next to numbers that are too large. (EG: 1, next to 32)
'''
import itertools

def get_mapping():
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mapping = {}
    for i, letter in enumerate(list(abc)):
        mapping[letter] = str(i+1)
    return mapping

def get_reduced_mapping():
    mapping = get_mapping()
    reduced_mapping = {}
    for k,v in mapping.items():
        if int(v) in [11,12,13,14,15,16,17,18,19,21,22,23,24,25,26]:
            reduced_mapping[k] = v
    return reduced_mapping


def find_all(search_term, input_string): # A generator is used to check if the encrypted number exists
    # len_search_term = len(search_term)
    search_pos = input_string.find(search_term)
    while search_pos != -1: # Able to find the number in the encrypted message
        yield search_pos
        search_pos = input_string.find(search_term, search_pos+1) # +1 is to avoid searching for the exact same position - but allows searching for another potential 

def get_possible_numbers(input_string):
    possible_numbers = {}
    mapping = get_mapping()
    reverse_mapping = {}
    for k,v in mapping.items():
        reverse_mapping[v] = k
    for encrypted_num in mapping.values():
        if len([i for i in find_all(encrypted_num,input_string)]) != 0:
            possible_numbers[encrypted_num] = reverse_mapping[encrypted_num]
    return possible_numbers

def get_possible_numbers_repeated(input_string):
    possible_numbers_repeated = []
    possible_numbers = get_possible_numbers(input_string)
    for number in possible_numbers:
        for i in range(int(len(input_string)/len(number))):
            possible_numbers_repeated.append(number)
    return possible_numbers_repeated

def replace_encrypted_numbers(message, possible_numbers):
    mapping = get_mapping()
    for number in possible_numbers:
        message = message.replace(number,possible_numbers[number])
    return message

def main():
    encrypted_message = input("Type in the encrypted message: ")
    possible_numbers_repeated = get_possible_numbers_repeated(encrypted_message)

    halp = itertools.permutations(possible_numbers_repeated,r=len(encrypted_message))
    for i in halp:
        if "".join(i)[0:len(encrypted_message)] == encrypted_message:
            


    # decrypted_texts = set()
    # for number in possible_numbers:
    #     message_test = encrypted_message
    #     decrypted_text = replace_encrypted_numbers(message_test, possible_numbers)
    #     decrypted_texts.add(decrypted_text)

    # print(decrypted_texts)



if __name__ == '__main__':
    main()