n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

def get_left_child(i):
    return 2 * i + 1

def get_right_child(i):
    return 2 * i + 2

def max_heapify(arr, n, i):
    left = get_left_child(i)
    right = get_right_child(i)
    largest = i

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # build the max heap
    for i in range(n, -1, -1):
        max_heapify(arr, n, i)

    # extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

    return arr

for n in heap_sort(nums):
    print(n)
"""수 정렬하기 2
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	158799	43339	29603	30.021%
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1 
5
5
4
3
2
1
예제 출력 1 
1
2
3
4
5"""