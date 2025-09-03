# 🚀 Pipeline de Automação de Pedidos com Google APIs

Este projeto automatiza o fluxo de processamento de pedidos utilizando as APIs do Google. Ele lê os pedidos de uma planilha do Google Sheets, busca informações de produtos em outra planilha (ou arquivo Excel) no Google Drive, calcula os totais e envia e-mails de confirmação personalizados via Gmail.

## ✨ Funcionalidades

- **Leitura de Pedidos:** Extrai dados de pedidos diretamente de uma planilha do Google Sheets.
- **Consulta de Produtos:** Lê a tabela de produtos, que pode ser tanto um Google Sheet quanto um arquivo Excel (`.xlsx`) armazenado no Google Drive.
- **Cálculo de Totais:** Processa os pedidos e calcula o valor total a ser cobrado de cada cliente.
- **Envio de E-mails:** Envia e-mails de confirmação personalizados para cada cliente através da API do Gmail.
- **Segurança:** Armazena os tokens de autenticação OAuth de forma segura no diretório `~/.config/pedidos-google/`.

## 📋 Requisitos

- Python 3.8+
- Uma Conta Google
- Um projeto configurado no Google Cloud Platform
- As bibliotecas Python listadas no arquivo `requirements.txt`

## ⚙️ Guia de Configuração Completo

Para que o script funcione, são necessárias duas etapas de configuração: preparar as APIs no Google Cloud e configurar o seu ambiente local.

### Parte A: Configuração do Projeto no Google Cloud

Siga estes passos para obter as credenciais de acesso às APIs.

1.  **Crie um Projeto no Google Cloud**
    * Acesse o [Google Cloud Console](https://console.cloud.google.com/).
    * No menu superior, clique no seletor de projetos e selecione **"NOVO PROJETO"**.
    * Dê um nome ao projeto (ex: `Automacao-Pedidos`) e clique em **"CRIAR"**.

2.  **Ative as APIs Necessárias**
    * Com o novo projeto selecionado, vá para o menu de navegação **APIs e serviços > Biblioteca**.
    * Pesquise e ative as três APIs a seguir, uma de cada vez:
        * `Google Sheets API`
        * `Google Drive API`
        * `Gmail API`

3.  **Configure a Tela de Consentimento OAuth**
    * No menu, acesse **APIs e serviços > Tela de consentimento OAuth**.
    * Selecione o tipo de usuário **"Externo"** e clique em **"CRIAR"**.
    * Preencha as informações obrigatórias:
        * **Nome do app:** Um nome de sua preferência (ex: "App de Pedidos").
        * **E-mail para suporte do usuário:** Seu e-mail de contato.
        * **Dados de contato do desenvolvedor:** Seu e-mail novamente.
    * Salve e continue nas próximas etapas.

4.  **Crie as Credenciais**
    * No menu, vá para **APIs e serviços > Credenciais**.
    * Clique em **"+ CRIAR CREDENCIAIS"** e selecione **"ID do cliente OAuth"**.
    * Em **"Tipo de aplicativo"**, escolha **"App para computador"**.
    * Dê um nome (ex: "Credenciais Desktop") e clique em **"CRIAR"**.

5.  **Faça o Download do JSON e Adicione Usuários de Teste**
    * Após a criação, uma janela aparecerá. Clique em **"FAZER O DOWNLOAD DO JSON"**.
    * **‼️ IMPORTANTE:** Renomeie o arquivo baixado para `client_secret.json`.
    * Volte para a **Tela de consentimento OAuth** e, na seção **"Usuários de teste"**, adicione a Conta Google que você usará para executar o script.

### Parte B: Configuração do Ambiente Local

Agora, prepare sua máquina para executar o script.

1.  **Clone o Repositório**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <NOME_DO_SEU_REPOSITORIO>
    ```

2.  **Crie um Ambiente Virtual**
    * É uma boa prática isolar as dependências do projeto.
    ```bash
    # Crie o ambiente
    python3 -m venv .venv

    # Ative o ambiente (para Linux/Mac)
    source .venv/bin/activate
    ```

3.  **Instale as Dependências**
    * Crie um arquivo `requirements.txt` com o conteúdo abaixo e depois execute o `pip`.

    *Arquivo `requirements.txt`:*
    ```
    numpy
    pandas
    tenacity
    python-dotenv
    rich
    google-api-python-client
    google-auth-oauthlib
    openpyxl # Necessário para ler arquivos .xlsx
    ```
    *Instale com o pip:*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Posicione o Arquivo de Credenciais**
    * Mova o arquivo `client_secret.json` que você baixou para o diretório de configuração.
    ```bash
    # Cria o diretório se ele não existir
    mkdir -p ~/.config/pedidos-google/

    # Mova o arquivo (ajuste o caminho se necessário)
    mv ~/Downloads/client_secret.json ~/.config/pedidos-google/
    ```

5.  **Crie o Arquivo de Variáveis de Ambiente (`.env`)**
    * Na raiz do seu projeto, crie um arquivo chamado `.env`.
    * Copie o conteúdo do exemplo abaixo e preencha com suas informações.

    *Exemplo de `.env`:*
    ```env
    # ID da planilha do Google Sheets que contém os pedidos.
    # Ex: "1a2b3c4d..." da URL da sua planilha.
    SHEETS_PEDIDOS_ID="SEU_ID_DA_PLANILHA_DE_PEDIDOS"

    # (Opcional) Range da planilha de pedidos. Padrão: "A:Z"
    SHEETS_PEDIDOS_RANGE="Pagina1!A:Z"

    # (Opcional) ID da pasta no Google Drive onde o arquivo de produtos está.
    DRIVE_PRODUTOS_FOLDER_ID="SEU_ID_DA_PASTA_NO_DRIVE"

    # Nome do arquivo de produtos (pode ser .xlsx ou Google Sheet).
    # Se deixado em branco, busca uma aba "Produtos" na mesma planilha dos pedidos.
    PRODUTOS_FILENAME="Tabela de Produtos.xlsx"

    # E-mail que será usado para enviar as confirmações.
    SENDER_EMAIL="seu-email@gmail.com"
    ```

## ▶️ Como Executar o Script

Com tudo configurado, basta rodar o comando abaixo no seu terminal (lembre-se de estar com o ambiente virtual ativado):

```bash
python3 seu_script.py
