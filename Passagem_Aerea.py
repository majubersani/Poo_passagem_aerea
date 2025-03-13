class Passagem:
    def __init__(self, codigo, origem, destino, data_voo, classe, status, preco_passagem):
        self.__codigo = codigo
        self._origem = origem
        self.__destino = destino
        self.__data_voo = data_voo
        self._classe = classe
        self.__status = status
        self.__preco_passagem = preco_passagem

    def get_codigo(self):
        return self.__codigo

    def get_origem(self):
        return self._origem

    def get_destino(self):
        return self.__destino

    def get_data_voo(self):
        return self.__data_voo

    def get_classe(self):
        return self._classe

    def get_status(self):
        return self.__status

    def get_preco_passagem(self):
        return self.__preco_passagem

    def apresentar(self):
        print(f'Passagem Código: {self.get_codigo()}')
        print(f'Origem: {self.get_origem()}, Destino: {self.get_destino()}')
        print(f'Data do Voo: {self.get_data_voo()}, Classe: {self.get_classe()}')
        print(f'Status: {self.get_status()}, Preço: {self.get_preco_passagem()}')

    def set_status(self, novo_status):
        self.__status = novo_status
        print(f'Status atualizado para: {novo_status}')

    def set_preco_passagem(self, valor):
        if valor >= 0:
            self.__preco_passagem = valor
        else:
            print("O preço deve ser positivo")


class PassagemAerea(Passagem):
    def __init__(self, nome, idade, codigo, origem, destino, data_voo, classe, status, preco_passagem):
        super().__init__(codigo, origem, destino, data_voo, classe, status, preco_passagem)
        self.__nome = nome
        self.__idade = idade
        self._bagagem = False
        self.checkin = False

    def apresentar(self):
        super().apresentar()
        print(f'Passageiro: {self.__nome}, Idade: {self.__idade}')
        print(f'Bagagem Despachada: {self._bagagem}')
        print(f'Check-in Realizado: {self.checkin}')

    def set_bagagem(self, status):
        if self._bagagem and status:
            print("A bagagem já foi despachada")
        elif not self._bagagem and not status:
            print("A bagagem não foi despachada")
        else:
            self._bagagem = status
            print("Bagagem despachada com sucesso"
        if status else "Bagagem retirada")

    def set_checkin(self, status):
        if self.checkin and status:
            print("O check-in já foi realizado")
        elif not self.checkin and not status:
            print("O check-in ainda não foi feito")
        else:
            self.checkin = status
            print("Check-in realizado com sucesso"
        if status else "Check-in cancelado")


passagem1 = PassagemAerea("Carlos Silva", 35, "12345", "Rio de Janeiro", "São Paulo", "2025-06-15", "Econômica", "Confirmado", "R$ 500,00")
passagem1.apresentar()
passagem1.set_bagagem(True)
passagem1.set_checkin(True)
print("-" * 40)
passagem2 = PassagemAerea("Ana Souza", 28, "67890", "São Paulo", "Paris", "2025-07-20", "Primeira Classe", "Pendente", "R$ 3000,00")
passagem2.apresentar()
passagem2.set_bagagem(True)
passagem2.set_checkin(True)
passagem2.set_status("Confirmado")
b