
# 快速排序是一种基于递归的 Divide & Conquer 算法，
# 其核心思想为将数组分为比基准值(pivot)小 / 大 的两组数组
# 不断拆分，并在拆分至有序列表时回溯
def quick_sort(sequence):
    if len(sequence) < 2 or not sequence:
        return sequence
    else:
        pivot = sequence[0]  # pivot could be first or mid or last element
        less = []
        more = []
        for each in sequence[1:]:
            if each <= pivot:
                less.append(each)
            if each > pivot:
                more.append(each)
        return quick_sort(less) + [pivot] + quick_sort(more)


print(quick_sort([0, 9, 3, 8, 2, 7, 5]))
