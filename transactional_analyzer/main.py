from Analyzer import Analyzer
from reports import (
    HigherAmount,
    UnusualHours,
    ShortTime,
    ManyDevicesByCard,
    ManyTransactionsByUser
)


def main():
    print('\n Selecione:\n')
    print('1 - Consulta Usuário Suspeito')
    print('2 - Relatório de Transações com Chargeback\n')

    first_option = int(input("Opção: "))

    if first_option == 1:
        user_id = int(input('\n Digite o id que deseja consultar: '))
        Analyzer.user_analyzer(user_id)

    elif first_option == 2:
        print('\n Escolha o relatório desejado:\n ')
        print('1 - Valores altos')
        print('2 - Ocorridas entre 00:00h e 05:59h')
        print('3 - Mesmo usuário em um curto espaço de tempo')
        print('4 - Mesmo cartão em dispositivos diferentes')
        print('5 - Mesmo usuário com muitas transações\n ')

        option = int(input("Opção: "))

        switcher = {
            1: HigherAmount.HigherAmount().report,
            2: UnusualHours.UnusualHours().report,
            3: ShortTime.ShortTime().report,
            4: ManyDevicesByCard.ManyDevicesByCard().report,
            5: ManyTransactionsByUser.ManyTransactionsByUser().report,
        }

        def switch(option):
            if option >= 1 and option <= 5:
                return switcher.get(option)()
            else:
                encerrar()

        switch(option)

    else:
        encerrar()


def encerrar():
    print('\n Opção inválida. Digite novamente')
    main()


if __name__ == '__main__':
    main()
