class No:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None

    def __str__(self):
        return str(self.valor)

class Pilha:
    def __init__(self):
        self.topo = None

    def push(self, valor):
        novo_no = No(valor)
        if self.topo is not None:
            novo_no.proximo = self.topo
        self.topo = novo_no

    def pop(self):
        if self.topo is None:
            return None
        valor = self.topo.valor
        self.topo = self.topo.proximo
        return valor

    def peek(self):
        if self.topo is None:
            return None
        return self.topo.valor

    def is_empty(self):
        return self.topo is None

    def __str__(self):
        valores = []
        atual = self.topo
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.proximo
        return ' -> '.join(valores)

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enqueue(self, valor):
        novo_no = No(valor)
        if self.fim is not None:
            self.fim.proximo = novo_no
        self.fim = novo_no
        if self.inicio is None:
            self.inicio = novo_no

    def dequeue(self):
        if self.inicio is None:
            return None
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        return valor

    def is_empty(self):
        return self.inicio is None

    def __str__(self):
        valores = []
        atual = self.inicio
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.proximo
        return ' -> '.join(valores)

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def append(self, valor):
        novo_no = No(valor)
        if self.fim is not None:
            self.fim.proximo = novo_no
            novo_no.anterior = self.fim
        self.fim = novo_no
        if self.inicio is None:
            self.inicio = novo_no

    def remove(self, valor):
        atual = self.inicio
        while atual is not None:
            if atual.valor == valor:
                if atual.anterior is not None:
                    atual.anterior.proximo = atual.proximo
                if atual.proximo is not None:
                    atual.proximo.anterior = atual.anterior
                if atual == self.inicio:
                    self.inicio = atual.proximo
                if atual == self.fim:
                    self.fim = atual.anterior
                return True
            atual = atual.proximo
        return False

    def is_empty(self):
        return self.inicio is None

    def __str__(self):
        valores = []
        atual = self.inicio
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.proximo
        return ' <-> '.join(valores)

class Principal:
    def __init__(self):
        self.pilha = Pilha()
        self.fila = Fila()
        self.lista = Lista()

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Inserir na Pilha")
            print("2. Remover da Pilha")
            print("3. Mostrar Pilha")
            print("4. Inserir na Fila")
            print("5. Remover da Fila")
            print("6. Mostrar Fila")
            print("7. Inserir na Lista")
            print("8. Remover da Lista")
            print("9. Mostrar Lista")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                valor = int(input("Digite um valor: "))
                self.pilha.push(valor)
            elif opcao == '2':
                print(f"Valor removido da pilha: {self.pilha.pop()}")
            elif opcao == '3':
                print(f"Pilha: {self.pilha}")
            elif opcao == '4':
                valor = int(input("Digite um valor: "))
                self.fila.enqueue(valor)
            elif opcao == '5':
                print(f"Valor removido da fila: {self.fila.dequeue()}")
            elif opcao == '6':
                print(f"Fila: {self.fila}")
            elif opcao == '7':
                valor = int(input("Digite um valor: "))
                self.lista.append(valor)
            elif opcao == '8':
                valor = int(input("Digite um valor para remover: "))
                if self.lista.remove(valor):
                    print(f"Valor {valor} removido da lista.")
                else:
                    print(f"Valor {valor} não encontrado na lista.")
            elif opcao == '9':
                print(f"Lista: {self.lista}")
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

        print("\nValores restantes nas estruturas:")
        print(f"Pilha: {self.pilha}")
        print(f"Fila: {self.fila}")
        print(f"Lista: {self.lista}")

if __name__ == "__main__":
    programa = Principal()
    programa.menu()