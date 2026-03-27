from funcionario import Funcionario

class Horista(Funcionario):
    def __init__(self, valor: float, horas: int):
        super().__init__()
        self.valor = valor
        self.horas = horas

    def pagamentosHoristas(self):
        horasTrabalhadas: float = self.valor*self.horas
        print(f"O numero total de horas trabalhadas foi de {horasTrabalhadas} horas")
