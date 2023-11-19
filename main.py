# Sort Program With Python
# Made By 1114 박준현 / @4rNe5
# Github : https://github.com/4rNe5
# 조현아쌤 사랑해요~~ 만점주세요.....

import random
import art


sorted_list = []  # 합병정렬에 사용하는 리스트


# 선택 정렬
def selection_sort(lst):
    # 리스트 구성 요소를 순회
    for i in range(len(lst)):
        # 가장 작은 요소의 인덱스 탐색
        min_idx = i
        for j in range(i + 1, len(lst)):
            # 현재 요소가 기존에 찾았던 가장 작은 요소보다 작으면, 현재 요소의 인덱스를 저장함.
            if lst[j] < lst[min_idx]:
                min_idx = j
        # 가장 작은 요소를 현재 요소와 교환.
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    # 선택 정렬된 리스트를 반환함.
    return lst


# 삽입 정렬
def insertion_sort(lst):
    # Input된 리스트의 첫 번째 요소부터 마지막 요소까지 순회함.
    for i in range(1, len(lst)):
        # 현재 요소를 key로써 저장함
        key = lst[i]
        # key 이전 요소부터 시작, key보다 큰 요소를 오른쪽으로 이동함.
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        # 정렬된 위치에 key를 삽입.
        lst[j + 1] = key
    # 삽입 정렬된 리스트를 반환함.
    return lst


# 버블 정렬
def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1, 0, -1):  # 리스트 마지막 요소부터 리스트 첫 번째 요소까지 역순으로 순회함.
        for j in range(i):  # 리스트 첫 번째 요소부터 리스트 마지막에서 i번째 요소까지 순회
            if lst[j] > lst[j + 1]:  # 현재 요소가 다음 요소보다 크면 두 요소를 교환함.
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    # 버블 정렬된 리스트를 반환함.
    return lst

# 퀵 정렬
def quick_sort(A, left, right):
    # - A: List[int] - 정렬을 요하는 입력 배열
    # - left: int - 정렬할 범위의 좌측 인덱스
    # - right: int - 정렬할 범위의 우측 인덱스

    if left < right:
        # 포인터를 초기화
        i = left + 1
        j = right
        pivot = A[left]

        # 파티션 단계
        while i <= j:
            while i <= right and A[i] <= pivot:
                i += 1
            while j >= left and A[j] > pivot:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]

        # 피벗을 올바른 위치로 이동시킴
        A[left], A[j] = A[j], A[left]

        # 두개의 파티션을 재귀 호출시킴
        quick_sort(A, left, j - 1)
        quick_sort(A, j + 1, right)


# 합병 정렬
def merge_sort(A, left, right):
    global sorted_list
    if left < right:
        mid = (left + right) // 2  # 분할...
        merge_sort(A, left, mid)  # 분할....
        merge_sort(A, mid + 1, right)  # 또 분할...
        sorted_list = [0] * len(A)  # sorted_list를 0으로 초기화
        merge(A, left, mid, right)  # !!합병!!


# 합병 정렬
def merge(A, left, mid, right):
    i = left  # 좌측 리스트의 첫 번째 인덱스
    j = mid + 1  # 우측 리스트의 첫 번째 인덱스
    k = left  # 합병 정렬될 리스트의 첫 번째 인덱스
    # 분할되어있는 리스트의 합병
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted_list[k] = A[i]
            i, k = i + 1, k + 1
        else:
            sorted_list[k] = A[j]
            j, k = j + 1, k + 1
    # 남아있는 리스트의 복사
    while i <= mid:
        sorted_list[k] = A[i]
        i, k = i + 1, k + 1
    while j <= right:
        sorted_list[k] = A[j]
        j, k = j + 1, k + 1
    # sorted_list(임시저장) 리스트를 A(기존) 리스트로 복사
    A[left: right + 1] = sorted_list[left: right + 1]

# 힙 정렬 2
def heapify(arr, n, i):  # n = arr의 길이, i = 루트노드 인덱스
  # 현재 노드를 가장 큰 값으로 설정함
  largest = i
  # 왼쪽 자식 노드에 대한 인덱스를 계산
  l = 2 * i + 1
  # 오른쪽 자식 노드에 대한 인덱스를 계산
  r = 2 * i + 2

  # 왼쪽 자식이 힙의 크기 내에 있고, 현재의 값보다 크면 largest(가장 큰 값)를 왼쪽 자식으로 업데이트함.
  if l < n and arr[i] < arr[l]:
    largest = l
  # 오른쪽 자식이 힙의 크기 내에 있고, 현재의 값보다 크면 largest(가장 큰 값)를 오른쪽 자식으로 업데이트함.
  if r < n and arr[largest] < arr[r]:
    largest = r
  # largest가 변경되면 현재 노드와 largest 노드 값을 교환, 이후 다시 heapify() 함수 호출
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)


# 힙 정렬 2
def heapSort(arr):
  n = len(arr)
  # 최대 힙 구성
  for i in range(n // 2, -1, -1):
    heapify(arr, n, i)
  # 힙에서 원소를 하나씩 꺼내어 정렬함.
  for i in range(n - 1, -1, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)

  # 힙 정렬된 리스트를 반환함
  return arr

# 힙 정렬 1
def heapPush(heap, n):
    # 힙에 원소를 추가, 그리고 힙 속성을 유지
    heap.append(n)
    i = len(heap) - 1
    while i != 0 and n > heap[i // 2]:
        heap[i] = heap[i // 2]
        i //= 2
    heap[i] = n

# 힙 정렬 1
def heapPop(heap):
    # 힙에서 최댓값을 제거후 반환
    size = len(heap) - 1
    if size == 0:
        return None
    p = 0
    i = 1
    root = heap[0]
    last = heap[size]
    while i <= size:
        if i < size and heap[i] < heap[i + 1]:
            i += 1
        if last >= heap[i]:
            break
        heap[p] = heap[i]
        p = i
        i *= 2
    heap[p] = last
    heap.pop()
    return root

# 힙 정렬 1
def heap_sort(lst):
    # 정렬을 요하는 리스트를 Heap에 Input, 그 후 다시 꺼내어 정렬
    heap = [0]
    for e in lst:
        heapPush(heap, e)
    for i in range(1, len(lst) + 1):
        lst[-i] = heapPop(heap)
    # 힙 정렬된 리스트를 반환
    return lst

# 메뉴
def print_menu():
    print("1. 선택 정렬 / Selection Sort")
    print("2. 삽입 정렬 / Insertion Sort")
    print("3. 버블 정렬 / Bubble Sort")
    print("4. 퀵 정렬 / Quick Sort")
    print("5. 합병 정렬 / Merge Sort")
    print("6. 힙 정렬 / Heap Sort")
    print("7. 종료 / Exit")


# 메인 함수
def Sort_main():
    print(art.text2art("4rNe5's Sort"))
    while True:
        # 리스트 생성
        lst = random.sample(range(101), 25)
        print_menu()
        choice = input("원하는 정렬 번호를 선택해 주세요 : ")
        print("")
        if choice == "1":
            print("<선택 정렬 / Selection Sort>")
            print("")
            print("정렬 전 : ", lst)
            print("선택 정렬 후 : ", selection_sort(lst))
        elif choice == "2":
            print("<삽입 정렬 / Insertion Sort>")
            print("")
            print("정렬 전 : ", lst)
            print("삽입 정렬 후 : ", insertion_sort(lst))
        elif choice == "3":
            print("<버블 정렬 / Bubble Sort>")
            print("")
            print("정렬 전 : ", lst)
            print("버블 정렬 후 : ", bubble_sort(lst))
        elif choice == "4":
            print("<퀵 정렬 / Quick Sort>")
            print("")
            print("정렬 전 : ", lst)
            quick_sort(lst, 0, len(lst) - 1)
            print("퀵 정렬 후 : ", lst)
        elif choice == "5":
            print("<합병 정렬 / Merge Sort>")
            print("")
            print("정렬 전 : ", lst)
            merge_sort(lst, 0, len(lst) - 1)
            print("합병 정렬 후 : ", lst)
        elif choice == "6":
            print("<힙 정렬 / Heap Sort>")
            print("")
            lst1=list(lst)
            lst2=list(lst)
            print("{1번 힙 정렬}")
            print("정렬 전 : ", lst1)
            print("1번 힙 정렬 후 : ", heap_sort(lst))
            print("------------------------------------")
            print("{2번 힙 정렬}")
            print("정렬 전 : ", lst2)
            print("2번 힙 정렬 후 : ", heapSort(lst2))
        elif choice == "7":
            exit("<종료 / Finish>")
            print("")
        else:
            print('<번호 오류 / Input Number Error>')
        print("")


if __name__ == "__main__":
    Sort_main()
