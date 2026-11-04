class PilhaAlertas:
    """
    Estrutura de dados Pilha para auditoria de alertas de colisão críticos.
    Maneja eventos de risco no formato LIFO (Last-In, First-Out).
    """
    def __init__(self):
        self._pilha = []

    def push(self, alerta):
        """Empilha um novo alerta de colisão no topo da pilha."""
        self._pilha.append(alerta)

    def pop(self):
        """
        Remove e retorna o alerta mais recente (topo da pilha).
        Retorna None se a pilha estiver vazia.
        """
        if self.is_empty():
            return None
        return self._pilha.pop()

    def peek(self):
        """Retorna o alerta do topo sem removê-lo."""
        if self.is_empty():
            return None
        return self._pilha[-1]

    def is_empty(self):
        """Verifica se a pilha está vazia."""
        return len(self._pilha) == 0

    def size(self):
        """Retorna a quantidade de alertas pendentes na pilha."""
        return len(self._pilha)

    def listar_alertas(self):
        """Retorna uma cópia dos alertas da pilha (do topo para a base)."""
        return self._pilha[::-1]
