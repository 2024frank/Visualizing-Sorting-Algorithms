def selection_sort(items):
    for index in range(len(items) - 1):
        min_index = index
        for checkme in range(index + 1, len(items)):
            print(".", end="") # Uncomment for part C
            if items[checkme] < items[min_index]:
                min_index = checkme  # there was an error on this line

        items[min_index], items[index] = items[index], items[min_index]
     

def merge(left,right):
    left_ind, right_ind = 0,0
    result = []
    while left_ind < len(left) and right_ind < len(right):
        print(".", end="") # Uncomment for part C
        if left[left_ind] < right[right_ind]:
            result.append(left[left_ind])
            left_ind += 1 # error here
        else:
            result.append(right[right_ind])
            right_ind += 1 # error here
    result += left[left_ind:]
    result += right[right_ind:]
    return result

def merge_sort(items):
    if len(items) <= 1:
        return items
    halfway = len(items) // 2
    left = merge_sort(items[:halfway])
    right = merge_sort(items[halfway:])
    return merge(left, right)

def test_sorts():
    alist = [3,5,8,6,2,1,7,4]
    blist = [3,5,8,6,2,1,7,4]
    print("Original list:")
    print(alist)
    print("Sorted with Selection Sort:")
    selection_sort(alist)
    print(alist)
    print("Sorted with Merge Sort:")
    blist = merge_sort(blist)
    print(blist)

if __name__ == "__main__":
    test_sorts()
