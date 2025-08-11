## Sistema de Gestão Escolar
Um sistema de linha de comando em Python para gerenciar o cadastro de alunos, notas e turmas. O projeto inclui funcionalidades de autenticação de usuários, operações CRUD (Criar, Ler, Atualizar e Deletar), além de relatórios e análises de desempenho.

### 🚀 Funcionalidades
* **Autenticação de Usuários**: Sistema de login e cadastro com senha criptografada (hash SHA-256).

* **CRUD de Alunos**: Gerencia o cadastro de alunos, incluindo nome, e-mail, turma e notas.

* **Validação de Dados**: Valida e-mails e notas, garantindo a integridade dos dados.

* **Relatórios de Desempenho**: Calcula a média dos alunos e gera um relatório detalhado de desempenho, mostrando a quantidade de aprovados, reprovados e alunos em recuperação por turma.

* **Gráficos Visuais**: Exibe um gráfico de barras com o desempenho geral dos alunos, utilizando a biblioteca matplotlib.

* **Exportação de Dados**: Exporta todos os dados de alunos para um arquivo .csv usando a biblioteca pandas.

### 🛠️ Tecnologias e Dependências
O projeto foi desenvolvido em Python e utiliza as seguintes bibliotecas:

* sqlite3: Para a gestão do banco de dados local.

* pandas: Para manipulação e exportação de dados para CSV.

* matplotlib: Para a geração de gráficos.

* hashlib: Para a criptografia de senhas.

* re: Para validação de expressões regulares (e-mail).

Para instalar as dependências, execute o seguinte comando:

```
Bash

pip install pandas matplotlib
```
⚙️ Como Instalar e Rodar o Projeto
Clone o repositório para o seu ambiente local:
```
Bash

git clone https://github.com/KlausMachado/AppEscola
```
Navegue até o diretório do projeto:
```
Bash

cd AppEscola
```
Instale as dependências listadas acima.

Execute o arquivo principal do projeto:
```
Bash

python main.py
```
### 📖 Como Usar
Ao iniciar o programa, você será direcionado para o menu de autenticação.

**Login/Cadastro:**

* Crie um novo usuário com a opção 1.

* Faça login com um usuário existente usando a opção 2. (Já existem usuários de teste pré-cadastrados para facilitar: usuario1@email.com, usuario2@email.com, etc., todos com a senha 123).

**Menu Principal**:

Após o login, você terá acesso ao menu principal, onde poderá escolher entre as seguintes ações:

**1- Exibir lista de alunos**: Mostra todos os alunos cadastrados.

**2- Inserir novo aluno**: Adiciona um novo aluno ao banco de dados.

**3- Deletar aluno: Remove um aluno pelo nome.**

**4- Alterar aluno**: Atualiza os dados de um aluno (nome, e-mail, turma, notas).

**5- Calcular média dos alunos**: Exibe um relatório detalhado e um gráfico de desempenho.

**6- Buscar aluno**: Procura um aluno específico pelo nome.

**7- Buscar turma**: Lista todos os alunos de uma turma.

**8- Exportar relatório geral em CSV**: Cria um arquivo relatorio_alunos.csv com todos os dados.

**9- SAIR**: Encerra o programa.

### 🤝 Contribuição
Contribuições são bem-vindas! Se você tiver ideias para melhorar o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### 📄 Licença
Este projeto está licenciado sob a licença MIT.
