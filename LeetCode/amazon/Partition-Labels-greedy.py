#In the greedy approach we find the
#last element and then set the ancho there.

#greedy Approch
#Step 1 Find the last position
# of the element enountered.
#as we loop down the string
# we extend the position by
# that last position

class Solution():
    def partitionLabels(self,S):
        #Find the last position of
        #each element and store in dictionary.
        last = {count: i for i, count in enumerate(S)}
        #initialize the anchor
        anchor = 0
        j      = 0
        output = []
        for i,c in enumerate(S):
            j = max(j,last[c]) #max between the current j and string value
            if i==j:
                output.append(i-anchor+1) #get the length of the output.
                anchor = i+1
        return output

if __name__ == '__main__':
    S      = "ababcbacadefegdehijhklij"
    object = Solution()
    output = object.partitionLabels(S)

    print (output)
