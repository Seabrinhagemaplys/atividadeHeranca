from funcionario import Funcionario

class Assalariado(Funcionario):
    def __init__(self, valor: float, meses: int):
        super().__init__()
        self.valor = valor
        self.meses = meses

    def pagamentosAssalariados(self):
        diasTrabalhados: int = self.valor*self.meses
        print(f"O numero total de dias trabalhados foi de {diasTrabalhados} dias")
