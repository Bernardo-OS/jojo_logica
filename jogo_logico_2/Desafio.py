class Desafio(object):
    def __init__(self, numero, pistas, sequencia):
        self.numero = numero
        self.pistas = pistas
        self.sequencia = sequencia

    def __str__(self):
        return f"Desafio: {self.numero}, Pistas: {self.pistas}, Sequencia: {self.sequencia}"

    def ler_arquivo_csv(self, caminho_arquivo):
        desafios = []
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) >= 3:
                    numero = partes[0].strip()
                    pistas = partes[1].strip()
                    sequencia = [p.strip() for p in partes[2:]]
                    desafios.append(Desafio(numero, pistas, sequencia))
        return desafios
    
    def dividir_fios(self, sequencia):
        return [fio.strip() for fio in sequencia.split(",")]

    def obter_desafio_por_numero(self, numero):
        desafios = self.ler_arquivo_csv("desafios.csv")
        for desafio in desafios:
            if desafio.numero == numero:
                return desafio
        print(f"Nenhum registro encontrado para o número {numero}.")
        return None