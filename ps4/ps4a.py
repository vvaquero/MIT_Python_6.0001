# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # base case
    out_list = []
    if len(sequence) == 1:
        return [sequence]
    else:
        out_list = get_permutations(sequence[1:])

        c = sequence[0]
        final_list = []
        for perm in out_list:
            for i in range(len(perm)):
                final_list.append(perm[:i]+c+perm[i:])
            final_list.append(perm + c)
        return final_list


def isCorrect(my_in, my_out):
    for word in my_out:
        assert word in my_in, 'the solution was incomplete! And we found a new permutation'
        if my_in.get(word, 0):
            my_in[word] = 0
        else:
            print(f'word {word}, either repeated or non-existing')
    if sum(my_in.values()) == 0:
        return True
    else:
        return False



if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    dic_val = 1
    expected_output = {'abc': dic_val, 'acb': dic_val, 'bac': dic_val, 'bca': dic_val, 'cab': dic_val, 'cba': dic_val}
    print(f'Expected Output:{expected_output.keys()}')
    perms = get_permutations(example_input)
    print('Actual Output: ', get_permutations(example_input))
    print(f'Is it correct?: {isCorrect(expected_output, perms)}\n\n')

    
    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)
    example_input = 'ZYXW'
    print('Input:', example_input)
    expected_output = {'ZYXW': dic_val, 'YZXW': dic_val, 'XZYW': dic_val, 'ZXYW': dic_val, 'YXZW': dic_val,
                       'XYZW': dic_val, 'WYZX': dic_val, 'YWZX': dic_val, 'ZWYX': dic_val, 'WZYX': dic_val,
                       'YZWX': dic_val, 'ZYWX': dic_val, 'ZXWY': dic_val, 'XZWY': dic_val, 'WZXY': dic_val,
                       'ZWXY': dic_val, 'XWZY': dic_val, 'WXZY': dic_val, 'WXYZ': dic_val, 'XWYZ': dic_val,
                       'YWXZ': dic_val, 'WYXZ': dic_val, 'XYWZ': dic_val, 'YXWZ': dic_val}
    print(f'Expected Output:{expected_output.keys()}')
    perms = get_permutations(example_input)
    print('Actual Output: ', get_permutations(example_input))
    print(f'Is it correct?: {isCorrect(expected_output, perms)}\n\n')

    example_input = 'ab'
    print('Input:', example_input)
    expected_output = {'ba': dic_val, 'ab': dic_val}
    print(f'Expected Output:{expected_output.keys()}')
    perms = get_permutations(example_input)
    print('Actual Output: ', get_permutations(example_input))
    print(f'Is it correct?: {isCorrect(expected_output, perms)}')


    pass #delete this line and replace with your code here

