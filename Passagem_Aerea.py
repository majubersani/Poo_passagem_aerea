class PassagemAerea:
    def __init__(self, codigo, origem, destino, data_voo, classe="Econômica", status="Em espera"):
        self.codigo = codigo
        self.origem = origem
        self.destino = destino
        self.data_voo = data_voo
        self.classe = classe
        self.status = status

    def mostrar_detalhes(self):
        print(f'Código da Passagem: {self.codigo}')
        print(f'Origem: {self.origem}  Destino: {self.destino}')
        print(f'Data do voo: {self.data_voo}')
        print(f'Classe: {self.classe}')
        print(f'Status: {self.status}')

    def confirmar_passagem(self):
        if self.status == "Em espera":
            self.status = "Confirmada"
            print(f'A passagem {self.codigo} foi confirmada.')
        else:
            print(f'A passagem {self.codigo} não pode ser confirmada.')

    def cancelar_passagem(self):
        self.status = "Cancelada"
        print(f'A passagem {self.codigo} foi cancelada.')


class Passageiro:
    def __init__(self, nome, documento, passagem):
        self.nome = nome
        self.documento = documento
        self.passagem = passagem

    def apresentar(self):
        print(f'Nome: {self.nome}')
        print(f'Documento: {self.documento}')
        self.passagem.mostrar_detalhes()

    def confirmar_passagem(self):
        self.passagem.confirmar_passagem()

    def cancelar_passagem(self):
        self.passagem.cancelar_passagem()


def main():
    passagem1 = PassagemAerea("20112007", "Brasil", "França", "20/10/2025", "Econômica", "Em espera")
    p1 = Passageiro("Majú", "123456789", passagem1)
    p1.apresentar()
    p1.confirmar_passagem()
    print("-" * 50)

    passagem2 = PassagemAerea("19203098", "África do Sul", "Portugal", "12/12/2025", "Primeira Classe", "Em espera")
    p2 = Passageiro("Lorena", "987654321", passagem2)
    p2.apresentar()
    p2.cancelar_passagem()
    print("-" * 50)


class PassagemAerea:
    def __init__(self, codigo, origem, destino, data_voo, classe="Econômica", status="Em espera"):
        self.codigo = codigo
        self.origem = origem
        self.destino = destino
        self.data_voo = data_voo
        self.classe = classe
        self.status = status

    def mostrar_detalhes(self):
        print(f'Código da Passagem: {self.codigo}')
        print(f'Origem: {self.origem}  Destino: {self.destino}')
        print(f'Data do voo: {self.data_voo}')
        print(f'Classe: {self.classe}')
        print(f'Status: {self.status}')

    def confirmar_passagem(self):
        if self.status == "Em espera":
            self.status = "Confirmada"
            print(f'A passagem {self.codigo} foi confirmada.')
        else:
            print(f'A passagem {self.codigo} não pode ser confirmada.')

    def cancelar_passagem(self):
        self.status = "Cancelada"
        print(f'A passagem {self.codigo} foi cancelada.')


class Passageiro:
    def __init__(self, nome, documento, passagem):
        self.nome = nome
        self.documento = documento
        self.passagem = passagem

    def apresentar(self):
        print(f'Nome: {self.nome}')
        print(f'Documento: {self.documento}')
        self.passagem.mostrar_detalhes()

    def confirmar_passagem(self):
        self.passagem.confirmar_passagem()

    def cancelar_passagem(self):
        self.passagem.cancelar_passagem()


def main():
    # Criando passagens aéreas
    passagem1 = PassagemAerea("20112007", "Brasil", "França", "20/10/2025", "Econômica", "Em espera")
    p1 = Passageiro("Majú", "123456789", passagem1)


    p1.apresentar()
    p1.confirmar_passagem()
    print("-" * 50)

    passagem2 = PassagemAerea("19203098", "África do Sul", "Portugal", "12/12/2025", "Primeira Classe", "Cancelada")
    p2 = Passageiro("Lorena", "987654321", passagem2)

    p2.apresentar()
    p2.cancelar_passagem()
    print("-" * 50)

    passagem3 = PassagemAerea("102894228", "Japão", "India", "17/11/2025", "Executiva", "Cancelada")
    p3 = Passageiro("Sophia", "20032013", passagem3)

    p3.apresentar()
    p3.cancelar_passagem()
    print("-" * 50)

if __name__ == "__main__":
    main()