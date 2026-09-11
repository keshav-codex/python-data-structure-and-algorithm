"""
Tuple Duplicate Counter
Given a tuple, find how many times each element occurs without using collections.Counter.

"""

def duplicate_counter(numbers : tuple ) -> None:
	counted = set()
	for num in numbers:
		if num not in counted:
			print(f"{num} : {numbers.count(num)}")
			counted.add(num)

if __name__ == "__main__":
	nums = (1, 2, 2, 3, 1, 2, 4)
	duplicate_counter(nums)