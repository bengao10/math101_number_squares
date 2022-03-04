#############################
## Written by Benjamen Gao
## For Math 101 Winter 2022
## Last Edit: B^2 3/4/2022
## Notes: Now Third Iteration
#############################

import math
import cvxpy as cp
import matplotlib.pyplot as plt


def main():
    find_distribution()
    # manual_input()


def find_distribution():
    sums = 50
    totals = dict()
    record = dict()
    for i in range(sums):
        print(f"Currently at {i}")
        for j in range(sums):
            for x in range(sums):
                for y in range(sums):
                    callable([i, j, x, y], totals, record)
    plot(totals)
    print(totals)
    while True:
        file = open('totals.txt', 'w')
        val = int(input("What number would you like to see? "))
        all_vals = record[val]
        for elem in all_vals:
            file.write(str(elem))
            file.write('\n')


def plot(totals):
    x = []
    y = []
    for key in totals:
        x.append(key)
        y.append(totals[key])
    plt.scatter(x, y)
    plt.show()


def manual_input():
    # nums = list()
    # for i in range(4):
    #     nums.append(float(input(f"Please enter the {ORDER[i]} number: ")))
    nums = [math.pi, math.e, math.sqrt(2), math.sqrt(3)]
    total_steps = 0
    while True:
        print(f"{nums}, distance: {return_max(nums)}")
        if nums[0] == 0 and nums[1] == 0 and nums[2] == 0 and nums[3] == 0:
            break
        total_steps += 1
        nums = [abs(nums[0] - nums[1]), abs(nums[1] - nums[2]), abs(nums[2] - nums[3]), abs(nums[3] - nums[0])]
    print(f"Terminated in {total_steps} steps")


def return_max(config):
    return max(config[0], config[1], config[2], config[3])


def distance_test(config):
    x = cp.Variable(1)
    objective = cp.Minimize((config[0] - x) ** 2 + (config[1] - x) ** 2 + (config[2] - x) ** 2 + (config[3] - x) ** 2)
    constraints = [-100 <= x, x <= 100]
    prob = cp.Problem(objective, constraints)
    prob.solve()
    return prob.value


def callable(nums, step_tracker, record):
    starting = nums
    total_steps = 0
    while True:
        if nums[0] == 0 and nums[1] == 0 and nums[2] == 0 and nums[3] == 0:
            break
        total_steps += 1
        nums = [abs(nums[0] - nums[1]), abs(nums[1] - nums[2]), abs(nums[2] - nums[3]), abs(nums[3] - nums[0])]
    if total_steps in step_tracker:
        step_tracker[total_steps] += 1
        record[total_steps].append(starting)
    else:
        step_tracker[total_steps] = 1
        record[total_steps] = [starting]


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
