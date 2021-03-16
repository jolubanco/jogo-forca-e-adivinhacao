import random

def jogar():
    print('********************************')
    print('Bem vindo no jogo de Advinhação!')
    print('********************************')

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual o nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')
    nivel = int(input('Defina o nível: '))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas+1):
        print('Tentativa {} de {}'.format(rodada,total_de_tentativas))

        chute_str = input('Digite um número entre 1 e 100: ')
        print('Voce digitou ', chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100')
            continue #vai para a proxima iteraçao sem sair do laço

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print('Você acertou e fez {} pontos!'.format(pontos))
            break #sai abruptamento do laço
        else:
            if(maior):
                print('Voce errou! O seu chute foi maior que o número secreto')
                if(rodada == total_de_tentativas):
                    print('O número secreto era {}. Você fez {} pontos!'.format(numero_secreto,pontos))
            elif(menor):
                print('Voce errou! O seu chute foi menor que o número secreto')
                if (rodada == total_de_tentativas):
                    print('O número secreto era {}. Você fez {} pontos!'.format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print('Fim do jogo!')

if(__name__ == "__main__"):
    jogar()
























    #while(rodada <= total_de_tentativas):
    #    print('Tentativa {} de {}'.format(rodada,total_de_tentativas))
    #    chute_str = input('Digite o seu número: ')
    #    print('Voce digitou ', chute_str)
    #   chute = int(chute_str)

    #    acertou = chute == numero_secreto
    #    maior   = chute > numero_secreto
    #    menor   = chute < numero_secreto

    #    if (acertou):
    #        print('Você acertou!')
    #    else:
    #        if(maior):
    #            print('Voce errou! O seu chute foi maior que o número secreto')
    #        elif(menor):
    #            print('Voce errou! O seu chute foi menor que o número secreto')
    #    rodada += 1
    #print('Fim do jogo!')