from multiprocessing import Pool, current_process, cpu_count


def worker(n):
    sum = 0
    for i in range(n):
        sum += i
    print(f"{n}: {sum}")
    return sum


def callback(result):
    print(f"Result in callback: {result}")

    
def factorize(*number):
    # YOUR CODE HERE


    with Pool(cpu_count()) as p:
        p.map_async(
            worker,
            number,
            callback=callback,
        )
        p.close()  # перестати виділяти процеси в пулл
        p.join()  # дочекатися закінчення всіх процесів

        print(f'End {current_process().name}')

    raise NotImplementedError() # Remove after implementation


a, b, c, d  = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]