class LinearSearch:
    def search(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

def main():
    arr = [10, 20, 30, 40, 50]
    target = 30
    ls = LinearSearch()
    result = ls.search(arr, target)
    print("Index:", result)

if __name__ == "__main__":
    main()
