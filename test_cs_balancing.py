from cs_balancing import (
    validando_nivel_cs,
    validando_nivel_cliente,
    validando_cs_indisponivel,
    clientes_distribuidos,
    customerSuccessBalancing,
)

def run_tests():
    #Validando níveis de CS
    try:
        validando_nivel_cs([(1, 60), (2, 70)])  # Deve passar
        print("Teste de validação de nível de CS passou!")
    except ValueError as e:
        print(f"Erro na validação de nível de CS: {e}")

    #Validando níveis de cliente
    try:
        validando_nivel_cliente([(101, 30), (102, 50)])  # Deve passar
        print("Teste de validação de nível de cliente passou!")
    except ValueError as e:
        print(f"Erro na validação de nível de cliente: {e}")

    #Validando CSs indisponíveis
    try:
        validando_cs_indisponivel([3], 1)  # Deve passar
        print("Teste de validação de CSs indisponíveis passou!")
    except ValueError as e:
        print(f"Erro na validação de CSs indisponíveis: {e}")

    #Distribuição de clientes
    niveis_cs = [(1, 60), (2, 60)]
    niveis_cliente = [(101, 30), (102, 30), (103, 30)]
    ids_cs_indisponivel = []

    resultado = customerSuccessBalancing(niveis_cs, niveis_cliente, ids_cs_indisponivel)
    
    # Testa se o resultado é um empate
    if len(resultado) > 1:
        print("Empate: dois ou mais CSs atenderam o mesmo número máximo de clientes.")
    elif len(resultado) == 1:
        print(f"O CS que atende mais clientes é: {resultado[0]}")
    else:
        print("Nenhum CS atende clientes.")

run_tests()
