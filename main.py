import time


def timer():
    hours = int(input("Hours: "))
    minutes = int(input("Minutes: "))
    seconds = int(input("Seconds: "))

    total_seconds = (hours * 3600) + (minutes * 60) + seconds

    for i in range(total_seconds):
        remaining_time = total_seconds
        hours = remaining_time // 3600
        minutes = (remaining_time - (hours * 3600)) // 60
        seconds = remaining_time - ((hours * 3600) + (minutes * 60))

        print(f"{hours}:{minutes}:{seconds}")
        time.sleep(1)
        total_seconds -= 1

    print("FINISH")


if __name__ == "__main__":
    timer()
