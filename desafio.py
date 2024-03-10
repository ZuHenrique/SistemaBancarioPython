# SISTEMA BANCÁRIO COM PYTHON

# Variáveis iniciais
saldo = 0.0
limite = 500.0
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    """Realiza um depósito no saldo da conta."""
    global saldo
    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")

def sacar(valor):
    """Realiza um saque no saldo da conta se possível."""
    global saldo, numero_saques, limite
    if valor > saldo:
        return "Falha: Saldo insuficiente."
    if valor > limite:
        return "Falha: Valor excede o limite para saque."
    if numero_saques >= LIMITE_SAQUES:
        return "Falha: Número máximo de saques alcançado."
    
    saldo -= valor
    extrato.append(f"Saque: R$ {valor:.2f}")
    numero_saques += 1
    return "Saque efetuado com sucesso."

def imprimir_extrato():
    """Imprime o extrato da conta com os movimentos e o saldo."""
    print("\n================ EXTRATO ================")
    for movimentacao in extrato:
        print(movimentacao)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print(f"Número de saques realizados: {numero_saques}")
    print("==========================================")

def validar_valor(valor):
    """Valida se o valor informado é um número positivo."""
    try:
        valor = float(valor)
        if valor <= 0:
            raise ValueError("O valor deve ser positivo.")
        return valor, None
    except ValueError as ve:
        return None, ve

def operacoes_bancarias():
    """Menu principal de operações bancárias da conta."""
    opcoes = {
        "d": (depositar, "Depósito"),
        "s": (sacar, "Saque"),
        "e": (imprimir_extrato, None),
        "q": (None, None)
    }
    
    while True:
        print("\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair")
        opcao = input("Selecione a operação desejada: ").lower()
        if opcao in opcoes:
            acao, nome_operacao = opcoes[opcao]
            if acao:
                if nome_operacao:
                    valor_input = input(f"Informe o valor do {nome_operacao}: ")
                    valor, erro = validar_valor(valor_input)
                    if erro:
                        print(f"Operação falhou! {erro}")
                    else:
                        resultado = acao(valor)
                        if resultado:
                            print(resultado)
                else:
                    acao()
        elif opcao == "q":
            print("Sessão encerrada.")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executa as operações bancárias
if __name__ == "__main__":
    operacoes_bancarias()