import random
import time
import os


def radix_sort(arr):
    negatives = [x for x in arr if x < 0]
    positives = [x for x in arr if x >= 0]
    negatives = [-x for x in negatives]
    positives = radix_sort_positive(positives)
    negatives = radix_sort_positive(negatives)
    negatives = [-x for x in reversed(negatives)]

    return negatives + positives


def radix_sort_positive(arr):
    max_value = max(arr)

    for exp in range(len(str(max_value))):
        buckets = [[] for _ in range(10)]

        for num in arr:
            digit = (num // (10 ** exp)) % 10
            buckets[digit].append(num)
            
        arr = [num for bucket in buckets for num in bucket]

    return arr

    
def write_in_file(m):
    mass1 = open(nazv + ".txt", "w")
    mass1.writelines(str(m)+" ")

    mass1.close()
    

def create_array(countelem):
    arr = []
    for i in range(countelem):
        m = random.randint(-countelem*10, countelem*10)
        arr.append(m)
    write_in_file(arr)
    return arr

nazvold = "qsawzdfdfhgfhgfhfghtftx12345"
nazvold2 = "qsawzdfdfhgfhgfhfghtftx12345"
chikl = 1

if __name__ == "__main__":
    while chikl != 0:
        ansver = int(input("1 - начать создание массива, 2 - выйти из программы: "))
        if ansver == 1:
            try:
                file = open(nazvold + ".txt")
            except IOError as e:
                nazvold = "mass1"
                file1 = open(nazvold + ".txt", "w")
                file1.close()
            countelem = int(input("Сколько элементов будет в массиве?: "))
            nazv = str(input("Введите название файла в котором будет исходный массив чисел: "))
            try:
                os.rename(nazvold + ".txt", nazv + ".txt")
            except:
                nazvold = nazv
            nazvold = nazv
            konnazv = str(input("Введите название файла в котором будет отсортированный массив чисел: "))
            try:
                file = open(nazvold2 + ".txt")
            except IOError as e:
                nazvold2 = "mass2"
                file2 = open(nazvold2 + ".txt", "w")
                file2.close()
            try:
                os.rename(nazvold2 + ".txt", konnazv + ".txt")
            except:
                nazvold2 = konnazv
            nazvold2 = konnazv
    
    
            arr = create_array(countelem)
            print(f"Исходный масив  - {arr}")


            times1 = time.time()
            sorted_arr = radix_sort(arr)
    
            times = time.time()
            times_g = times - times1
            times_g = str(times_g*1000).split(".")[0]
            print(f"Отсортированный масив  - {sorted_arr}")

            print("Сгенерированный массив - файл",nazv + ".txt")
            mass1 = open(konnazv + ".txt", "w")
            for i in sorted_arr:
                mass1.write(str(i)+" ")
            mass1.close()
    
            print("Отсортированный по возрастанию массив -",konnazv + ".txt")
            print(f"Algoritm time {times_g} ms")
        elif ansver == 2:
            chikl = 0
    
