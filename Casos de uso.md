## Casos de uso


1) **Criar Projeto**
    - **Ator**: Usuário do sistema.
    - **Objetivo**: Possibilitar que o usuário crie um novo projeto. 
    - **Pré-condições**: Sistema está operacional.
    - **Passos Principais**:
        1. Usuário acessa a seção de criação de projeto.
        2. Usuário fornece o nome do projeto, descrição e outros detalhes relevantes.
        3. Usuário confirma a criação.
    - **Pós-condições**: Um novo projeto é criado e listado no perfil do usuário.
    - **Exceções**: Caso o usuário não preencha o campo obrigatório "Nome do Projeto" o projeto não será criado e o usuário será notificado do motivo da não criação. Caso o usuário preencher o campo "Nome do Projeto" com o nome de um projeto já existente, será notificado que o projeto não pode ser criado.  

2) **Editar Projeto**
    - **Ator**: Usuário do sistema.
    - **Objetivo**: Possibilitar que o usuário consiga editar informações de algum projeto já criando anteriormente. 
    - **Pré-condições**: Usuário deve ter um projeto existente.
    - **Passos Principais**:
        1. Usuário seleciona o projeto desejado.
        2. Usuário acessa a opção de edição.
        3. Usuário modifica os detalhes necessários.
        4. Usuário salva as alterações.
    - **Pós-condições**: Os detalhes do projeto são atualizados.
    - **Exceções**: Caso o usuário apague o campo obrigatorio "Nome do Projeto" o projeto não será atualizado e o usuário será notificado. Caso o usuário altere o campo "Nome do Projeto" para o nome de um projeto já existente, será notificado que o projeto não pode ser alterado. 

3) **Gerenciar Tarefas no Projeto**
    - **Ator**: Usuário do sistema.
    - **Objetivo**: Possibilitar que o usuário crie, edite e remova tarefas dentro de algum projeto já existente, conforme sua necessidade.
    - **Pré-condições**: Usuário tem um projeto existente.
    - **Passos Principais**:
        1. Usuário acessa o projeto.
        2. Usuário adiciona, edita ou exclui tarefas conforme necessário.
    - **Pós-condições**: As tarefas dentro do projeto são atualizadas.
    - **Exceções**: Caso o usuário deixe em branco o campo obrigatorio "Nome da Tarefa" a tarefa não será atualizado ou criada e o usuário será notificado. Caso o usuário preencha o campo "Nome do Tarefa" com o nome de uma tarefa já existente, no mesmo projeto, será notificado que a tarefa não pode ser criada. 


4) **Etiquetar Tarefas**
    - **Ator**: Usuário do sistema.
    - **Objetivo**: Permitir que o usuário rotule suas tarefas com alguma etiqueta pré-definida ou criada por ele. 
    - **Pré-condições**: Usuário tem uma tarefa existente.
    - **Passos Principais**:
        1. Usuário seleciona uma tarefa.
        2. Usuário adiciona ou remove etiquetas.
    - **Pós-condições**: A tarefa é etiquetada conforme especificado pelo usuário.
    - **Exceções**: Não se aplica.

5) **Filtrar Tarefas**
    - **Ator**: Usuário do sistema.
    - **Objetivo**: Permitir que o usuário crie filtros com diversos critérios, como data de entrega, palavras-chave e etiquetas.
    - **Pré-condições**: Usuário possui tarefas criadas.
    - **Passos Principais**:
        1. Usuário acessa a opção de filtragem.
        2. Usuário define critérios de filtragem.
    - **Pós-condições**: As tarefas são exibidas com base nos critérios de filtragem.
    - **Exceções**: Não se aplica.

6) **Visualizar Tarefas no Calendário**
    - **Ator**: Usuário do sistema.
    - **Objetivo**: Permitir que o usuário visualize em um calendário todos os seus objetivos que tem data de finalização.
    - **Pré-condições**: Sistema está operacional.
    - **Passos Principais**:
        1. Usuário acessa o calendário.
        2. Usuário vê tarefas dispostas nas datas correspondentes.
    - **Pós-condições**: Tarefas são visualizadas no formato de calendário.
    - **Exceções**: Não se aplica.

 7) **Acessar Dashboard de Progresso**
    - **Ator**: Usuário do sistema.
    - **Objetivo**: Permitir que o usuário consiga visualizar o desenvolvimento de um projeto em específico ou de todos os projetos ao longo do tempo, com representações visuais intuitivas.
    - **Pré-condições**: Sistema está operacional.
    - **Passos Principais**:
        1. Usuário acessa o dashboard.
        2. Usuário vê métricas e indicadores de progresso dos projetos.
    - **Pós-condições**: O usuário tem uma visão geral do progresso dos projetos.
    - **Exceções**: Caso o usuário não tenha nenhum projeto ou tarefa, acessará a página de Dashboard vazia com a notificação que não possui projetos/tarefas. 

8) **Visualizar Histórico de Acompanhamento**
    - **Ator**: Usuário do sistema.
    - **Objetivo**: Permitir o usuário visualizar tarefas que já foram concluídos, em um ambiente separado das tarefas que estão em execução. 
    - **Pré-condições**: Sistema está operacional.
    - **Passos Principais**:
        1. Usuário acessa o histórico.
        2. Usuário vê lista de tarefas concluídas e informações relevantes.
    - **Pós-condições**: Histórico de tarefas é apresentado ao usuário.
    - **Exceções**: Caso o usuário não tenha nenhuma tarefa concluída, acessará a página de histórico vazia com a notificação que não há tarefas concluídas. 

9) **Receber Notificações de Tarefas**
    - **Ator**: Usuário do sistema.
    - **Objetivo**: Notificar o usuário de tarefas que estão proximas do prazo ou que foram marcadas como prioridades, ajudando o usuario a não se perder em seu planejamento. 
    - **Pré-condições**: Usuário tem tarefas próximas do prazo ou marcadas como urgentes.
    - **Passos Principais**:
	  1. Sistema identifica tarefas que se enquadram nos critérios.
	  2. Sistema envia notificação ao usuário.
    - **Pós-condições**: Usuário é notificado sobre tarefas pendentes ou urgentes
    - **Exceções**: Não se aplica. 

10) **Fazer Backup das Ações do Usuário**
    - **Ator**: Usuário do sistema.
    - **Objetivo**: Permitir que o usuário salve todo seus projetos para que posteriormente possa importar esses projetos novamente sem perda de tudo que registrou. 
    - **Pré-condições**: Usuário realizou ações no gerenciador de tarefas que deseja registrar em backup.
    - **Passos Principais**:
		1. Usuário acessa a opção "Criar Backup" na plataforma.
		2. Sistema registra todas as ações do usuário e cria um arquivo compactado contendo todos os dados.
		3. Sistema fornece ao usuário uma opção para baixar o arquivo de backup.
    - **Pós-condições**:
		1. Usuário tem em mãos um arquivo de backup contendo todas as suas ações.
		2. Usuário pode transferir esse arquivo para outro computador e importá-lo no gerenciador de tarefas para continuar seu trabalho de onde parou.
    - **Exceções**: Não se aplica.
