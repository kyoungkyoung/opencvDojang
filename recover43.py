import threading
import time

def calculate_sum(start, end, result):
    total_sum = 0
    for i in range(start, end + 1):
        total_sum += i
    result.append(total_sum)

if __name__ == "__main__":
    start_time = time.time()

    result = []
    thread1 = threading.Thread(target=calculate_sum, args=(1, 50000000, result))
    thread2 = threading.Thread(target=calculate_sum, args=(50000001, 100000000, result))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    total_sum = sum(result)

    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print("1부터 100000000까지의 합:", total_sum)
    print("실행 시간:", elapsed_time, "초")