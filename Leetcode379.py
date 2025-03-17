#Time Complexity = O(n)
#Space Complexity = O(n)
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.nums = set(range(maxNumbers))
        print(self.nums)
    def get(self) -> int:
        return self.nums.pop() if self.nums else -1

    def check(self, number: int) -> bool:
        return number in self.nums
    def release(self, number: int) -> None:
        self.nums.add(number)
