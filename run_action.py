#!/usr/bin/env python3
import time
import datetime

print("Starting continuous action for 10 seconds...")
print("=" * 70)

start_time = time.time()
iteration = 1

while time.time() - start_time < 10:
    elapsed = time.time() - start_time
    timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[Iteration {iteration:2d}] Time: {timestamp} | Elapsed: {elapsed:6.2f}s | Status: ✓ Running...")
    iteration += 1
    time.sleep(1)

print("=" * 70)
print(f"✓ Completed! Total runtime: {time.time() - start_time:.2f} seconds")
print(f"✓ Total iterations executed: {iteration - 1}")
print(f"✓ Action finished successfully")
