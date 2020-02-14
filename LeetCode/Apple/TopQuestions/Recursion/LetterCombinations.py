#Example:
#Input: "23"
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


#How to represent the data?
#Dictionary

#Perform online coding interviews today.

class Solution:
    def letterCombinations(self,digits:str)->list[str]:
        phone = {"2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"]}

        def build_combination(digits):
        output = []
        if digits:
            build_combination(digits)
        return output




if __name__ == "__main__":
    digits ="23"
    output = Solution()
    print ("The output combinations are:",output.letterCombinations(digits))
