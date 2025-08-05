import functools
import textwrap
from abc import ABC, abstractmethod
from datetime import date, datetime
from pathlib import Path


class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        # data_atual = date.today().strftime("%d/%m/%Y")
        # transacoes_no_ultimo_dia = [t for t in conta.historico.transacoes if t["data"].startswith(data_atual)]
        # print(transacoes_no_ultimo_dia)

        if not conta.pode_realizar_transacao():
            print("\n@@@ Você excedeu o limite de 10 transações diárias @@@")
            return

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        super().__init__(endereco)

    # representação do objeto usado em logs
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ({self.cpf})>"


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self, tipo_operacao: None):
        match (tipo_operacao):
            case "Saque":
                for saque in self.transacoes:
                    if saque["tipo"] == Saque.__name__:
                        yield saque
            case "Deposito":
                for deposito in self.transacoes:
                    if deposito["tipo"] == Deposito.__name__:
                        yield deposito
            case None:
                for transacao in self.transacoes:
                    yield transacao


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._cliente = cliente
        self._agencia = "0001"
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def agencia(self):
        return self._agencia

    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero=numero, cliente=cliente)

    def sacar(self, valor):
        if self._saldo > valor:
            if valor > 0:
                self._saldo -= valor
                print("\n=== Saque realizado com sucesso! ===")
                return True
            else:
                print(
                    "\n@@@ Operação falhou! O valor informado deve ser maior que 0. @@@"
                )
                return False
        else:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado deve ser maior que 0. @@@")
            return False

    def pode_realizar_transacao(self):
        hoje = date.today().strftime("%d/%m/%Y")
        transacoes_do_dia = [
            t for t in self.historico.transacoes if t["data"].startswith(hoje)
        ]
        return len(transacoes_do_dia) < 10


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        # historico armazena transacoes -> transacoes podem ser depositos/saques -> aqui, verificamos se o tioi é saque
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == "Saque"
            ]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques > self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            # se tudo der certo, chama o método sacar da classe-pai (Conta)
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            Saldo:\t{self.saldo:.2f}
        """

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"


ROOT_PATH = Path(__file__).parent


# DESAFIO DECORADOR + DESAFIO ARQUIVO
def log_operacao(funcao):
    @functools.wraps(funcao)
    def wrapper(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        nome_operacao = funcao.__name__
        try:
            with open(ROOT_PATH / "log.txt", "a", encoding="utf-8") as arquivo:
                arquivo.writelines(
                    f"[{data_hora}] Função '{nome_operacao}' executada com "
                    f"argumentos {args} e {kwargs}. Retornou {resultado}\n"
                )
        except IOError as ex:
            print(f"Erro ao abrir arquivo: {ex}")

        print("\n========== REGISTRO DE LOG ==========")
        print(f"Data operação: {data_hora} - Nome: {nome_operacao}")

    return wrapper


# DESAFIO GERADOR
def gerador_relatorio(transacoes, filtro=0):
    print("========== RELATÓRIO ==========")
    match (filtro):
        case 1:
            saques = [
                transacao
                for transacao in transacoes
                if transacao["tipo"] == Saque.__name__
            ]
            for saque in saques:
                yield saque
        case 2:
            deposito = [
                transacao
                for transacao in transacoes
                if transacao["tipo"] == Deposito.__name__
            ]
            for deposito in deposito:
                yield deposito
        case 0:
            for transacao in transacoes:
                yield transacao
        case _:
            for transacao in transacoes:
                yield transacao


# DESAFIO ITERADOR
class Contalterador:
    def __init__(self, contas: list[Conta]):
        self.contas = contas
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self.contador]
            self.contador += 1
            return (
                "Não há contas para processar"
                if not self.contas
                else f"""\
                Agência:\t{conta.agencia}
                C/C:\t\t{conta.numero}
                Titular:\t{conta.cliente.nome}
                Saldo:\t{conta.saldo:.2f}
                """
            )
        except IndexError:
            raise StopIteration


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [gr]\tGerar relatório
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    # Se encontrar, retorna o elemento na 1° posição (pois nao existem dois clientes com o mesmo CPF)
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: escolhe a primeira conta do cliente
    numero = int(input("Informe o n° da conta: "))
    conta_filtrada = [conta for conta in cliente.contas if conta.numero == numero]
    conta = conta_filtrada[0] if conta_filtrada else None

    if not conta:
        print("\n@@@ Conta não encontrada! @@@")
        return

    return conta


@log_operacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return  # Retorna para o main

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    cliente.realizar_transacao(conta=conta, transacao=transacao)


@log_operacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f} \t{transacao['data']}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco
    )

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


@log_operacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)  # Adiciona a conta na lista de contas
    cliente.contas.append(conta)  # Adiciona a conta na lista de contas do cliente

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    for conta in Contalterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def gerar_relatorio(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    filtro = int(
        input(
            "Qual o filtro do relatório?\n0 - Todas operações\n1 - Somente saques\n2 - Somente depósitos\n =>"
        )
    )

    for i in gerador_relatorio(transacoes=conta.historico.transacoes, filtro=filtro):
        print(i)


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        match (opcao):
            case "d":
                depositar(clientes)
            case "s":
                sacar(clientes)
            case "e":
                exibir_extrato(clientes)
            case "nu":
                criar_cliente(clientes)
            case "nc":
                numero_conta = len(contas) + 1
                criar_conta(numero_conta, clientes, contas)
            case "lc":
                listar_contas(contas)
            case "gr":
                gerar_relatorio(clientes)
            case "q":
                print("\n===Programa encerrado! ===")
                break
            case _:
                print("\n@@@Opção inválida! @@@")


main()
