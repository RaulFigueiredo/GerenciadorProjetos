1) **Criar Projeto**
    - **Pré-condições**: Usuário deve estar autenticado no sistema.
    - **Passos Principais**:
        1. Usuário acessa a seção de criação de projeto.
        2. Usuário fornece o nome do projeto, descrição e outros detalhes relevantes.
        3. Usuário confirma a criação.
    - **Pós-condições**: Um novo projeto é criado e listado no perfil do usuário.

2) **Editar Projeto**
    - **Pré-condições**: Usuário deve ter um projeto existente.
    - **Passos Principais**:
        1. Usuário seleciona o projeto desejado.
        2. Usuário acessa a opção de edição.
        3. Usuário modifica os detalhes necessários.
        4. Usuário salva as alterações.
    - **Pós-condições**: Os detalhes do projeto são atualizados.

3) **Gerenciar Tarefas no Projeto**
    - **Pré-condições**: Usuário tem um projeto existente.
    - **Passos Principais**:
        1. Usuário acessa o projeto.
        2. Usuário adiciona, edita ou exclui tarefas conforme necessário.
    - **Pós-condições**: As tarefas dentro do projeto são atualizadas.

4) **Etiquetar Tarefas**
    - **Pré-condições**: Usuário tem uma tarefa existente.
    - **Passos Principais**:
        1. Usuário seleciona uma tarefa.
        2. Usuário adiciona ou remove etiquetas.
    - **Pós-condições**: A tarefa é etiquetada conforme especificado pelo usuário.

5) **Filtrar Tarefas**
    - **Pré-condições**: Usuário possui tarefas criadas.
    - **Passos Principais**:
        1. Usuário acessa a opção de filtragem.
        2. Usuário define critérios de filtragem.
    - **Pós-condições**: As tarefas são exibidas com base nos critérios de filtragem.

6) **Visualizar Tarefas no Calendário**
    - **Pré-condições**: Usuário tem tarefas agendadas.
    - **Passos Principais**:
        1. Usuário acessa o calendário.
        2. Usuário vê tarefas dispostas nas datas correspondentes.
    - **Pós-condições**: Tarefas são visualizadas no formato de calendário.

 7) **Acessar Dashboard de Progresso**
    - **Pré-condições**: Usuário possui projetos/tarefas.
    - **Passos Principais**:
        1. Usuário acessa o dashboard.
        2. Usuário vê métricas e indicadores de progresso dos projetos.
    - **Pós-condições**: O usuário tem uma visão geral do progresso dos projetos.

8) **Visualizar Histórico de Acompanhamento**
    - **Pré-condições**: Usuário tem um histórico de tarefas concluídas.
    - **Passos Principais**:
        1. Usuário acessa o histórico.
        2. Usuário vê lista de tarefas concluídas e informações relevantes.
    - **Pós-condições**: Histórico de tarefas é apresentado ao usuário.

9) **Receber Notificações de Tarefas**
    - **Pré-condições**: Usuário tem tarefas próximas do prazo ou marcadas como urgentes.
    - **Passos Principais**:
        1. Sistema identifica tarefas que se enquadram nos critérios.
        2. Sistema envia notificação ao usuário.
    - **Pós-condições**: Usuário é notificado sobre tarefas pendentes ou urgentes

10) **Fazer Backup das Ações do Usuário**
- **Pré-condições**: Usuário realizou ações no gerenciador de tarefas que deseja registrar em backup.
- **Passos Principais**:
    1. Usuário acessa a opção "Criar Backup" na plataforma.
    2. Sistema registra todas as ações do usuário e cria um arquivo compactado contendo todos os dados.
    3. Sistema fornece ao usuário uma opção para baixar o arquivo de backup.
- **Pós-condições**:
    1. Usuário tem em mãos um arquivo de backup contendo todas as suas ações.
    2. Usuário pode transferir esse arquivo para outro computador e importá-lo no gerenciador de tarefas para continuar seu trabalho de onde parou.