"""
'abcd', 'abcde' -> 'e'
'aaabbcdd', 'abdbacade' -> 'e'
"""

C = set('abcd')
D = set('abcde')
X = D - C
print(X)

M = set('aaabbbbbbbcdd')
N = set('abdbacadeeeeeeeeeeeeee')
Y = N - M
print(Y)