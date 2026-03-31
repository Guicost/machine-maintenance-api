# 🏭 Machine Maintenance API

Projeto em desenvolvimento com o objetivo de **gerenciar máquinas** e controlar **manutenções** de forma simples e organizada.

A ideia é simular um cenário real, onde é necessário acompanhar equipamentos e registrar intervenções (preventivas ou corretivas).

---

##  Funcionalidades

O sistema permite:

* Cadastrar máquinas
* Registrar manutenções vinculadas a uma máquina
* Listar, atualizar e remover registros
* Organizar tudo em uma **API REST simples**

---

## 🛠 Tecnologias utilizadas

* Python
* FastAPI
* SQLAlchemy
* SQLite

---

##  Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Guicost/machine-maintenance-api.git
cd machine-maintenance-api/backend
```

### 2. Crie e ative o ambiente virtual

```bash
python3 -m venv venv

# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Rode a aplicação

```bash
uvicorn app.main:app --reload
```

### 5. Acesse a documentação

```
http://127.0.0.1:8000/docs
```

---

##  Exemplos de uso

### Criar máquina

```json
{
  "nome": "Torno",
  "modelo": "TC-800",
  "status": "ativa"
}
```

### Criar manutenção

```json
{
  "descricao": "Troca de óleo",
  "tipo": "preventiva",
  "status": "pendente",
  "maquina_id": 1
}
```
