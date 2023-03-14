# importando o pyautogui
import pyautogui
# controlar o tempo das funções
import time
# biblioteca de manipulação de tabelas
import pandas as pd

import pyperclip

# pausa a cada ação do script
pyautogui.PAUSE = 1

# abrindo o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# abrindo nova guia e abrindo o link
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

# delay para a página carregar
time.sleep(3)

# achar a coordenada do mouse: print(pyautogui.position())
# levar o cursor do mouse até o local requerido
pyautogui.click(x=973, y=426)
# escrever o login
pyautogui.write("meu_login")
# levar o cursor do mouse até o local requerido
pyautogui.click(x=935, y=521)
# escrever a senha
pyautogui.write("minha_senha")
# logar no site
pyautogui.click(x=971, y=601)

# delay para a página carregar
time.sleep(3)

# exportar base de dados
pyautogui.click(x=510, y=330)
# clicar no menu
pyautogui.click(x=1661, y=198)
# faz o download
pyautogui.click(x=1485, y=623)

# delay para a página carregar
time.sleep(5)

# endereço da tabela baixada
tabela = pd.read_csv(r"C:\Users\mtsfs\Downloads\Compras.csv", sep=";")
# exibe a tabela
print(tabela)

# fazer as somas das colunas
total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
# cálculo de preço médio
preco_medio = total_gasto / quantidade

print("total_gasto")
print("quantidade")
print("preco_medio")


# abrindo nova guia e abrindo o email
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/?ogbl#inbox")
pyautogui.press("enter")

# delay para a página carregar
time.sleep(3)

# clica no botão escrever
pyautogui.click(x=135, y=240)
# escrever o destinatário
pyautogui.write("kenaa@example.com")
# confirma o destinatário
pyautogui.press("tab")

# passar para o campo assunto
pyautogui.press("tab")
# escrever o assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")

# passar para o corpo do email
pyautogui.press("tab")
# escrever o corpo do email

texto = f"""
Prezados, 
Segue o relatório de compras.

Total gasto: {total_gasto:,.2f}
Quantidade de produtos: {quantidade:,}
Preço médio: {preco_medio:,.2f}

Estou a disposição para quaisquer dúvidas.

Atenciosamente,
Marco Túlio Salvador Filho
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# enviar o email
pyautogui.hotkey("ctrl", "enter")