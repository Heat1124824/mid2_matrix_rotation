class ArrayRotation:
    def __init__(self, arr):
        self.arr = arr

    def rotate_right(self, steps):
        n = len(self.arr)
        steps = steps % n
        for _ in range(steps):
            temp = self.arr[-1] #串列的最後一項
            for i in range(n-1, 0, -1):
                self.arr[i] = self.arr[i-1] #將前一項的值指派到現在的值
            self.arr[0] = temp #串列最後一項會被推到第一項
        return self.arr

    def rotate_left(self, steps):
        n = len(self.arr)
        steps = steps % n
        for _ in range(steps):
            temp = self.arr[0]
            for i in range(n-1):
                self.arr[i] = self.arr[i+1]
            self.arr[-1] = temp
        return self.arr

def main():
    num_array = [1, 5, 8, 6, 3]
    array_rotation = ArrayRotation(num_array)

    
    print(array_rotation.rotate_right(2))
    #print(array_rotation.rotate_left(3))
    

if __name__ == "__main__":
    main()
