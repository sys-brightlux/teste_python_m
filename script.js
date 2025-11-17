// --- DADOS DE EXEMPLO ---
// Não altere esta lista
const listaTarefas = [
    {id: 1, titulo: 'Desenvolver tela de login', status: 'concluida'},
    {id: 2, titulo: 'Testar API de usuários', status: 'pendente'},
    {id: 3, titulo: 'Corrigir bug do relatório', status: 'concluida'},
    {id: 4, titulo: 'Documentar funcionalidade X', status: 'pendente'},
    {id: 5, titulo: 'Revisar layout', status: 'pendente'},
];

/**
 * 1. Popular a <ul> com os itens da lista.
 * 2. Atualizar o <span> com a contagem de tarefas pendentes.
 */
function exibirTarefasEContador() {
    
    // TODO: 1. Encontre a <ul> (id="lista-tarefas")
    const elementoLista = document.getElementById('lista-tarefas');
    
    // TODO: 2. Encontre o <span> (id="contador-pendentes")
    const elementoContador = document.getElementById('contador-pendentes');
    
    // (Opcional: Limpar a lista antes de adicionar novos itens)
    // elementoLista.innerHTML = '';
    
    // Variável para contar
    let contagemPendentes = 0;

    // TODO: 3. Itere sobre a 'listaTarefas' (usando for, forEach, map, etc.)
    
    
        // Dentro do loop, você deve:
        
        // --- Tarefa 1: ---
        // TODO: 4a. Crie um novo elemento <li>
        // TODO: 4b. Defina o texto do <li> (ex: "[pendente] Testar API de usuários")
        // TODO: 4c. Adicione a classe CSS correta ao <li> ('concluida' ou 'pendente')
        // TODO: 4d. Adicione o <li> à <ul> (elementoLista)
        
        
        // --- Tarefa 2: ---
        // TODO: 5. Se a tarefa atual tiver status 'pendente',
        // incremente a variável 'contagemPendentes'
        
    // (Fim do loop)


    // TODO: 6. Após o loop, atualize o texto do 'elementoContador'
    // com o valor final da 'contagemPendentes'.
    // ex: elementoContador.textContent = contagemPendentes;
    
}

exibirTarefasEContador();