#Leet Code course
#Partition it in a way such that no elements from 1 substring occur in the
#other substring.

def hash_table(input:str) -> dict:
    hash = {}
    for i in input:
        if i not in hash:
            hash[i]=input.count(i)
    return hash

#partition(s) = partition(s[:i]+ partition[i+1:a])
#Recursive solution:
def check(s,explored,hash_table):
    output = []
    n = len(s)
    for i in range(n):
        if s[i] not in explored and hash[s[i]]!=0:
            hash[s[i]]-=1
            return 0
        else:
            return output.append(s[i+1:n]),-1

def partition(s:str):
    explored = []
    hash = hash_table(s)
    res, val=check(s,explored,hash)
    if (val!=-1):
        return partition(s)
    else:
        return partition(res)


if __name__ == '__main__':
    S = "ababcbacadefegdehijhklij"
    #output = 9,7,8
    print (hash_table(S))
    print (partition(S))


#Hash table technique
