import time
from pynput.keyboard import Key, Controller
keyboard = Controller()

#3Bixx!

while True:
    try:
        last_num = int(input("Last number: "))
        break
    except:
        print("Try a number")

while True:
    try:
        num_count = int(input("Number count: "))
        break
    except:
        print("Try a number")

remaining = 0
times_ran = 0
print("you have 3 seconds to click on the chat ")
time.sleep(3)

for _ in range(num_count):
    last_num += 1
    time.sleep(1)

    for char in str(last_num):
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)
        times_ran += 1

        if times_ran == len(str(last_num)):
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            remaining += 1
            times_ran = 0
            print(str(last_num) + " | " + str(int(num_count) - remaining) + " remaining")

print("\n finished")
exit()
