import time
import pyautogui
import pandas as pd
import os

pyautogui.PAUSE = 0.2

# Abrir a janela de execução usando "Win + R"
pyautogui.hotkey('win', 'r')
time.sleep(0.5)  # Pequena pausa para garantir que a janela de execução esteja aberta

# Digitar o comando para abrir o Microsoft Edge e pressionar Enter
pyautogui.write("msedge")
pyautogui.press("enter")

# Aguarde o navegador abrir (ajuste o tempo conforme necessário)
time.sleep(5)

# Digitar a URL e pressionar Enter
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Espera adicional para garantir que a página tenha tempo de carregar
time.sleep(5)

pyautogui.click(x=446, y=283)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("rosemaryaraujorodrigues69@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha senha")
pyautogui.click(x=667, y=406)
time.sleep(5)

# Verificar o diretório atual e a existência do arquivo
print("Diretório atual:", os.getcwd())
print("Conteúdo do diretório:", os.listdir())

# Tentando carregar a tabela
try:
    tabela = pd.read_csv("produtos.csv")
    print(tabela)
    
    # Iterar sobre as linhas do DataFrame e preencher os campos
    for index, row in tabela.iterrows():
        pyautogui.click(x=469, y=200)  # Posicionar no primeiro campo

        pyautogui.write(str(row['codigo']))
        pyautogui.press("tab")
        
        pyautogui.write(str(row['marca']))
        pyautogui.press("tab")
        
        pyautogui.write(str(row['tipo']))
        pyautogui.press("tab")
        
        pyautogui.write(str(row['categoria']))
        pyautogui.press("tab")
        
        pyautogui.write(str(row['preco_unitario']))
        pyautogui.press("tab")
        
        pyautogui.write(str(row['custo']))
        pyautogui.press("tab")
        
        if pd.notna(row['obs']):
            pyautogui.write(str(row['obs']))
        pyautogui.press("tab")
        
        pyautogui.press("enter")
        time.sleep(0.5)  # Pausa para garantir que o produto foi cadastrado antes de prosseguir para o próximo

        # Ajuste o scroll conforme necessário para se adaptar ao layout da página
        pyautogui.scroll(5000)
except FileNotFoundError:
    print("Erro: Arquivo 'produtos.csv' não encontrado.")
except pd.errors.EmptyDataError:
    print("Erro: Arquivo 'produtos.csv' está vazio.")
except pd.errors.ParserError:
    print("Erro: Ocorreu um erro ao analisar o arquivo 'produtos.csv'. Verifique o formato.")
except Exception as e:
    print(f"Erro inesperado: {e}")