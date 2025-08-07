import time
import sys

def run_benchmark():
    count = 0
    for _ in range(int(1e8)):
        count += 1

if __name__ == "__main__":
    target_time = float(sys.argv[1])
    start = time.time()
    run_benchmark()
    end = time.time()
    actual_time = end - start
    print(f"{actual_time:.10f}", end="")
