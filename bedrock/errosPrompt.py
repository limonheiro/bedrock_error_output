
import boto3
from botocore.exceptions import ClientError

# Criar o client Bedrock Runtime na região AWS de uso.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

def messagePrompt(message="ola"):
    model_id = "amazon.titan-text-premier-v1:0"
    # print(message)
    conversation = [
        {
            "role": "user",
            "content": [{"text": "Olá estou com este erro no meu código em python, gostaria de uma resposta em pt-br:"+message}],
        }
    ]
    
    try:
        # Envia a mensagem para o modelo, usando a inferencia.
        response = client.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
        )

        # Extrair e printar a resposta.
        response_text = response["output"]["message"]["content"][0]["text"]
        # print("\nResposta do modelo:")
        return response_text

    except (ClientError, Exception) as e:
        return f"ERRO: Falha na chamada '{model_id}'. Erro: {e}"
    
if __name__ == "__main__":
    print(2)