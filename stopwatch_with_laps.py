# stopwatch_with_laps.py

import time

def stopwatch():
    input("Press Enter to start.")
    start_time = time.time()
    laps = []
    while True:
        command = input("Press Enter for a lap or type 'stop' to end: ").strip().lower()
        if command == "stop":
            break
        lap_time = time.time() - start_time
        laps.append(round(lap_time, 2))
    total_time = time.time() - start_time
    print("Laps:", laps)
    print("Total time:", round(total_time, 2))

# Run the stopwatch
stopwatch()
