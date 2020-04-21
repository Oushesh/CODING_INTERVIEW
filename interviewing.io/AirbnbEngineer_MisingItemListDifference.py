'''
Reference Link for the problem: https://www.youtube.com/watch?v=cdCeU8DJvPM
Using the set data structure we have O(1) lookup time
'''
class Item:
    def find_missing(self,s1,s2):
        if len(s1) > len(s2):
            s_long = set(s1)
            s_short = set(s2)
        else:
            s_long = set(s2)
            s_short = set(s1)
        return s_long.difference(s_short)

    def find_missing_old_style(self,s1,s2):
        '''
        This method has a complexity of O(n²) since
        we have to perform elementwise comparison
        of individual elements.
        '''
        assert(abs(len(s1)-len(s2))==1)
        for i in s1:
            for j in s2:
                print (i,j)
                if not i==j:
                    return i

    def find_missing_xor(self,s1,s2):
        xor_sum = 0
        for num in s1:
            xor_sum ^= num
            print (xor_sum)
        for num in s2:
            xor_sum ^=num
            #print (xor_sum)
        return xor_sum


if __name__ =="__main__":
    current_Item = Item()
    s1 = [4,12,9,5,6]
    s2 = [4,12,9,6]
    print ('Missing Item is:',current_Item.find_missing(s1,s2))
    print ('Missing Item based on old fashion comparison is:',current_Item.find_missing_old_style(s1,s2))
    print ('Missing Item based on XOR method',current_Item.find_missing_xor(s1,s2))
