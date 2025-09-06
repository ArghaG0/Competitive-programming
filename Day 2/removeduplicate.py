class RemoveDuplicates:
    def process(self, arr):
        seen = set()
        result = []
        for num in arr:
            if num not in seen:
                seen.add(num)
                result.append(num)
        return result

def main():
    arr = [1, 2, 2, 3, 4, 4, 5]
    rd = RemoveDuplicates()
    result = rd.process(arr)
    print("Array without duplicates:", result)

if __name__ == "__main__":
    main()
