import requests
import bedrock.errosPrompt as prompt

BASE_URL = 'https://bible-api.com/'

#retorna o versiculo
def getOutput(json):
    return f'{json.get('verses')[0]['text']}\n{json.get('reference')}'

#faz a requisição e a verifica
def getConect(base, endpoint=''):
    try:
        return requests.get(f'{BASE_URL}{endpoint}')
    except (requests.RequestException, Exception) as e:
        return prompt.messagePrompt(str(e)) 
        # return f'Máximo de tentativas excedidas:\nErro:{e}'

#verifica o retorno da requisição e retorna a chamada da mensagem
def getMsg(request):
    if not isinstance(request, str):
        return  getOutput(request.json())
    else:
        return request

#retorna um versiculo aleatória
def apiBibleRandom():
    r = getConect(BASE_URL, '?random=verse&translation=almeida')
    return getMsg(r)

#retorna o versiculo baseado no argumento
def apiBible(*args):
    r = getConect(BASE_URL, ''.join(args)+'?translation=almeida')
    return getMsg(r)
    
if __name__ == "__main__":
    mgs = apiBibleRandom()
    print(mgs)
    mgs = apiBible('Lucas 3:16')
    print(mgs)