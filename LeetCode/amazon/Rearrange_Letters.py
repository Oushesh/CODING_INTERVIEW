#https://www.youtube.com/watch?v=1tjyR-IvbsU
MAX_CHAR = 256

def nextChar(freq, dist):
    Max = float('-inf')
    for i in range(0, MAX_CHAR):
        if (dist[i] <= 0 and freq[i] > 0 and (Max == float('-inf') or freq[i] > freq[Max])):
            Max = i
    return Max

def rearrange(string, out, d):
    # Find length of input string
    n = len(string)
    # Create an array to store all characters
    # and their frequencies in str[]
    freq = [0] * MAX_CHAR

    # Traverse the input string and store frequencies
    # of all characters in freq[] array.
    for i in range(0, n):
        freq[ord(string[i])] += 1

    # Create an array for inserting the values at
    # correct distance dist[j] stores the least
    # distance between current position and the
    # we next position can use character 'j'
    dist = [0] * MAX_CHAR

    for i in range(0, n):

        # find next eligible character
        # next eligible character
        j = nextChar(freq, dist)

        # return 0 if string cannot be rearranged
        if j == float('-inf'):
            return 0

        # Put character j at next position
        out[i] = chr(j)

        # decrease its frequency
        freq[j] -= 1

        # set distance as d
        dist[j] = d

        # decrease distance of all characters by 1
        for i in range(0, MAX_CHAR):
            dist[i] -= 1

    # return success
    return 1

if __name__ == "__main__":
    string = "aaaabbbcc"
    n = len(string)

    # To store output
    out = [None] * n

    if rearrange(string, out, 2):
        print(''.join(out))
    else:
        print("Cannot be rearranged")
