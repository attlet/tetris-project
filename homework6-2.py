import threading
import time
class calc:
    sum = 0
    value = 0
    def __init__(self,value1):
        self.value = value1
        while self.value > 0:
            self.sum += self.value
            self.value = self.value - 1

    def result(self):
        print(self.sum)
        time.sleep(0.2)


cal1 = calc(1000)
cal2 = calc(100000)
cal3 = calc(10000000)

th1 = threading.Thread(target = cal1.result)
th2 = threading.Thread(target = cal2.result)
th3 = threading.Thread(target = cal3.result)

th1.start()
th2.start()
th3.start()