#############################
## Written by Benjamen Gao
## For Math 101 Winter 2022
## Last Edit: B^2 2/7/2022
## Notes: First Iteration
#############################
ORDER = ["top left", "top right", "bottom right", "bottom left"]


def main():
    nums = list()
    for i in range(4):
        nums.append(float(input(f"Please enter the {ORDER[i]} number: ")))
    total_steps = 0
    while True:
        print(nums)
        if nums[0] == 0 and nums[1] == 0 and nums[2] == 0 and nums[3] == 0:
            break
        total_steps += 1
        nums = [abs(nums[0] - nums[1]), abs(nums[1] - nums[2]), abs(nums[2] - nums[3]), abs(nums[3] - nums[0])]
    print(f"Terminated in {total_steps} steps")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
