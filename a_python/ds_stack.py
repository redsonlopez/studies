class Pilha:
    """permite a criação de uma pilha"""
    def __init__(self):
        self.itens= []
    def __repr__(self):
        return str(self.itens)
    def empilha(self, valor):
        """adiciona itens a pilha"""
        self.itens.append(valor)
    def desempilha(self):
        assert self.itens, "Erro: pilha vazia."
        # modifica o valor do topo
        return self.itens.pop()

