from collections import Counter

def read_input(filename):
    cases = []
    with open(filename, 'r') as f:
        num_cases = int(f.readline().strip())
        for _ in range(num_cases):
            cases.append(f.readline().strip())
    return cases


def is_vowel(c):
    if c in {'A', 'E', 'I', 'O', 'U'}:
        return True
    return False


def solve(s):
    counter = Counter(s)
    most_frequent_vowel = most_frequent_consonant = ''
    max_freq_consonant = 0
    max_freq_vowel = 0
    
    for char, freq in counter.items():
        if is_vowel(char):
            if max_freq_vowel < freq:
                max_freq_vowel = freq
                most_frequent_vowel = char
        else:
            if max_freq_consonant < freq:
                max_freq_consonant = freq
                most_frequent_consonant = char

    vowel_swaps_count = 0
    for char in s:
        if char == most_frequent_vowel:
            pass
        elif is_vowel(char):
            vowel_swaps_count += 2
        else:
            vowel_swaps_count += 1

    consonant_swaps_count = 0
    for char in s:
        if char == most_frequent_consonant:
            pass
        elif not is_vowel(char):
            consonant_swaps_count += 2
        else:
            consonant_swaps_count += 1

    return min(vowel_swaps_count, consonant_swaps_count)


def test():
    cases = read_input("consistency_chapter_1_input.txt")
    with open('result.txt', 'w') as f:
        for i, case in enumerate(cases):
            swaps_count = solve(case)
            print('Case #{}: {}'.format(i + 1, swaps_count), file=f)


# AAAAAB
# AEIOUB
# AEIBCD
# AEIUBCD -> BBBBBCD -> BBBBBBB (10)
# AAAUBCD (5)
# HAAACKEEERCUUUP -> 12 for vowels, 6 for consonants
# HAAACKEEERCUUUP -> 9 vowels, 8 for consonants 

# vowels? -> find a letter with greater frequency


