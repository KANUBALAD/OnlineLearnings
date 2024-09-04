def is_palindrome(s):

    """ (str) -> bool
    
    Return True if and only if s is a palindrome
    >>> is_palindrom('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrom('dented')
    False
    
    """
# #algorithm one
    # return reverse(s)==s 
 
 # algorithm two
    # the number of chars in s.
    # n = len(s)
    #compare the first half of s to the reverse of the second half
    # omit the middle character of an odd length string
    # return s[:n // 2] == reverse(s[n - n // 2:])


# algorithm threee
    i = 0 # first item
    j = len(s) - 1 # last item
    # print(f'i is {i} and j is {j}')

    #NOTES: When middle of the string is reached then it is a palindrom,
    # for even lenght then j < i and odd i+j 
    while i < j and s[i] == s[j]: 
        i = i+1
        j = j-1
        # print(f'i is {i} and j is {j}')

    return j <= i # this is added such that it works for odd and even

print(is_palindrome('racecar'))
print(is_palindrome('dented'))
print(is_palindrome('noon'))
print(is_palindrome(''))


    
def reverse(s):
    """ (str) -> str
    Return a reversed version of s
    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """
    rev = ''
    # For each character in s, add that char to the beginning of rev
    for ch in s:
        rev = ch + rev
    return rev
        
 

