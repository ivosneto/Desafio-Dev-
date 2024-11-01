nome_ouvinte=input('a ')
qtd_musicas=int(input('b '))
musica_mais_ouvida=None
musica_menos_ouvida=None
mais_streams=0
menos_streams=10000000000

for i in range (0,qtd_musicas):
    musica=input('c ')
    streams=int(input('d '))

    if i==0:
        musica_mais_ouvida = musica
        mais_streams = streams
        musica_menos_ouvida = musica
        menos_streams = streams
        

    else:
        if streams > mais_streams:
            mais_streams = streams
            musica_mais_ouvida = musica
        
        elif streams < menos_streams:
            menos_streams = streams
            musica_menos_ouvida = musica
        




if qtd_musicas == 0:
    print (f'{nome_ouvinte} é team Taylor e não ouviu Kanye West')
elif qtd_musicas==1:
    print (f'A única música que {nome_ouvinte} ouviu foi {musica_mais_ouvida} com {mais_streams} streams')
elif mais_streams == menos_streams:
    print(f'A música que {nome_ouvinte} mais ouviu foi {musica_mais_ouvida} com {mais_streams} streams')
else:
    print (f'A música que {nome_ouvinte} mais ouviu foi {musica_mais_ouvida} com {mais_streams} streams')
    print (f'A música que {nome_ouvinte} menos ouviu foi {musica_menos_ouvida} com {menos_streams} streams')