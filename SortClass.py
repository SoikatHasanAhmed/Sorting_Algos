import time
import random
import heapq

class SortClass:
    global runtime
    global array
    class algo_name:
        bubble_sort = 1
        insertion_sort = 2
        selection_sort = 3
        merge_sort = 4
        heap_sort = 5
        quick_sort = 6
        counting_sort = 7
        radix_sort = 8




    def __init__(self, name_of_algo,input_arrray):
        # Remember Self just refers to the object you are passing
        self.algoname = name_of_algo
        self.array = input_arrray
        self._compute_algos(name_of_algo,input_arrray)



    def _compute_algos(self,name_algo_to_compute,array):
        start_time = time.time()
        if name_algo_to_compute ==1 :


                changed = True
                while changed:
                    changed = False
                    for i in range(len(array) - 1):
                        if array[i] > array[i + 1]:
                            array[i], array[i + 1] = array[i + 1], array[i]
                            changed = True
                t1 = time.time() - start_time
                self.runtime =  t1

        if name_algo_to_compute == 2:


            for i in range(1, len(array)):
                j = i - 1
                key = array[i]
                while (array[j] > key) and (j >= 0):
                    array[j + 1] = array[j]
                    j -= 1
                array[j + 1] = key
            t2 = time.time() - start_time
            self.runtime = t2

        # Selection Sort
        if name_algo_to_compute == 3:
            start_time = time.time()
            for i, e in enumerate(array):
                mn = min(range(i, len(array)), key=array.__getitem__)
                array[i], array[mn] = array[mn], e
            t3 = time.time() - start_time
            self.runtime = t3

        # Merge sort
        if name_algo_to_compute == 4:

            def _mergeSort(alist):
                start_time = time.time()
                #    print("Splitting ",alist)
                if len(alist) > 1:
                    mid = len(alist) // 2
                    lefthalf = alist[:mid]
                    righthalf = alist[mid:]

                    _mergeSort(lefthalf)
                    _mergeSort(righthalf)

                    i = 0
                    j = 0
                    k = 0
                    while i < len(lefthalf) and j < len(righthalf):
                        if lefthalf[i] < righthalf[j]:
                            alist[k] = lefthalf[i]
                            i = i + 1
                        else:
                            alist[k] = righthalf[j]
                            j = j + 1
                        k = k + 1

                    while i < len(lefthalf):
                        alist[k] = lefthalf[i]
                        i = i + 1
                        k = k + 1

                    while j < len(righthalf):
                        alist[k] = righthalf[j]
                        j = j + 1
                        k = k + 1
                t4 = time.time() - start_time
                self.runtime = t4
            #here i call the function because i have to use the function inside the function
            _mergeSort(array)

        # Heap sort


        if name_algo_to_compute == 5:



            heapq.heapify(array)
            array[:] = [heapq.heappop(array) for i in range(len(array))]
            t5 = time.time() - start_time
            self.runtime = t5
        if name_algo_to_compute == 6:
            def _quickSort(arr):
                start_time = time.time()
                less = []
                pivotList = []
                more = []
                if len(arr) <= 1:
                    return arr
                else:
                    pivot = arr[0]
                    for i in arr:
                        if i < pivot:
                            less.append(i)
                        elif i > pivot:
                            more.append(i)
                        else:
                            pivotList.append(i)
                    less = _quickSort(less)
                    more = _quickSort(more)
                    t6 = time.time() - start_time
                    self.runtime = t6
                _quickSort(array)
        # counting sort


        if name_algo_to_compute == 7:

            k = max(array)
            counter = [0] * (k + 1)
            for i in array:
                counter[i] += 1

            ndx = 0;
            for i in range(len(counter)):
                while 0 < counter[i]:
                    array[ndx] = i
                    ndx += 1
                    counter[i] -= 1
            t7 = time.time() - start_time
            self.runtime = t7

        if name_algo_to_compute == 8:

            RADIX = 10
            maxLength = False
            tmp, placement = -1, 1

            while not maxLength:
                maxLength = True
                # declare and initialize buckets
                buckets = [list() for _ in range(RADIX)]

                # split aList between lists
                for i in array:
                    tmp = i / placement
                    buckets[tmp % RADIX].append(i)
                    if maxLength and tmp > 0:
                        maxLength = False

                # empty lists into aList array
                a = 0
                for b in range(RADIX):
                    buck = buckets[b]
                    for i in buck:
                        array[a] = i
                        a += 1

                # move to next digit
                placement *= RADIX
            t8 = time.time() - start_time
            self.runtime = t8


    def get_runtime(self):
        return  '{:.10f}'.format(self.runtime)


    def get_sorted_array(self):
        return self.array






