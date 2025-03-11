# PROBLEM:
# Write a function print_counts(text) that returns a histogram
# dictionary with how many times each letter appears in a given
# string For example, print_counts("rare") should return
# {'r': 2, 'a': 1, 'e': 1}

def print_counts(text):
    answer = {}
    for c in text:
        answer[c] = text.count(c)
    return answer

def print_counts2(text):
    return {c : text.count(c) for c in text}

def main():
    ans = print_counts2('abracadabra')
  # Should return { 'a' : 5, 'b' : 2, 'c' : 1, 'r' : 2, 'd' : 1}

    for c, count in ans.items():
        print(f'The character {c} appears {count} times')

if __name__ == "__main__":
    main()