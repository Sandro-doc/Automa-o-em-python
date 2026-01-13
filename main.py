import pyautogui
import time
import pandas
import pyperclip
#pyautogui.click -> clica
#pyautogui.write -> escreve
#pyautogui.pres -> aperta uma tecla
#pyautogui.hotkey -> aperta uma combinação de teclas

pyautogui.PAUSE = 1
link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

#Passo 1: entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


#copia e cola o link

pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")

# Passo 2: Fazer login
pyautogui.press("enter") # apertar o enter para entrar no link
# Fazer uma pausa para a página carregar
time.sleep(3)

pyautogui.click(x=794, y=398) # clicar no campo de usuário
pyautogui.write("usuarioteste") # escrever o usuário
pyautogui.press("tab") # ir para o campo de senha
pyautogui.write("senhateste") # escrever a senha
pyautogui.press("enter") # apertar o enter para fazer login
time.sleep(5) # esperar a página carregar
# passo 3: Abrir a base de dados
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent
arquivo_csv = BASE_DIR / "produtos.csv"

tabela = pd.read_csv(arquivo_csv)
print(tabela.head())

for linha in tabela.index:

    # Passo 4: Cadastrar 1 produto novo
    pyautogui.click(x=811, y=271) # clicar no botão de novo produto
    #Código do produto
    codigo = str(tabela.loc[linha, "codigo"])
    marca = str(tabela.loc[linha, "marca"])
    tipo = str(tabela.loc[linha, "tipo"])
    categoria = str(tabela.loc[linha, "categoria"])
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    custo = str(tabela.loc[linha, "custo"])  
    obs = str(tabela.loc[linha, "obs"]) 

     #Código do produto
    pyautogui.write(codigo)
    pyautogui.press("tab")#passar para o proximo campo
    #Marca
    pyautogui.write(marca)
    pyautogui.press("tab")#passar para o proximo campo
    #Tipo
    pyautogui.write(tipo)        
    pyautogui.press("tab")#passar para o proximo campo
    #categoria
    pyautogui.write(categoria)
    pyautogui.press("tab")#passar para o proximo campo
    #Preço unitário
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")#passar para o proximo campo
    #Custo
    pyautogui.write(custo)
    pyautogui.press("tab")#passar para o proximo campo
    #Observações
    pyautogui.write(obs)
    pyautogui.press("tab")#passar para o proximo campo      



    #voltar para o inicio da paginha
    pyautogui.scroll(5500)









# Passo 1: entrar no sistema da empresa
# Passo 2: Fazer login
# passo 3: Abrir a base de dados 
# Passo 4: Cadastrar 1 produto novo
# Passo 5: Cadastrar restante dos produtos