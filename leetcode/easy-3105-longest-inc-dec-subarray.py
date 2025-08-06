from typing import Literal


def sign(n: int) -> Literal[-1, 1] | None:
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return None


def subarray(nums: list[int]) -> int:
    ans: list[int] = [0] * len(nums)

    for i in range(len(nums)):
        direction: Literal[-1, 1] | None = None
        count: int = 1
        # print("===================")
        for j in range(i + 1, len(nums)):
            # print(f"{j-1=}, {nums[j-1]=}, {j=}, {nums[j]=}, {direction=}, {count=}")
            if direction is None and nums[j - 1] != nums[j]:
                direction = sign(nums[j] - nums[j - 1])
                count += 1

            elif direction is not None and direction == sign(nums[j] - nums[j - 1]):
                count += 1

            else:
                break
            # print(f"{j-1=}, {nums[j-1]=}, {j=}, {nums[j]=}, {direction=}, {count=}")

        ans[i] = count

    return max(ans)


def test():
    assert subarray([1, 4, 3, 3, 2]) == 2
    assert subarray([3, 3, 3, 3]) == 1
    assert subarray([3, 2, 1]) == 3


test()
