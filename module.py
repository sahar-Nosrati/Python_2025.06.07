import random
import time

day_times = ["Morning", "Afternoon", "Evening"]
tempreture = []
uv_index = []

min_uv_index = 0
max_uv_index = 11

min_tempreture = 20
max_tempreture = 40

for index in range(3):
  uv_index.append(random.randint(min_uv_index, max_uv_index))
for temp in range(3):
  tempreture.append(random.randint(min_tempreture, max_tempreture))

for (time_day, temp, index) in zip(day_times, tempreture, uv_index):
     print(f"\rCurrent temperature and uv index in Tehran during day {time_day}: {temp}°C {index}", end="")
     time.sleep(2)
     
print("\nDone displaying all updates.")

while True:
    print('\r{}'.format(time.strftime("%H:%M:%S")), end="")
    time.sleep(1)