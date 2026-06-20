class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_lookup = dict()
        answer = []

        for index,num in enumerate(nums):
            if num_lookup.get(num) == 1:
                num_lookup[num] += 1
                print(num_lookup[num])
            else:
                num_lookup[num] = 1

        for num in nums:
            match = target - num

            if num_lookup.get(match) is not None:
                if num != match:
                    answer.append(num)

                if num == match:
                    if num_lookup.get(match) == 2:
                        answer.append(num)
        
        answer_1 = answer[0]
        answer_2 = answer[1]

        ind_answer = []

        for index,num in enumerate(nums):
            if num == answer_1 or num == answer_2:
                ind_answer.append(index)

        return ind_answer

        
