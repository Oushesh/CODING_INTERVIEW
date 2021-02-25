'''
Ref:https://www.glassdoor.com/Interview/There-is-a-fence-with-n-posts-each-post-can-be-painted-with-one-of-the-k-colors-You-have-to-paint-all-the-posts-such-tha-QTN_1377709.htm

Interview Question
Intern Interview

There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence


Mathematics --> Combinatorics Problem


nCr = n!/r!*(n-r)!


Approach 1 --> Combinatorics:
               No constraint: [1,2,3,4,5] 5C2 -->
               Lets treat the long list as a sliding window of length()

Lets list all the possibilities:

Combination of every 2 being same & every one being different.

i)  Double:
    R R  B B
    B B
    G G
    factorial(len(post)/2) if len(post) is even else:
                                        int(len(post))/2 Example if len(post)==5 int(5/2)= 2
                                        output = factorial(2) * len(colors)-1

ii) Single --> 3 2 1 3 2 1 --> fill this all along the len(post)

iii) Sum the 2 to get the output.

Instead if the question referred to like check if a given
colour combination satisfy the criteria. I would have the used the following approach
with a hash map/freq counter and return booelan True or False if the
condition:
            The value of any given key exceeds 2. (dict[key]>2 --> return False)
Assume: N posts in sequence. --> list  [1,2,3,4,5]  5 posts
        K colours --> list
        example: 'R','G','B' --> len(list)=3
        Constraint: no more than 2 adjacent posts have the same color --> posts[i], posts[i+1]

        R,R  --> Loop (i,len(list)-2)
        R,R,G --> sliding window of 3 -->

        unique colours --> build a map --> {R:0,G:0,B:0}
        if found: update {R:1,G:1,B:0}       check --> R,R,G    R,R,B
        check(map)--> return False if dict.value >2


        3 sliding window check:
        at no given time there should more than 2 of the same colour within the sliding window.
        We use this logic to place the stuffs.
        R G B
'''
class Fence:
    def factorial(self,n):
        if n==1:
            return n
        return n*self.factorial(n-1)

    def combinations(self,posts,colors):
        if len(posts)%2==0:
            doublet = self.factorial(len(posts)/2)
            print (doublet)
            #3 2 1 3 2 1 --> Factorial of 3 here is repeated by the times we can
            #fit them in the array
            if len(posts)%len(colors)==0:
                singlet = self.factorial(len(colors))*len(posts)/len(colors)
                print (singlet)
            else:
                #We fit the 3 2 1 one by one
                singlets = []
                start = len(colors)
                for i in range(len(posts)):
                    if start==1:
                        start = len(colors)
                    singlets.append(start)
                    start-=1
                singlet = sum(singlets)
                print (singlet)
        else:
            doublet = self.factorial(int(len(posts)/2))*(len(colors)-1)
            #3 2 1 3 2 1
            #Factorial of 3 here is 3*2*1
            if len(posts)%len(colors)==0:
                singlet = self.factorial(len(colors))*len(posts)/len(colors)
            else:
                #We fit the 3 2 1 one by one
                singlets = []
                start = len(colors)
                for i in range(len(posts)):
                    if start==1:
                        start = len(colors)
                    singlets.append(start)
                    start-=1
                singlet =  sum(singlets)

        combinations = int (doublet + singlet)
        return combinations

    #Extending the function to a more general form
    # TODO: Extend the function to fit a general form
    def combinations_general(self,posts,colors,constraints):
        if len(posts)%len()==0:
            doublets = self.factorial(len(posts))

if __name__ == "__main__":
    '''
    constraints, K = 2 (no more than 2 fences are allowed to have the same color)
    Singlet: [3,2,1,3,2,1]
    '''
    posts = [1,2,3,4,5,6]
    colors = ['R','G','B']
    #constraints, K
    constraints = 2
    given_fence = Fence()
    print ('The number of possibilities to color the posts is:',given_fence.combinations(posts,colors))

#TODO: complete this, debug and write a version for C++
