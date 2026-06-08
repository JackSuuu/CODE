'''
# Why do we need two arrays (A and B)?
In standard MergeSort:

We recursively divide the array and merge two sorted halves.

Merging requires extra space to store the result while comparing and combining.

Usually, you’d allocate a temporary array each time you merge — 
but that can be wasteful and use a lot of memory.

'''

def merge_a_to_b(A, B, m, p, n):
    i, j, k = m, p, m
    while i < p and j < n:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1
    while i < p:
        B[k] = A[i]
        i += 1
        k += 1
    while j < n:
        B[k] = A[j]
        j += 1
        k += 1

def merge_b_to_a(B, A, m, p, n):
    i, j, k = m, p, m
    while i < p and j < n:
        if B[i] <= B[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = B[j]
            j += 1
        k += 1
    while i < p:
        A[k] = B[i]
        i += 1
        k += 1
    while j < n:
        A[k] = B[j]
        j += 1
        k += 1

def merge_sort(A, B, m, n):
    if n - m > 1:
        q = (m + n) // 2
        p = (m + q) // 2
        r = (q + n) // 2

        merge_sort(A, B, m, p)
        merge_sort(A, B, p, q)
        merge_sort(A, B, q, r)
        merge_sort(A, B, r, n)

        merge_a_to_b(A, B, m, p, q)
        merge_a_to_b(A, B, q, r, n)
        merge_b_to_a(B, A, m, q, n)

if __name__ == "__main__":
    A = [9, 2, 7, 1, 5, 3, 8, 4]
    n = len(A)
    B = [0] * n  # This is array B

    merge_sort(A, B, 0, n)

    print("Sorted array:", A)
