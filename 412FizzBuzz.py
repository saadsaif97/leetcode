from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if(not 1 <= n <= 10**4):
            return ["out of constraints"]

        ans = []
        for i in range(1, n+1):
            divisibleByThree = i % 3 == 0
            divisibleByFive = i % 5 == 0
            divisibleByThreeAndFive = divisibleByThree and divisibleByFive
            if(divisibleByThreeAndFive):
                ans.append("FizzBuzz")
            elif(divisibleByThree):
                ans.append("Fizz")
            elif(divisibleByFive):
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans


solution = Solution()
print(solution.fizzBuzz(3))
print(solution.fizzBuzz(5))
print(solution.fizzBuzz(15))
print(solution.fizzBuzz(0))
