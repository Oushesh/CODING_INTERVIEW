
def hash_table(string):
    dict = {}
    for i in string:
        dict[i] = string.count(i) #python counter method.
    return dict

def nextChar(dist, freq):
    for key, value in dist.items():
        if value <=0 and freq >0:
    return None

def rearrange(input,k):
    #Hash Table counter
    dist = {i:0 for i in input}
    n = len(input)
    output = []

    for i in range(0,n):
        nxt=nextChar(dist,freq)
        output.append(nxt)



    return output

if __name__ == "__main__":
    input = "aaaabbbcc"
    print (hash_table(input))
    k     = 2
    output = rearrange(input,k)
