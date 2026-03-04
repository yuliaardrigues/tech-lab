# abrir o navegador 
# entrar no sistema da empresa

# fazer login
# abrir a base de dados 
# cadastrar um produto
# repetir o passo ate a lista acabar  



import pyautogui
import time
import pandas as pd
import openpyxl


link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('brave')
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(2)

pyautogui.click(x=278, y=384) # clicar no campo de email

pyautogui.write('rodriguesyulia@gmail.com') # escrever o email

# clicar no campo de senha
pyautogui.press('tab')
pyautogui.write('123456') # escrever a senha

pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(3)

tabela = pd.read_csv('produtos.csv')

#clicar produto e cadastrar produto
for linha in tabela.index:

    pyautogui.click(x=356, y=282) 
    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != "nan":
      pyautogui.write(obs)
    pyautogui.press('tab') 
    
    pyautogui.press('enter')
    pyautogui.scroll(5000)

