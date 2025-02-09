import boto3
from botocore.exceptions import NoCredentialsError, BotoCoreError

def reconhecer_celebridades_em_imagem(caminho_imagem):
    # Inicializa o cliente do Rekognition
    client = boto3.client('rekognition')

    try:
        # Abre a imagem e converte para bytes
        with open(caminho_imagem, 'rb') as image_file:
            image_bytes = image_file.read()

        # Chama a API do Rekognition para reconhecer celebridades
        response = client.recognize_celebrities(Image={'Bytes': image_bytes})

        # Processa a resposta
        if 'CelebrityFaces' in response:
            for celeb in response['CelebrityFaces']:
                print(f"Nome: {celeb['Name']}")
                print(f"ID: {celeb['Id']}")
                print(f"URLs: {celeb['Urls']}")
                print(f"Confiança: {celeb['MatchConfidence']}%")
                print("------")
        else:
            print("Nenhuma celebridade reconhecida na imagem.")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_imagem}' não encontrado.")
    except NoCredentialsError:
        print("Erro: Credenciais da AWS não encontradas.")
    except BotoCoreError as e:
        print(f"Erro ao acessar o serviço AWS Rekognition: {e}")

# Exemplo de uso
caminho_imagem = 'caminho/para/sua/imagem.jpg'
reconhecer_celebridades_em_imagem(caminho_imagem)