frase = 'O programa de computador surgiu antes do desenvolvimento do computador eletrônico. \
    Um trabalho publicado em 1843 por Ada Lovelace, sugerindo uma forma para calcular os \
    números de Bernoulli através da máquina analítica de Charles Babbage, é tido \
    como o primeiro programa de computador.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)
