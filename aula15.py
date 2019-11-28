class Carro:
    # isso é uma classe - forma do bolo
    def __init__(self, proprietario, modelo, cor, placa, valor, marca):
        # init é um magic methodo e self é a referencia dos atributos
        self.proprietario = proprietario
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.valor = valor
        self.marca = marca

    def __str__(self):
        return f"Olá {self.proprietario}, seu carro é o {self.modelo} - {self.marca}"
# até aqui é um método pois está dentro de uma class e se não estivesse seria uma função mesmo
meu_carro = Carro(
    proprietario = 'josé',
    modelo = 'Siena',
    cor = 'Laranja',
    placa = 'TOP-5555',
    valor = 2000,
    marca = 'Fiat'
)
# uma função que recebe um objeto do tipo carro
print(meu_carro)
