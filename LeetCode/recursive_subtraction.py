'''
Test Function: recursive delete:
'''

def recursive_sub(list,first=0,second=1):
    output = 2
    for i in range(len(list)):
        output = output-list[i]
    return output

'''
Example:
set_A = set([(1,1),(3,1),(1,3),(3,3)])
>>> set_B = set([(3,1),(3,2),(4,2),(4,1)])
>>> set_C = set([(3,2),(3,4),(4,2),(4,4)])
>>> set_D = set([(2,3),(3,4),(2,4),(3,3)])
>>> set_E = set([(1,3),(2,4),(1,4),(2,3)])
big_set = set([(1,1),(4,1),(1,4),(4,4)])

--> output_set = set() #empty set

now recursively it should be

output_set = set()
output_set = set_A - output_set() --> set_A
'''
def recursive_set_delete(list_set):
    output_set = list_set[0]
    for i in range(1,len(list_set)):
        #print (list_set[i])
        output_set = output_set - list_set[i]
    return output_set

if __name__ == "__main__":
    list = [1,2,3,4,5]
    print (recursive_sub(list))
    big_set = set([(1,1),(4,4),(1,4),(4,1)])
    ##list_set_delete
    list_set = []
    list_set=[{(1,1),(3,1),(1,3),(3,3)},{(3,1),(3,2),(4,2),(4,1)},{(3,2),(3,4),(4,2),(4,4)},{(2,3),(3,4),(2,4),
    (3,3)},{(1,3),(2,4),(1,4),(2,3)},{(1,1),(4,4),(1,4),(4,1)}]
    print (recursive_set_delete(list_set))

    
