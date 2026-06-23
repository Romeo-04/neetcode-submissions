class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_prod = [1]
        suff_prod = []

        running_value = 1

        for i in nums:
            running_value *= i
            pref_prod.append(running_value)

        rev_num = list(reversed(nums))

        running_value = 1

        for i in rev_num:
            running_value *= i
            suff_prod.append(running_value)
        
        suff_prod = suff_prod[::-1]
        suff_prod.pop(0)
        suff_prod.append(1)

        results = []

        for i in range(len(nums)):
            results.append(pref_prod[i] * suff_prod[i])
        

        return results
    
        
        


        

        

            
            
