c = ' ' #inicializei a varíavei que receberia o texto
cont = 0 #inicializei um contador
while cont<990: #iniciei um laço de repetição que só vai parar de executar todas linhas abaixo quando ele for = 990 (o que não vai ocorrer)
    c = str(input('Texto')).strip() #variável que vai recber os 11550 caracteres
    dif = 'vimeo-prod-skyfire-std-us' #existem 4 links, mas só 3 deles recebem essa varíavel aí pra n pegar o errado meti um diferenciador
    link = 'https://vod-progressive.akamaized.net/exp=1630590962~acl=%2Fvimeo-prod-skyfire-std-us%2F01%2F3559%2F23%2F592797447%2F2793428542.mp4~hmac=4872a4b7fef39214198b5a35897e27d14addc6e8dfe9f8ee498ef6b567c999b4/vimeo-prod-skyfire-std-us/01/3559/23/592797447/2793428542.mp4'
    padrao = 'https://vod-progressive.akamaized.net/exp='
    print(f'Você deve voltar {len(padrao)} caracteres')
    print(len(c))
    print(len(padrao))
    print(f'O diferenciador começa em {c.find(dif)}')
    print(f'Começa em {c.find(dif)-len(padrao)}')
    começo = c.find(dif)-(len(padrao))
    ultimo = começo+263
    print(len(link))
    print(c[começo:ultimo])


