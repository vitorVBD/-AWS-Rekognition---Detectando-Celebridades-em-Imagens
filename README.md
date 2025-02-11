# Reconhecimento de Celebridades com AWS Rekognition

Este projeto utiliza o serviço AWS Rekognition para reconhecer celebridades em imagens. Ele foi desenvolvido em Python usando a biblioteca Boto3 para interagir com os serviços da AWS.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes requisitos:

1. **Conta AWS**: Você precisa de uma conta na AWS e de credenciais de acesso (Access Key e Secret Key).
2. **Python 3.x**: O código foi desenvolvido para Python 3.
3. **Boto3**: A biblioteca Boto3 é necessária para interagir com os serviços da AWS.
4. **Imagens**: Tenha as imagens que deseja analisar prontas.

## Instalação

1. Clone este repositório:
   ```
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. Instale as dependências:

```pip install boto3```

3. Configure suas credenciais da AWS:

- Crie um arquivo ```~/.aws/credentials (Linux/Mac)``` ou ```%UserProfile%\.aws\credentials (Windows)``` com o seguinte conteúdo:

    ```
    [default]
    aws_access_key_id = SUA_ACCESS_KEY
    aws_secret_access_key = SUA_SECRET_KEY

## Como Usar
1. Coloque a imagem que deseja analisar na pasta do projeto ou forneça o caminho completo para a imagem.

2. Execute o script Python:
    ```
    python index.py

3. O script exibirá no console as celebridades reconhecidas na imagem, juntamente com informações como nome, ID, URLs e confiança do reconhecimento.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença
Este projeto está licenciado sob a licença MIT.
