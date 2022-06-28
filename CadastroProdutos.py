from selenium import webdriver
from selenium.webdriver.common.by import By
import PySimpleGUI as sg
from time import sleep

CadastroProdutos = []  # onde vai ficar armazenado as informações para cadastro
ListaTipos = sorted(('Hi-Wall', 'Piso Teto', 'Cassete', 'Mult-Split'))
ListaMarcas = sorted(('Midea', 'Carrier', 'Springer', 'Komeco'))
ListaPecas = sorted(('Placa', 'Display', 'Turbina', 'Filtro', 'Coxim', 'Vane Horizontal', 'Vane Vertical',
                     'Placa Condensadora', 'Base Condensadora', 'Tirante Lateral', 'Serpentina Evaporadora',
                     'Serpentina Condensadora', 'Motor Vane', 'Lateral Direita', 'Lateral Esquerda',
                     'Painel Frontal', 'Chassi', 'Tansformador', 'Relé'))


class Layout:
    def __init__(self):
        sg.theme('Dark Grey 13')
        modelo = [[sg.Text('Modelo', size=(13, 0)), sg.Input(key='modelo', size=(20, 0))],
                  [sg.Text('Capacidade', size=(13, 0)), sg.Input(key='capacidade', size=(20, 0))],
                  [sg.Text('Ciclo', size=(13, 0))],
                  [sg.Radio('Quente/Frio', 'ciclo', key='quente_frio'), sg.Radio('Frio', 'ciclo', key='frio')],
                  [sg.Text('Peça', size=(13, 0)), sg.Combo(ListaPecas, size=(18, 10), key='peca')],
                  [sg.Text('Marca', size=(13, 0)), sg.Combo(ListaMarcas, size=(18, 10), key='marca')],
                  [sg.Text('Tipo', size=(13, 0)), sg.Combo(ListaTipos, size=(18, 10), key='tipo')],
                  [sg.Text('SubMarca', size=(13, 0)), sg.Input(key='submarca', size=(20, 0))],
                  [sg.Text('Cod. Interno', size=(13, 0)), sg.Input(key='cod. interno', size=(20, 0))],
                  [sg.Text('Cod. Fabrica', size=(13, 0)), sg.Input(key='cod. fabrica', size=(20, 0))],
                  [sg.Text('Valor da peça', size=(13, 0)), sg.Input(key='valor da peça', size=(20, 0))],
                  [sg.Submit()]]
        self.window = sg.Window('Cadastro Automático de Peças', modelo)

    def iniciar(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            CadastroProdutos.append(values.copy())  # armazenar as informações no dicionario
        self.window.close()


layout = Layout()
layout.iniciar()


def procedimento_abrir_anuncio(codigo_interno, modelo):
    driver = webdriver.Chrome()
    # colocar o URL do produto
    driver.get(f"https://app.lojaintegrada.com.br/painel/catalogo/produto/buscar?q="
                    f"{codigo_interno}-{modelo}&listagem=alfabetica&filtro=")


for produto in CadastroProdutos:
    sleep(1)
    procedimento_abrir_anuncio(produto['cod. interno'], produto['modelo'])
    input()

    # colocar o SKU
    # preço de venda
    # descrição completa
    # tag title
    # meta tag description
    # meta tag keyword
    # peso
    # altura
    # largura
    # profundidade
    # gerenciar estoque do produto
    # disponibilidade para 1 dia util
    # tornar o produto indisponivel
    # salvar alterações
