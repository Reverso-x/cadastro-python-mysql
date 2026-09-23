# 🔐 Sistema de Cadastro e Login
###  Sistema de cadastro e login desenvolvido em Python com MySQL, executado através do terminal.

---

### 🔨 Em desenvolvimento

O projeto ainda está em desenvolvimento e novas funcionalidades poderão ser adicionadas futuramente.

---

### 📌 Sobre o projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos de programação em Python e integração com banco de dados MySQL.

O sistema permite realizar operações de cadastro e autenticação de usuários através do terminal.

---

### 📚 Objetivo

Projeto desenvolvido para praticar Python, SQL e integração com banco de dados, fazendo parte dos meus estudos em programação e tecnologia.

---

### ⚙️ Tecnologias utilizadas

- 🐍 Python
- 🗄️ MySQL
- 🐙 GitHub

---

### 🚀 Funcionalidades

- 👤 Cadastro de usuários
- 🔑 Login de usuários **(pendente)**
- ✅ Validação de dados **(pendente)**
- 🗄️ Armazenamento de informações no MySQL
- 🔎 Consulta de usuários no banco de dados

---

### 🖥️ Execução

O sistema é executado diretamente pelo terminal.

É necessário ter o MySQL instalado e executar o arquivo `banco.sql` para criar o banco de dados e a tabela.

**⚠️ Antes de executar o projeto:**

Configure no arquivo `main.py` os dados de acesso ao seu MySQL, **principalmente o usuário(user) e a senha(password)** da sua instalação.

Por exemplo:

```python
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SUA_SENHA",
    database="cadastro_db"
)
```

