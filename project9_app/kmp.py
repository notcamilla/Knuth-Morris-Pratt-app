import numpy as np

def lps(pattern):
    n = len(pattern)
    n_lps = np.zeros(n, dtype = int)
    j = 0
    i = 1
    while i < n:
        if pattern[i] == pattern[j]:
            n_lps[i] = j + 1
            j += 1
            i += 1
        elif j != 0:
            j = n_lps[j-i]
        else:
            n_lps[i] = 0
            i += 1

    return n_lps


def kmp(pattern, s):
    n = len(pattern)
    m = len(s)
    n_lps = lps(pattern)
    j = 0 # pattern index
    i = 0 # s index
    idx = []

    while i < m:
        if s[i] == pattern[j]:
            j += 1
            i += 1
        if j == n:
            idx.append(i-j)
            j = n_lps[j-1]
        elif i < m and s[i] != pattern[j]:
            if j != 0:
                j = n_lps[j-1]
            else:
                i += 1

    result= np.array(idx)
                
    return result, result.shape[0]

def short_seq_check(seq):
    return all(nt in 'ACGT' for nt in seq)
            
