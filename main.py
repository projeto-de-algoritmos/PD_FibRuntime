import time
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# A naive recursive solution
def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


# A memoized solution
def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n] = result
    return result


def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_2(n, memo)


# A bottom-up solution
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

size_1 = 5
size_2 = 10
size_3 = 25
size_4 = 30

sizes = [ size_1, size_2, size_3, size_4 ]

dataset_fib = {}
dataset_fib_memo = {}
dataset_fib_bottom_up = {}

for size in sizes:
    
    start_time = time.time()    
    fib(size)
    end_time = time.time() - start_time
    dataset_fib[size] = end_time

    start_time = time.time()    
    fib_memo(size)
    end_time = time.time() - start_time
    dataset_fib_memo[size] = end_time

    start_time = time.time()    
    fib_bottom_up(size)
    end_time = time.time() - start_time
    dataset_fib_bottom_up[size] = end_time


print(dataset_fib)
print(dataset_fib_memo)
print(dataset_fib_bottom_up)


plt.plot(dataset_fib.values(), sizes, color='red')
plt.plot(dataset_fib_memo.values(), sizes, color='blue')
plt.plot(dataset_fib_bottom_up.values(), sizes, color='green')


plt.title("Comparação Fib vs MemoFib vs BottomUp")
red_patch = mpatches.Patch(color='red', label='Fib')
blue_patch = mpatches.Patch(color='blue', label='MemoFib')
green_patch = mpatches.Patch(color='green', label='BottomUp')

plt.legend(handles=[red_patch, blue_patch, green_patch])
plt.xlabel('Tempo(s)')
plt.ylabel('Tamanho do vetor')
plt.grid(color='r', linestyle='-', linewidth=0.2)

plt.show()
