from sklearn.datasets import load_iris

# if __name__ == '__main__':
#     # data=load_iris()
#     # print(data)
#
#     print("xxxx")

def quicksort(array):
    if len(array) < 2:
        return array
    else:
      pivot = array[0] #递归条件
      less = [i for i in array[1:] if i <= pivot]
      greater = [i for i in array[1:] if i > pivot]
      return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    a= quicksort([10, 5, 2, 3])
    print(a)








