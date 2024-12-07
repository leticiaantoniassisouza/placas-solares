class ColunaSolar:
    def __init__(self, id_coluna, energia_produzida, eficiencia):
        self.id_coluna = id_coluna  # Identificador único da coluna
        self.energia_produzida = energia_produzida  # Energia produzida pela coluna
        self.eficiencia = eficiencia  # Eficiencia de produção da coluna solar (0 a 100%)

    def verificar_energia(self):
        """Verifica se a coluna está produzindo energia dentro da faixa necessária"""
        if self.energia_produzida >= 100:  # Exemplo de limite para energia produzida
            return True
        return False

    def verificar_ineficiencia(self):
        """Verifica se a coluna está com baixa eficiência de produção de energia"""
        if self.eficiencia < 75:  # Limite de eficiência considerado baixo
            return True
        return False

    def ajustar_energia(self, nova_energia):
        """Ajusta a energia produzida pela coluna solar"""
        self.energia_produzida = nova_energia

    def ajustar_eficiencia(self, nova_eficiencia):
        """Ajusta a eficiência da coluna solar"""
        self.eficiencia = nova_eficiencia


class SistemaSolar:
    def __init__(self):
        self.colunas = []  # Lista de colunas solares no sistema

    def adicionar_coluna(self, coluna):
        """Adiciona uma nova coluna solar ao sistema"""
        self.colunas.append(coluna)

    def verificar_sistema(self):
        """Verifica a situação de todas as colunas solares no sistema"""
        for coluna in self.colunas:
            if coluna.verificar_energia() and not coluna.verificar_ineficiencia():
                print(f"Coluna {coluna.id_coluna} está funcionando corretamente.")
            else:
                if coluna.verificar_ineficiencia():
                    print(f"Coluna {coluna.id_coluna} está com baixa eficiência.")
                if not coluna.verificar_energia():
                    print(f"Coluna {coluna.id_coluna} não está produzindo energia suficiente.")

    def ajustar_coluna(self, id_coluna, nova_energia=None, nova_eficiencia=None):
        """Ajusta as características de uma coluna específica"""
        for coluna in self.colunas:
            if coluna.id_coluna == id_coluna:
                if nova_energia is not None:
                    coluna.ajustar_energia(nova_energia)
                if nova_eficiencia is not None:
                    coluna.ajustar_eficiencia(nova_eficiencia)
                print(f"Coluna {id_coluna} ajustada com sucesso.")
                return
        print(f"Coluna com ID {id_coluna} não encontrada no sistema.")

# Exemplo de uso
if __name__ == "__main__":
    # Criando o sistema solar
    sistema = SistemaSolar()

    # Adicionando colunas solares
    coluna1 = ColunaSolar(id_coluna=1, energia_produzida=120, eficiencia=80)
    coluna2 = ColunaSolar(id_coluna=2, energia_produzida=90, eficiencia=60)
    sistema.adicionar_coluna(coluna1)
    sistema.adicionar_coluna(coluna2)

    # Verificando o sistema
    sistema.verificar_sistema()

    # Ajustando a energia de uma coluna
    sistema.ajustar_coluna(id_coluna=2, nova_energia=110, nova_eficiencia=85)

    # Verificando o sistema novamente
    sistema.verificar_sistema()
