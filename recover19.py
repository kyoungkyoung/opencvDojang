import time

start_time = time.time()

total_sum = 0
for i in range(1, 100000001):
  total_sum += i

end_time = time.time()
elapsed_time = end_time - start_time

print("1부터 100000000까지의 합:", total_sum)
print(f"실행 시간: {elapsed_time:.6f} 초")  