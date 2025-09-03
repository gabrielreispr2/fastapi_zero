Pipeline de Pedidos via Google APIs

Este script automatiza o processo de gestão de pedidos, integrando Google Sheets, Google Drive e Gmail para criar um fluxo de trabalho coeso e eficiente.
✨ Funcionalidades

    Leitura de Pedidos: Extrai dados de pedidos diretamente de uma planilha do Google Sheets.

    Consulta de Produtos: Lê a tabela de produtos, que pode ser tanto uma planilha do Google Sheets quanto um arquivo Excel (.xlsx) armazenado no Google Drive.

    Cálculo de Totais: Processa os pedidos e calcula o valor total a ser cobrado de cada cliente.

    Envio de E-mails: Envia e-mails de confirmação personalizados para cada cliente através da API do Gmail.

    Segurança: Armazena os tokens de autenticação OAuth de forma segura no diretório ~/.config/pedidos-google/.

📋 Requisitos

    Python 3.8 ou superior

    Bibliotecas listadas no arquivo requirements.txt.

    Uma Conta Google.

    Acesso a um projeto no Google Cloud Platform.

⚙️ Guia de Configuração

Para utilizar o script, é necessário configurar um projeto no Google Cloud Platform para obter as credenciais de acesso às APIs. Siga os passos abaixo.
A. Configuração do Projeto no Google Cloud

    Acesse o Google Cloud Platform

        Se você não tiver uma conta, crie uma em console.cloud.google.com.

    Crie um Novo Projeto

        No painel superior, clique no seletor de projetos.

        [Imagem: Seletor de projetos]

        Na janela que abrir, clique em "NOVO PROJETO".

        [Imagem: Botão para criar novo projeto]

        Dê um nome ao seu projeto (ex: "Automacao-Pedidos") e selecione uma organização, se aplicável. Clique em "CRIAR".

        [Imagem: Tela de criação de projeto]

    Selecione o Projeto Criado

        Abra novamente o seletor de projetos e escolha o projeto que você acabou de criar para garantir que ele está ativo.

        [Imagem: Selecionando o projeto recém-criado]

    Ative as APIs Necessárias

        No menu de navegação à esquerda, vá para APIs e serviços > Biblioteca.

        [Imagem: Menu de navegação para APIs e Serviços]

        Use a barra de busca para encontrar e ativar as três APIs a seguir, uma por uma:

            Google Sheets API

            Google Drive API

            Gmail API

        [Imagem: Tela de ativação de uma API]

    Configure a Tela de Consentimento OAuth

        Ainda em APIs e serviços, vá para a "Tela de consentimento OAuth".

        [Imagem: Menu para Tela de consentimento OAuth]

        Selecione o tipo de usuário "Externo" e clique em "CRIAR".

        [Imagem: Selecionando tipo de usuário Externo]

        Preencha as informações obrigatórias:

            Nome do app: Dê um nome de sua preferência (ex: "App de Pedidos").

            E-mail para suporte do usuário: Insira seu e-mail.

            Dados de contato do desenvolvedor: Insira seu e-mail novamente.

        Clique em "SALVAR E CONTINUAR" nas seções seguintes até chegar ao fim.

    Crie as Credenciais (ID do Cliente OAuth)

        No menu à esquerda, vá para "Credenciais" e clique em "+ CRIAR CREDENCIAIS" > "ID do cliente OAuth".

        [Imagem: Botão para criar credenciais]

        Em "Tipo de aplicativo", selecione "App para computador".

        Dê um nome para a credencial (ex: "Credenciais Desktop") e clique em "CRIAR".

        [Imagem: Configurando o tipo de aplicativo]

    Faça o Download do Arquivo JSON

        Uma janela aparecerá com o ID e a chave secreta do cliente. Clique em "FAZER O DOWNLOAD DO JSON".

        [Imagem: Janela para download do arquivo JSON]

        ‼️ IMPORTANTE: Renomeie o arquivo baixado para client_secret.json. Este passo é crucial para que o script funcione.

    Adicione Usuários de Teste

        Como o aplicativo está em modo de teste, você precisa autorizar explicitamente as contas do Google que poderão usá-lo.

        Volte para a "Tela de consentimento OAuth".

        Na seção "Usuários de teste", clique em "+ ADD USERS".

        [Imagem: Adicionando um usuário de teste]

        Adicione o endereço de e-mail da conta do Google que você usará para rodar o script e enviar os e-mails.

Com estes passos, seu ambiente no Google Cloud está pronto. O próximo passo é configurar o ambiente local!
