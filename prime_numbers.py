'''
Redo of DBS Code challenge for their SEED programme ~ Not actual attempt

- Multiple Inputs
- First input is number of inputs?
- The rest of the inputs are numbers from 1 - < 1 000 000 # Forgot actual number
- Print out the numbers in the inputs based on their prime factorization

EG: 
12 = 2 * 2 * 3
4 = 2 * 2
6 = 2 * 3
9 = 3 * 3
8 = 2 * 2 * 2

Output:
4
8
12
6
9
'''


def get_prime_number_list():
    '''
    Generate a list of prime numbers. It ends at 500,000 since we're only testing numbers
    below 1 000 000, and if we're validating for prime numbers, the max it can get is num/2
    '''
    prime_number_list = [2]
    for test_prime in range (3,1000,2): # 500000
        # Because anything a multiple of 2 will not be a prime number
        _midpoint = test_prime / 2  
        for i in prime_number_list:
            if test_prime % i == 0:
                break
            # if i == prime_number_list[-1]:
            if i > _midpoint:
                # Testing the last number in prime number list, and test_prime is still not divisible
                prime_number_list.append(test_prime)
                break
    print("Prime number list obtained!")
    return prime_number_list


def get_prime_factorization(number, prime_number_list):
    _prime_factors_list = []
    remaining_number = number
    for test_prime in prime_number_list:
        while True:
            if remaining_number % test_prime == 0:
                _prime_factors_list.append(test_prime)
                remaining_number = remaining_number / test_prime
                # print("number: {} test_prime: {} remaining_number: {}".format(number,test_prime,remaining_number))
            else:
                break
        if remaining_number == 1:
            break

    return _prime_factors_list

def sort_by_prime_factorization(to_sort)
        

def main():
    prime_number_list = get_prime_number_list()
    total_values = input("Input the total number of values to sort by prime factorization: ")
    to_get_prime_factors = []
    for i in range(int(total_values)):
        new_num = int(input("Input value for value {}: ".format(i+1)))
        to_get_prime_factors.append(new_num)


    to_sort = {}
    for input_num in to_get_prime_factors:
        to_sort[input_num] = get_prime_factorization(input_num, prime_number_list)


    sorted_list = sort_by_prime_factorization(to_sort)
    

if __name__ == '__main__':
    main()