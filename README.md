# Number Access Verification in Django

## **Sobre o Projeto**
Este é um aplicativo simples para ver quantas vezes um determinado número foi acessado por um usuário. Ele é composto por um **back-end** que processa e armazena os dados e um **front-end** que permite a interação do usuário. O objetivo é demonstrar conceitos básicos de uma API REST e de uma interface de usuário funcional.

## **Funcionalidades**
- Registro de números submetidos pelos usuários.
- Exibição da quantidade de vezes que um número foi acessado globalmente.
- Interface amigável, com validação de entrada e feedback visual.

## **Como Executar**

### **Back-end**
1. Clone o projeto:
   ```bash
   git clone https://github.com/joaoVictorBAlves/contagem_valores
   ```
2. Instale os requisitos:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure o ambiente:
   - Certifique-se de que o banco de dados está configurado (SQLite ou outro).
   - Migre o banco:
     ```bash
     python manage.py migrate
     ```
4. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

## **Back-end**
O servidor fornece um endpoint principal para registrar e contar os valores submetidos. A API foi desenvolvida em um framework como **Django** ou **Flask**.

#### **Endpoints**
##### 1.1. `POST /registrar_valor/`
- **Descrição**: Registra um número enviado pelo usuário e atualiza o contador global.
- **Parâmetros de Entrada**:
  - `valor` (form-data ou x-www-form-urlencoded): O número a ser registrado.
- **Resposta** (em JSON):
  - **Sucesso (HTTP 200)**:
    ```json
    {
        "valor": 42,
        "contagem": 3
    }
    ```
    - `valor`: O número submetido.
    - `contagem`: Quantidade de vezes que o número foi registrado até agora.
  - **Erro (HTTP 400 ou 500)**:
    ```json
    {
        "error": "Mensagem de erro descritiva."
    }
    ```
