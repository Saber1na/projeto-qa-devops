# tests/test_validacao_senha.py

import pytest
from pytest_bdd import scenario, scenarios, given, when, then, parsers

# Importa a função que vamos testar (do outro arquivo)
from app_logic import validar_senha


# --- Contexto ---
@pytest.fixture
def context():
    return {}


# --- Ligação dos Cenários ---
# Esta linha "mágica" diz ao pytest para LER TODOS os cenários
# do arquivo .feature e executá-los.
scenarios('features/validacao_senha.feature')


# --- Implementação dos Passos (Steps) ---

@given(parsers.parse('que eu informe a senha "{senha}"'), target_fixture="context")
def given_informar_senha(context, senha):
    """Guarda a senha do Gherkin no contexto."""
    context['senha_atual'] = senha
    print(f"\n[TESTE] Senha informada: {senha}")
    return context

@when('o sistema validar a senha', target_fixture="context")
def when_validar_senha(context):
    """Chama a função de lógica de negócio."""
    senha = context['senha_atual']
    resultado = validar_senha(senha) # AQUI testamos o código local
    context['resultado_validacao'] = resultado
    print(f"[TESTE] Resultado da função: {resultado}")
    return context

@then(parsers.parse('o resultado da validação deve ser "{esperado}"'))
def then_verificar_resultado(context, esperado):
    """Compara o resultado da função com o esperado no Gherkin."""

    # Converte o texto "válida" ou "inválida" para True/False
    resultado_esperado_bool = True if esperado == "válida" else False

    resultado_obtido = context['resultado_validacao']

    print(f"[TESTE] Esperado: {resultado_esperado_bool}, Recebido: {resultado_obtido}")

    # A verificação final do QA
    assert resultado_obtido == resultado_esperado_bool, "O resultado da validação não foi o esperado!"