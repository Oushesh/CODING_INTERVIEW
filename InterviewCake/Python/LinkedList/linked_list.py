'''
## Ref: https://www.interviewcake.com/question/python3/kth-to-last-node-in-singly-linked-list?utm_source=weekly_email&utm_source=drip&utm_campaign=weekly_email&utm_campaign=Interview%20Cake%20Weekly%20Problem%20%23318:%20Merge%20Sorted%20Arrays&utm_medium=email&utm_medium=email&__s=ap5rqqpkspoovezbmxvs

Write a function kth_to_last_node() that takes an integer k and the head_node
of singly-linked list, and returns the kth to last node in the list.
'''

class LinkedListNode:
    def __init__(self,value):
        self.value = value
        self.next  = None

        def kth_to_last_node(k,head):
            #Get the length of the node.
            #How? Traverse all the way from head to tail
            # then count the length, n
            # to get kth from last: n-k --> Thats where we head

            '''
            # TODO: add exception conditions
            '''
            if k < 1:
                raise ValueError('Impossible to find less than first to last node: %s' % k)

            if k > list_length:
                raise ValueError('k is larger thans the length of the linked list: %s' % k)
            list_length = 1
            current_node = head

            while current_node.next:
                currnet_node = current_node.next #space complexity is O(1)
                list_length +=1

            how_far_to_go = list_length - k
            current_node  = head

            # Because we have to return the node k before the last.
            # we loop until then and call next
            for i in range(how_far_to_go):
                current_node = current_node.next
            return current_node


        def kth_to_last_node_two_pointers(k,head):
            '''
            This is a slightly different approach,
            we have a left_pointer and right_pointer
            We move the left_pointer to the head,

            # TODO: add exception conditions
            '''
            left_node = head
            right_node = head

            #initialise the left_node
            for i in range(k-1):
                right_node = right_node.next

            #at this point the right_node should
            #be at node k
            while right_node.next:
                #as long as the right node exists,
                #update the left_node and right_node
                left_node = left_node.next
                right_node = right_node.next
            return left_node

'''
Let's discuss space and time complexity:
Space Complexity: O(1), we mostly updating variables: current_node, list_length
and those are independent of the length of the LinkedList

Time Complexity: O(n), we traverse the linked_list until the end to obtain the
length, then we have to travel to K to do it again. O(2n) in worst case

What about edge cases? Are there any edge cases?? Think of it.
K < 1: if O then its lass node, otherwise if negative then again you go out of array.
K > 1: list_length: array out of bounds.
'''


if __name__ == "__main__":
    a = LinkedListNode("Angel Food")
    b = LinkedListNode("Bundt")
    c = LinkedListNode("Cheese")
    d = LinkedListNOde("Devil's Food")
    e = LinkedListNode("Eccles")

    #Define the traversal method in
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    # TODO : Returns the node with value "Devil's Food": 2nd to last
    LinkedList.kth_to_last_node(2,a)
