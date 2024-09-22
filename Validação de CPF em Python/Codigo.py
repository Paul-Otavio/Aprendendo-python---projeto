import re
import sys

# Solicita a entrada do CPF ao usuário
entrada = input('CPF [746.824.890-70]: ')

# Remove todos os caracteres não numéricos da entrada do CPF
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

# Verifica se a entrada é uma sequência de números repetidos
entrada_e_sequencial = entrada == entrada[0] * len(entrada)

# Se a entrada for sequencial, exibe uma mensagem e encerra o programa
if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

# Extrai os primeiros nove dígitos do CPF
nove_digitos = cpf_enviado_usuario[:9]

# Inicializa o contador regressivo para o primeiro dígito verificador
contador_regressivo_1 = 10

# Calcula o primeiro dígito verificador
resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Adiciona o primeiro dígito verificador aos nove dígitos iniciais
dez_digitos = nove_digitos + str(digito_1)

# Inicializa o contador regressivo para o segundo dígito verificador
contador_regressivo_2 = 11

# Calcula o segundo dígito verificador
resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

# Concatena os dígitos para formar o CPF completo gerado pelo cálculo
cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# Verifica se o CPF enviado pelo usuário é válido
if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')

