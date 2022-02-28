import random

n = 128
max_iter = 10000


def main():
    arr = [random.randint(-100, 100) for _ in range(n)]
    total_iter = 0
    while not check_convergence(arr):
        arr = do_iteration(arr)
        total_iter += 1
        if total_iter == max_iter:
            break
    print(f"Configuration: {arr}")
    if check_convergence(arr):
        print(f"Converged in {total_iter} iterations")


def check_convergence(arr):
    maximum = max(arr)
    for elem in arr:
        if elem != 0:
            print(f"Not converged. Distance: {maximum}")
            return False
    print(f"Converged. Distance: {maximum}")
    return True


def do_iteration(arr):
    new_arr = [0 for _ in range(n)]
    for i in range(n):
        if i != n - 1:
            new_arr[i] = abs(arr[i + 1] - arr[i])
        else:
            new_arr[i] = abs(arr[-1] - arr[0])
    return new_arr


if __name__ == "__main__":
    main()
