# --- DADOS DE EXEMPLO ---
# Não altere esta lista
lista_tarefas = [
    {'id': 1, 'titulo': 'Desenvolver tela de login', 'status': 'concluida'},
    {'id': 2, 'titulo': 'Testar API de usuários', 'status': 'pendente'},
    {'id': 3, 'titulo': 'Corrigir bug do relatório', 'status': 'concluida'},
    {'id': 4, 'titulo': 'Documentar funcionalidade X', 'status': 'pendente'},
    {'id': 5, 'titulo': 'Revisar layout', 'status': 'pendente'},
]

# --- FUNÇÃO 1 ---
def calcular_progresso(tarefas):
    """
    Complete esta função.
    Recebe: uma lista de dicionários (tarefas).
    Retorna: a porcentagem (float) de tarefas com status 'concluida'.
    
    Ex: Se 2 de 5 tarefas estiverem 'concluida', deve retornar 40.0
    """
    
    # TODO: Escreva seu código aqui para a FUNÇÃO 1.
    # Lembre-se de tratar o caso de divisão por zero (lista vazia).
    
    pass

# --- FUNÇÃO 2 ---
def obter_titulos_pendentes(tarefas):
    """
    Complete esta função.
    Recebe: uma lista de dicionários (tarefas).
    Retorna: uma NOVA LISTA contendo apenas os TÍTULOS das tarefas
             que estão com status 'pendente'.
    """
    
    # TODO: Escreva seu código aqui para a FUNÇÃO 2.
    
    pass


print(f"--- Teste Python ---")
total = len(lista_tarefas) 

# Teste 1: Progresso
porcentagem = calcular_progresso(lista_tarefas)
print(f"\n[Teste de Progresso]")
print(f"Dados de exemplo: {total} tarefas")
print(f"Progresso: {porcentagem}%")

# Teste 2: Filtro
titulos = obter_titulos_pendentes(lista_tarefas)
print(f"\n[Teste de Filtro de Pendentes]")
print(f"Total de tarefas pendentes: {len(titulos) if titulos else 0}")
print("Títulos:")
if titulos is not None:
    for titulo in titulos:
        print(f"  - {titulo}")
else:
    print(" (lista não retornada)")

# --- Resultado esperado ---
# --- Teste Python Unificado ---
#
# [Teste de Progresso]
# Dados de exemplo: 5 tarefas
# Progresso: 40.0%
#
# [Teste de Filtro de Pendentes]
# Total de tarefas pendentes: 3
# Títulos:
#   - Testar API de usuários
#   - Documentar funcionalidade X
#   - Revisar layout