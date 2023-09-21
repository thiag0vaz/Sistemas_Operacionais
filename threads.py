import threading
import time

def tchau():
    frases = [
        " Tchau coração!",
        " Até mais BB!",
        " Fica bem nenem!",
        " Já estou com saudades!",
        " Volte sempre!",
        " A - D - E - U - S | Ande direito enquanto usa sandalha",
        " Até logo!",
        " Ande pela sombra!",
        " Tenha um ótimo dia!",
        " Vá correr!",
    ]
    for frase in frases:
        print(frase)
        time.sleep(1.1)  

def numeros():
    numeros = ["1-", "2-", "3-", "4-", "5-", "6-", "7-", "8-", "9-", "10-"]
    for numero in numeros:
        print(numero)
        time.sleep(1)  

thread1 = threading.Thread(target=numeros)
thread2 = threading.Thread(target=tchau)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Programa concluído.")
