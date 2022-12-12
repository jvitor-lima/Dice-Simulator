import random
import PySimpleGUI as tela


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        self.layout = [
            [tela.Text('Deseja jogar o dado?')],
            [tela.Button('Sim'), tela.Button('Não')]
        ]

    def Iniciar(self):
        self.janela = tela.Window('Simulador de Dado', layout=self.layout)
        self.eventos, self.valores = self.janela.Read()

        try:
            if self.eventos == 'Sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Agrecemos a sua participação!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print('o valor do dado é: ',random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()