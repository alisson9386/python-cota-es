import requests

from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto
    

janela = Tk()
janela.title("Cotação Atual das Moedas")
janela.geometry("400x200")
janela.configure(background="MIDNIGHTBLUE")
janela.resizable(width=False, height=False)
janela.attributes("-alpha",0.9)


texto_orientacao = Label(janela, text="Clique no botão para visualizar as cotações das moedas em tempo real!", bg="MIDNIGHTBLUE", fg="white")
texto_orientacao.grid(column=0,row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar cotações Dólar/Euro/BTC", command=pegar_cotacoes, bg="MIDNIGHTBLUE", fg="white")
botao.grid(column=0,row=1, padx=10, pady=10)

texto_cotacoes = Label(janela, text="Cotação não solicitada", bg="MIDNIGHTBLUE", fg="white")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()

