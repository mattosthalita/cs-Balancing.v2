# Sistema de Balanceamento entre Clientes e Customer Success

O arquivo `cs_balancing.py` contém um sistema de balanceamento entre clientes e Customer Success (CS). Os CSs são os Gerentes de Sucesso, responsáveis pelo acompanhamento estratégico dos clientes. A saída do sistema é o ID do CS que atende a mais clientes.

## Limitações

- Todos os CSs têm níveis diferentes.
- Não há limite de clientes por CS.
- Clientes podem ficar sem serem atendidos.
- Clientes podem ter o mesmo tamanho.

### Regras de Validação

- \(0 < n < 1.000\) (número de CSs)
- \(0 < m < 1.000.000\) (número de clientes)
- \(0 < \text{id do CS} < 1.000\)
- \(0 < \text{id do cliente} < 1.000.000\)
- \(0 < \text{nível do CS} < 10.000\)
- \(0 < \text{tamanho do cliente} < 100.000\)
- Valor máximo de \(t = n/2\) arredondado para baixo.

## Como instalar: 

1. **Clone o repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <DIR_DO_REPOSITORIO>

## Como testar: 
1. Execute o comando:
   ```bash
   python test_cs_balancing.py
