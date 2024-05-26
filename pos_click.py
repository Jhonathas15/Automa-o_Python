import pyautogui
from time import sleep

# Antes de tudo é necessário dá uma pequena pausa para deixar o cursor na posição que você quer
# Para isso faça:
sleep(10)
# comando para printar a posição X e Y do cursor
print(pyautogui.position())

# Depois disso só jogar a posição printada no terminal, lá na função PYAUTOGUI.CLICK()
