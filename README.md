# Estruturas de Dados em Python

Este projeto implementa três estruturas de dados clássicas usando Python: Pilha, Fila e Lista Duplamente Encadeada. Além disso, há uma classe principal para interagir com o usuário e testar as funcionalidades dessas estruturas.

## Estruturas de Dados Implementadas

1. **No (Nodo)**: Classe que representa um nó, elemento básico das estruturas de dados, contendo um valor inteiro e referências para o próximo e o anterior elementos.

2. **Pilha**: Classe que implementa a estrutura de dados do tipo Pilha, seguindo a estratégia LIFO (Last In, First Out).

3. **Fila**: Classe que implementa a estrutura de dados do tipo Fila, seguindo a estratégia FIFO (First In, First Out).

4. **Lista**: Classe que implementa uma Lista Duplamente Encadeada, permitindo inserções e remoções em qualquer posição.

## Como Executar

1. **Pré-requisitos**: Certifique-se de ter o Python instalado na sua máquina.

2. **Download**: Baixe o arquivo `estruturas_dados_atualizado.py`.

3. **Execução**: Execute o script Python através do terminal ou de um ambiente de desenvolvimento (IDE).

    ```sh
    python estruturas_dados_atualizado.py
    ```

4. **Interação**: Siga as instruções do menu para inserir, remover e visualizar elementos nas diferentes estruturas de dados.

## Menu de Opções

O programa apresenta um menu interativo com as seguintes opções:

1. Inserir na Pilha
2. Remover da Pilha
3. Mostrar Pilha
4. Inserir na Fila
5. Remover da Fila
6. Mostrar Fila
7. Inserir na Lista
8. Remover da Lista
9. Mostrar Lista
0. Sair

Após escolher a opção desejada, siga as instruções fornecidas pelo programa para manipular as estruturas de dados.

## Valores Restantes

Ao final da execução do programa, os valores restantes em cada estrutura de dados serão exibidos:

- Pilha
- Fila
- Lista

## Estrutura do Código

### Classe `No`
Classe básica que representa um nó com um valor inteiro e referências para o próximo e o anterior nós.

### Classe `Pilha`
Implementa uma pilha utilizando a estratégia LIFO. Métodos principais:
- `push(valor)`: Insere um valor no topo da pilha.
- `pop()`: Remove e retorna o valor do topo da pilha.
- `peek()`: Retorna o valor do topo da pilha sem removê-lo.
- `is_empty()`: Verifica se a pilha está vazia.
- `__str__()`: Retorna uma representação em string da pilha.

### Classe `Fila`
Implementa uma fila utilizando a estratégia FIFO. Métodos principais:
- `enqueue(valor)`: Insere um valor no fim da fila.
- `dequeue()`: Remove e retorna o valor do início da fila.
- `is_empty()`: Verifica se a fila está vazia.
- `__str__()`: Retorna uma representação em string da fila.

### Classe `Lista`
Implementa uma lista duplamente encadeada. Métodos principais:
- `append(valor)`: Insere um valor no fim da lista.
- `remove(valor)`: Remove o valor especificado da lista.
- `is_empty()`: Verifica se a lista está vazia.
- `__str__()`: Retorna uma representação em string da lista.

### Classe `Principal`
Classe responsável por interagir com o usuário, oferecendo um menu para testar as funcionalidades das estruturas de dados. No final da execução, exibe os valores restantes em cada estrutura.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias ou correções.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.
