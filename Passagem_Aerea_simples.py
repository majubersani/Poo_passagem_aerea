class PassagemAerea:
    def __init__(self, codigo, passageiro, origem, destino, data_voo, classe="Econômica", status="Em espera"):
        self.codigo = codigo
        self.passageiro = passageiro
        self.origem = origem
        self.destino = destino
        self.data_voo = data_voo
        self.classe = classe
        self.status = status

    def mostrar_detalhes(self):
        print(f'Código da Passagem: {self.codigo}')
        print(f'Passageiro: {self.passageiro}')
        print(f'Origem: {self.origem} | Destino: {self.destino}')
        print(f'Data do voo: {self.data_voo}')
        print(f'Classe: {self.classe}')
        print(f'Status: {self.status}')
        print("-" * 20)

    def confirmar_passagem(self):
        self.status = "Confirmada"
        print(f'A passagem {self.codigo} de {self.passageiro} foi confirmada.')

    def cancelar_passagem(self):
        self.status = "Cancelada"
        print(f'A passagem {self.codigo} de {self.passageiro} foi cancelada.')

    def atualizar_status(self, novo_status):
        self.status = novo_status
        print(f'O status da passagem {self.codigo} foi atualizado para: {self.status}')
        print("-" * 20)

#p1 = passagem
p1 = PassagemAerea("58692", "Maria Júlia Bersani", "Paraguai", "Argentina", "02/11/2025")
p2 = PassagemAerea("254785", "Luciano", "Russia", "Bélgica", "24/12/25", classe="Executiva")
p3 = PassagemAerea("132456", "Lucas", "Taiwan", "Australia", "12/09/2025", classe="Primeira classe", status="Confirmada")

p1.mostrar_detalhes()
p2.mostrar_detalhes()
p3.mostrar_detalhes()

p1.confirmar_passagem()
p2.cancelar_passagem()
p3.atualizar_status("Em andamento")
