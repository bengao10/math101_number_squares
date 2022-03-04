import random

max_iter = 10000

def main():
    all_converged = []
    for i in range(1, 1000):
        print(i)
        if converged(i):
            all_converged.append(i)
    print(all_converged)


def converged(n):
    arr = [random.randint(-100, 100) for _ in range(n)]
    total_iter = 0
    while not check_convergence(arr):
        arr = do_iteration(arr, n)
        total_iter += 1
        if total_iter == max_iter:
            return False
            # break
    #print(f"Configuration: {arr}")
    if check_convergence(arr):
        #print(f"Converged in {total_iter} iterations")
        return True


def check_convergence(arr):
    #maximum = max(arr)
    for elem in arr:
        if elem != 0:
            #print(f"Not converged. Distance: {maximum}")
            return False
    #print(f"Converged. Distance: {maximum}")
    return True


def do_iteration(arr, n):
    new_arr = [0 for _ in range(n)]
    for i in range(n):
        if i != n - 1:
            new_arr[i] = abs(arr[i + 1] - arr[i])
        else:
            new_arr[i] = abs(arr[-1] - arr[0])
    return new_arr


if __name__ == "__main__":
    main()
