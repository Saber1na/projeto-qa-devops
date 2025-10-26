# language: pt
# tests/features/validacao_senha.feature

Funcionalidade: Validação de Senha
  Para garantir a segurança das contas,
  Como um administrador do sistema,
  Eu quero que as senhas obedeçam regras de complexidade.

Cenário: Tentativa com senha forte
  Dado que eu informe a senha "SenhaForte123"
  Quando o sistema validar a senha
  Então o resultado da validação deve ser "válida"

Cenário: Tentativa com senha fraca (muito curta)
  Dado que eu informe a senha "Fraca1"
  Quando o sistema validar a senha
  Então o resultado da validação deve ser "inválida"

Cenário: Tentativa com senha fraca (sem número)
  Dado que eu informe a senha "SenhaSemNumero"
  Quando o sistema validar a senha
  Então o resultado da validação deve ser "inválida"

Cenário: Tentativa com senha fraca (sem maiúscula)
  Dado que eu informe a senha "senhaforte123"
  Quando o sistema validar a senha
  Então o resultado da validação deve ser "inválida"