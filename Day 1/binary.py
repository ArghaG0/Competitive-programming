class BinarySearch:
    def search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

def main():
    arr = [10, 20, 30, 40, 50]
    target = 40
    bs = BinarySearch()
    result = bs.search(arr, target)
    print("Index:", result)

if __name__ == "__main__":
    main()
