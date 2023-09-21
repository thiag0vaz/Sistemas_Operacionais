import threading
import time

def mostrar_numeros(thread_id):
    for i in range(1, 6):
        print(f"Thread {thread_id}: {i}")
        time.sleep(1)

thread1 = threading.Thread(target=mostrar_numeros, args=(1,))
thread2 = threading.Thread(target=mostrar_numeros, args=(2,))
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Programa concluído.")
