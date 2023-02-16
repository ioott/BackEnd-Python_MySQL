from reports import (
    HigherAmount,
    UnusualHours,
    ShortTime,
    ManyDevicesByCard,
    ManyTransactionsByUser
)


def main():
    while (True):
        print('Escolha o relatório de transações com chargeback desejado:')
        print('1 - Valores altos')
        print('2 - Ocorridas entre 00:00h e 05:59h')
        print('3 - Mesmo usuário em um curto espaço de tempo')
        print('4 - Mesmo cartão em dispositivos diferentes')
        print('5 - Mesmo usuário com muitas transações')
        print('6 - Sair')

        option = int(input("Opção: "))

        switcher = {
            1: HigherAmount.HigherAmount().report,
            2: UnusualHours.UnusualHours().report,
            3: ShortTime.ShortTime().report,
            4: ManyDevicesByCard.ManyDevicesByCard().report,
            5: ManyTransactionsByUser.ManyTransactionsByUser().report,
            6: encerrar,
        }

        def switch(option):
            return switcher.get(option, 0)()

        switch(option)


def encerrar():
    print('Encerrado')
    exit()


if __name__ == '__main__':
    main()
