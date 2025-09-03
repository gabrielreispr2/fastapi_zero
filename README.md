<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guia de Configuração - Pipeline de Pedidos</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        h1, h2, h3 {
            color: #1a73e8;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 10px;
            margin-top: 1.5em;
        }
        h1 {
            font-size: 2.5em;
            text-align: center;
        }
        h2 {
            font-size: 2em;
        }
        h3 {
            font-size: 1.5em;
            border-bottom: 1px solid #e0e0e0;
        }
        ul, ol {
            padding-left: 20px;
        }
        li {
            margin-bottom: 1em;
        }
        code {
            background-color: #e8eaed;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
        }
        .guide-image {
            display: block;
            max-width: 100%;
            height: auto;
            border: 1px solid #ddd;
            border-radius: 4px;
            margin-top: 10px;
            margin-bottom: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .important-note {
            background-color: #fffbe6;
            border: 1px solid #ffe58f;
            border-radius: 4px;
            padding: 15px;
            margin: 1em 0;
        }
        .important-note strong {
            color: #d46b08;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Pipeline de Pedidos via Google APIs</h1>
        <p>Este script automatiza o processo de gestão de pedidos, integrando Google Sheets, Google Drive e Gmail para criar um fluxo de trabalho coeso e eficiente.</p>

        <h2>✨ Funcionalidades</h2>
        <ul>
            <li><strong>Leitura de Pedidos:</strong> Extrai dados de pedidos diretamente de uma planilha do Google Sheets.</li>
            <li><strong>Consulta de Produtos:</strong> Lê a tabela de produtos, que pode ser tanto uma planilha do Google Sheets quanto um arquivo Excel (<code>.xlsx</code>) armazenado no Google Drive.</li>
            <li><strong>Cálculo de Totais:</strong> Processa os pedidos e calcula o valor total a ser cobrado de cada cliente.</li>
            <li><strong>Envio de E-mails:</strong> Envia e-mails de confirmação personalizados para cada cliente através da API do Gmail.</li>
            <li><strong>Segurança:</strong> Armazena os tokens de autenticação OAuth de forma segura no diretório <code>~/.config/pedidos-google/</code>.</li>
        </ul>

        <h2>📋 Requisitos</h2>
        <ul>
            <li>Python 3.8 ou superior</li>
            <li>Bibliotecas listadas no arquivo <code>requirements.txt</code>.</li>
            <li>Uma Conta Google.</li>
            <li>Acesso a um projeto no Google Cloud Platform.</li>
        </ul>

        <h2>⚙️ Guia de Configuração</h2>
        <p>Para utilizar o script, é necessário configurar um projeto no Google Cloud Platform para obter as credenciais de acesso às APIs. Siga os passos abaixo.</p>

        <h3>A. Configuração do Projeto no Google Cloud</h3>
        <ol>
            <li>
                <strong>Acesse o Google Cloud Platform</strong><br>
                Se você não tiver uma conta, crie uma em <a href="https://console.cloud.google.com/" target="_blank">console.cloud.google.com</a>.
            </li>

            <li>
                <strong>Crie um Novo Projeto</strong><br>
                No painel superior, clique no seletor de projetos e, na janela que abrir, clique em <strong>"NOVO PROJETO"</strong>.
                <img src="https://placehold.co/700x150/e8eaed/7d7d7d?text=Imagem:+Seletor+de+projetos" alt="Imagem: Seletor de projetos" class="guide-image">
                Dê um nome ao seu projeto (ex: "Automacao-Pedidos") e selecione uma organização, se aplicável. Clique em <strong>"CRIAR"</strong>.
                <img src="https://placehold.co/700x300/e8eaed/7d7d7d?text=Imagem:+Tela+de+criação+de+projeto" alt="Imagem: Tela de criação de projeto" class="guide-image">
            </li>

            <li>
                <strong>Selecione o Projeto Criado</strong><br>
                Abra novamente o seletor de projetos e escolha o projeto que você acabou de criar para garantir que ele está ativo.
            </li>

            <li>
                <strong>Ative as APIs Necessárias</strong><br>
                No menu de navegação à esquerda, vá para <strong>APIs e serviços > Biblioteca</strong>. Use a barra de busca para encontrar e ativar as três APIs a seguir:
                <ul>
                    <li>Google Sheets API</li>
                    <li>Google Drive API</li>
                    <li>Gmail API</li>
                </ul>
                 <img src="https://placehold.co/700x350/e8eaed/7d7d7d?text=Imagem:+Tela+de+ativação+de+uma+API" alt="Imagem: Tela de ativação de uma API" class="guide-image">
            </li>

            <li>
                <strong>Configure a Tela de Consentimento OAuth</strong><br>
                Ainda em <strong>APIs e serviços</strong>, vá para a <strong>"Tela de consentimento OAuth"</strong>. Selecione o tipo de usuário <strong>"Externo"</strong> e clique em <strong>"CRIAR"</strong>. Preencha as informações obrigatórias (Nome do app, E-mail de suporte, etc.) e clique em <strong>"SALVAR E CONTINUAR"</strong> até o final.
            </li>

            <li>
                <strong>Crie as Credenciais (ID do Cliente OAuth)</strong><br>
                No menu à esquerda, vá para <strong>"Credenciais"</strong> e clique em <strong>"+ CRIAR CREDENCIAIS" > "ID do cliente OAuth"</strong>. Em <strong>"Tipo de aplicativo"</strong>, selecione <strong>"App para computador"</strong> e clique em <strong>"CRIAR"</strong>.
                <img src="https://placehold.co/700x400/e8eaed/7d7d7d?text=Imagem:+Configurando+o+tipo+de+aplicativo" alt="Imagem: Configurando o tipo de aplicativo" class="guide-image">
            </li>

            <li>
                <strong>Faça o Download do Arquivo JSON</strong><br>
                Uma janela aparecerá com o ID e a chave secreta. Clique em <strong>"FAZER O DOWNLOAD DO JSON"</strong>.
                <div class="important-note">
                    <strong>IMPORTANTE:</strong> Renomeie o arquivo baixado para <code>client_secret.json</code>. Este passo é crucial para que o script funcione.
                </div>
                 <img src="https://placehold.co/700x250/e8eaed/7d7d7d?text=Imagem:+Janela+para+download+do+JSON" alt="Imagem: Janela para download do arquivo JSON" class="guide-image">
            </li>

            <li>
                <strong>Adicione Usuários de Teste</strong><br>
                Volte para a <strong>"Tela de consentimento OAuth"</strong>. Na seção <strong>"Usuários de teste"</strong>, clique em <strong>"+ ADD USERS"</strong> e adicione o endereço de e-mail da conta do Google que você usará para rodar o script.
            </li>
        </ol>

        <p>Com estes passos, seu ambiente no Google Cloud está pronto. O próximo passo é configurar o ambiente local!</p>
    </div>
</body>
</html>
