# Importando a biblioteca PYAUTOGUI
import pyautogui

# Importando a função SLEEP da biblioteca TIME
from time import sleep

# Abrindo janela do windows
pyautogui.press('win')

# Pequena pausa para ñ ter erros
sleep(0.3)

# Comando para escrever algo, no meu caso watssap
pyautogui.write('watssap')

# comando para pressionar uma tecla, no meu caso enter
pyautogui.press('enter')

# Pequena pausa para ñ ter erros
sleep(2)

# Comando para escrever algo, no meu caso Eu
pyautogui.write('Eu')
pyautogui.press('enter')

# Pequena pausa para ñ ter erros
sleep(0.5)

# Comando para dar um click de mouse
pyautogui.click(x=238, y=232)

# Pequena pausa para ñ ter erros
sleep(1)

pyautogui.write('Deu certo rapaz. tua vez de tentar!!')
pyautogui.press('enter')

