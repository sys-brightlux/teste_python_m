# **Teste Rápido de Programação \- Desenvolvimento de Sistemas**

Bem-vindo(a) ao nosso teste\! O objetivo é avaliar sua lógica de programação e familiaridade com as tecnologias que usamos no dia a dia.

Este teste é dividido em duas partes, ambas com dois objetivos:

1. **Lógica em Python** (arquivo: teste\_python.py)  
2. **Front-End em HTML/JavaScript** (arquivo: index.html)

## **Contexto**

Estamos trabalhando em um sistema de gerenciamento de projetos. A base do sistema são Usuários e suas Tarefas. Os dados de exemplo já estão fornecidos no arquivo de script (index.html ou teste\_python.py).

## **📜 Regras e Diretrizes para o Teste (Obrigatório)**

Para garantir a igualdade e a validade da avaliação, o teste deve ser realizado seguindo as seguintes regras **restritivas**:

* **Duração:** O tempo máximo de realização é de **1 hora** a partir do momento em que o teste for iniciado.  
* **Recursos Externos:** O uso de **qualquer tipo de pesquisa externa** é estritamente proibido. Isso inclui, mas não se limita a:  
  * Navegadores de internet (Google, Stack Overflow, MDN, etc.).  
  * Ferramentas de Inteligência Artificial (IA), como ChatGPT, Gemini, Copilot, etc.  
  * Vídeos (YouTube) ou quaisquer outros tutoriais online.  
* **Dispositivos Pessoais:** O uso de **celulares** ou outros dispositivos de comunicação é proibido durante a realização.  
* **Fones de Ouvido:** O uso de **fones de ouvido** ou qualquer dispositivo de áudio não é permitido.  
* **Material de Consulta:** A única fonte de informação permitida são os **arquivos fornecidos** no próprio teste.

## **Tarefa 1: Lógica de Programação (Python)**

**Arquivo:** teste\_python.py

Abra o arquivo teste\_python.py. Você encontrará uma lista de tarefas e duas funções que precisam ser completadas: calcular\_progresso e obter\_titulos\_pendentes.

**Seus objetivos:**

1. **Função calcular\_progresso:** Complete a função para que ela retorne a porcentagem (float) de tarefas com status **'concluida'**.  
   * *Resultado esperado: 40.0%*  
2. **Função obter\_titulos\_pendentes:** Complete a função para que ela retorne uma **nova lista** contendo apenas os **títulos** das tarefas com status **'pendente'**.  
   * Resultado esperado (Títulos):$$'Testar API de usuários', 'Documentar funcionalidade X', 'Revisar layout'$$

## **Tarefa 2: Front-End (HTML/JavaScript)**

**Arquivos:** index.html

O projeto Front-End será implementado em um **único arquivo** (index.html) contendo HTML, CSS (com Tailwind) e JavaScript.

**Seus objetivos:**

1. **Popular a Lista:** Edite a seção \<script\> do index.html para iterar sobre a listaTarefas. Para cada tarefa, crie um item de lista (\<li\>), adicione a classe CSS correta (concluida ou pendente) e adicione-o à \<ul\> (com id lista-tarefas).  
2. **Atualizar o Contador:** Durante a iteração, conte quantas tarefas possuem o status **'pendente'** e atualize o texto do \<span\> (com id contador-pendentes) com esse número.  
   * *Resultado esperado: O número **3** deve aparecer no cabeçalho.*

## **Como Entregar**

Complete as tarefas nos arquivos indicados (teste\_python.py e index.html).

Boa sorte\!
