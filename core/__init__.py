import datetime

class SystemInfo:
    def __init__(self):
        pass
    
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = "São {} horas e {} minutos." .format(now.hour, now.minute)
        return answer

    @staticmethod
    def get_date():
        now = datetime.datetime.now()
        answer = 'Hoje é dia {} de {} de {}'.format(now.day, now.strftime('%B'), now.year)
        return answer
    
    @staticmethod
    def get_helpList():
        answer = 'Oi, sou sua assistente virtual... {}... {}... {}... {}... {}'.format('Minha função é te auxiliar em suas atividades no computador',
        'No momento posso te informar a hora e data atual',
        'Tabuada do um, tabuada do dois',
        'Também posso te auxiliar em abrir programas como o bloco de notas, chrome e Dosvox',
        'Antes de abrir verifique se o programa está instalado')
        
        return answer
    
    @staticmethod
    def get_multiplOne():
        answer = 'Tabuada do um... {}... {}... {}... {}... {}... {}... {}... {}... {}'.format(
        'um vezes um é igual a um', 'um vezes dois é igual a dois',
        'um vezes três é igual a três', 'um vezes quatro é igual a quatro', 
        'um vezes cinco é igual a cinco', 'um vezes seis é igual a seis',
        'um vezes sete é igual a sete', 'um vezes oito é igual a oito', 
        'um vezes nove é igual a nove', 'um vezes dez é igual a dez')

        return answer

    @staticmethod
    def get_multiplTwo():
        answer = 'Tabuada do dois... {}... {}... {}... {}... {}... {}... {}... {}... {}... {}'.format(
        'dois vezes um é igual a dois', 'dois vezes dois é igual a quatro',
        'dois vezes três é igual a seis', 'dois vezes quatro é igual a oito', 
        'dois vezes cinco é igual a dez', 'duas vezes seis é igual a doze',
        'duas vezes sete é igual a quatorze', 'duas vezes oito é igual a dezesseis', 
        'duas vezes nove é igual a dezoito','duas vezes dez é igual a vinte')

        return answer
    
    @staticmethod
    def get_multiplThree():
        answer = 'Tabuada do três... {}... {}... {}... {}... {}... {}... {}... {}... {}... {}'.format(
        'três vezes um é igual a três', 'três vezes dois é igual a seis',
        'três vezes três é igual a nove', 'três vezes quatro é igual a doze', 
        'três vezes cinco é igual a quinze', 'três vezes seis é igual a dezoito',
        'três vezes sete é igual a vinte e um', 'três vezes oito é igual a vinte e quatro', 
        'três vezes nove é igual a vinte e sete','três vezes dez é igual a trinta')

        return answer

    @staticmethod
    def get_multiplFour():
        answer = 'Tabuada do quatro... {}... {}... {}... {}... {}... {}... {}... {}... {}... {}'.format(
        'quatro vezes um é igual a quatro', 'quatro vezes dois é igual a oito',
        'quatro vezes três é igual a doze', 'quatro vezes quatro é igual a dezesseis', 
        'quatro vezes cinco é igual a vinte', 'quatro vezes seis é igual a vinte e quatro',
        'quatro vezes sete é igual a vinte e oito', 'quatro vezes oito é igual a trinta e dois', 
        'quatro vezes nove é igual a trinta e seis','quatro vezes dez é igual a quarenta')

        return answer

    @staticmethod
    def get_multiplFive():
        answer = 'Tabuada do cinco... {}... {}... {}... {}... {}... {}... {}... {}... {}... {}'.format(
        'cinco vezes um é igual a cinco', 'cinco vezes dois é igual a dez',
        'cinco vezes três é igual a quinze', 'cinco vezes quatro é igual a vinte', 
        'cinco vezes cinco é igual a vinte e cinco', 'cinco vezes seis é igual a trinta',
        'cinco vezes sete é igual a trinta e cinco', 'cinco vezes oito é igual a quarenta', 
        'cinco vezes nove é igual a quarenta e cinco','cinco vezes dez é igual a cinquenta')

        return answer

    @staticmethod
    def get_multiplSix():
        answer = 'Tabuada do seis... {}... {}... {}... {}... {}... {}... {}... {}... {}... {}'.format(
        'seis vezes um é igual a seis', 'seis vezes dois é igual a doze',
        'seis vezes três é igual a dezoito', 'seis vezes quatro é igual a vinte e quatro', 
        'seis vezes cinco é igual a trinta', 'seis vezes seis é igual a trinta e seis',
        'seis vezes sete é igual a quarenta e dois', 'seis vezes oito é igual a quarenta e oito', 
        'seis vezes nove é igual a cinquenta e quatro','seis vezes dez é igual a sessenta')

        return answer

    @staticmethod
    def get_multiplSeven():
        answer = 'Tabuada do sete... {}... {}... {}... {}... {}... {}... {}... {}... {}... {}'.format(
        'sete vezes um é igual a sete', 'sete vezes dois é igual a quatorze',
        'sete vezes três é igual a vinte e um', 'sete vezes quatro é igual a vinte e oito', 
        'sete vezes cinco é igual a trinta e cinco', 'sete vezes seis é igual a quarenta e dois',
        'sete vezes sete é igual a quarenta e nove', 'sete vezes oito é igual a cinquenta e seis', 
        'sete vezes nove é igual a sessenta e três','sete vezes dez é igual a setenta')

        return answer
    
    @staticmethod
    def get_multiplEight():
        answer = 'Tabuada do oito... {}... {}... {}... {}... {}... {}... {}... {}... {}... '.format(
        "oito vezes um é igual a oito", "oito vezes dois é igual a dezesseis",
        "oito vezes três é igual a vinte e quatro", "oito vezes quatro é igual a trinta e dois",
        "oito vezes cinco é igual a quarenta", "oito vezes seis é igual a quarenta e oito",
        "oito vezes sete é igual a cinquenta e seis", "oito vezes oito é igual a sessenta e quatro", 
        "oito vezes nove é igual a setenta e dois","oito vezes dez é igual a oitenta")

        return answer

    @staticmethod
    def get_multiplNine():
        answer = 'Tabuada do nove... {}... {}... {}... {}... {}... {}... {}... {}... {}... '.format(
        "nove vezes um é igual a nove", "nove vezes dois é igual a dezoito",
        "nove vezes três é igual a vinte e sete", "nove vezes quatro é igual a trinta e seis",
        "nove vezes cinco é igual a quarenta e cinco", "nove vezes seis é igual a cinquenta e quatro",
        "nove vezes sete é igual a sessenta e três", "nove vezes oito é igual a setenta e dois", 
        "nove vezes nove é igual a oitenta e um","nove vezes dez é igual a noventa")
            
        return answer

    @staticmethod
    def get_multiplTen():
        answer = 'Tabuada do dez... {}... {}... {}... {}... {}... {}... {}... {}... {}... '.format(
        "dez vezes um é igual a dez", "dez vezes dois é igual a vinte",
        "dez vezes três é igual a trinta", "dez vezes quatro é igual a quarenta",
        "dez vezes cinco é igual a cinquenta", "dez vezes seis é igual a sessenta",
        "dez vezes sete é igual a setenta", "dez vezes oito é igual a oitenta", 
        "dez vezes nove é igual a noventa","dez vezes dez é igual a cem")
            
        return answer

    # Multiplicando números
    @staticmethod
    def get_oneMultiplOne():
        answer = 'um vezes um é igual a um'
        
        return answer

    @staticmethod
    def get_oneMultiplTwo():
        answer = 'um vezes dois é igual a dois'

        return answer

    @staticmethod
    def get_oneMultiplThree():
        answer = 'um vezes três é igual a três'

        return answer

    @staticmethod
    def get_oneMultiplFour():
        answer = 'um vezes quatro é igual a quatro'

        return answer

    @staticmethod
    def get_oneMultiplFive():
        answer = 'um vezes cinco é igual a cinco'

        return answer

    @staticmethod
    def get_oneMultiplSix():
        answer = 'um vezes seis é igual a seis'

        return answer

    @staticmethod
    def get_oneMultiplSeven():
        answer = 'um vezes sete é igual a sete'

        return answer

    @staticmethod
    def get_oneMultiplEight():
        answer = 'um vezes oito é igual a oito'
        
        return answer

    @staticmethod
    def get_oneMultiplNine():
        answer = 'um vezes nove é igual a nove'
    
        return answer

    @staticmethod
    def get_oneMultiplTen():
        answer = 'um vezes dez é igual a dez'

        return answer

    @staticmethod
    def get_twoMultiplOne():
        answer = 'dois vezes um é igual a dois'

        return answer

    @staticmethod
    def get_twoMultiplTwo():
        answer = 'dois vezes dois é igual a quatro'

        return answer

    @staticmethod
    def get_twoMultiplThree():
        answer = 'dois vezes três é igual a seis'

        return answer

    @staticmethod
    def get_twoMultiplFour():
        answer = 'dois vezes quatro é igual a oito'

        return answer

    @staticmethod
    def get_twoMultiplFive():
        answer = 'dois vezes cinco é igual a dez'

        return answer

    @staticmethod
    def get_twoMultiplSix():
        answer = 'dois vezes seis é igual a doze'

        return answer

    @staticmethod
    def get_twoMultiplSeven():
        answer = 'dois vezes sete é igual a quatorze'

        return answer

    @staticmethod
    def get_twoMultiplEight():
        answer = 'dois vezes oito é igual a dezesseis'

        return answer

    @staticmethod
    def get_twoMultiplNine():
        answer = 'dois vezes nove é igual a dezoito'

        return answer

    @staticmethod
    def get_twoMultiplTen():
        answer = 'dois vezes dez é igual a vinte'

        return answer

    @staticmethod
    def get_threeMultiplOne():
        answer = 'três vezes um é igual a três'

        return answer

    @staticmethod
    def get_threeMultiplTwo():
        answer = 'três vezes dois é igual a seis'

        return answer

    @staticmethod
    def get_threeMultiplThree():
        answer = 'três vezes três é igual a nove'

        return answer

    @staticmethod
    def get_threeMultiplFour():
        answer = 'três vezes quatro é igual a doze'

        return answer

    @staticmethod
    def get_threeMultiplFive():
        answer = 'três vezes cinco é igual a quinze'

        return answer

    @staticmethod
    def get_threeMultiplSix():
        answer = 'três vezes seis é igual a dezoito'

        return answer

    @staticmethod
    def get_threeMultiplSeven():
        answer = 'três vezes sete é igual a vinte e um'

        return answer

    @staticmethod
    def get_threeMultiplEight():
        answer = 'três vezes oito é igual a vinte e quatro'

        return answer

    @staticmethod
    def get_threeMultiplNine():
        answer = 'três vezes nove é igual a vinte e sete'

        return answer

    @staticmethod
    def get_threeMultiplTen():
        answer = 'três vezes dez é igual a trinta'

        return answer

    @staticmethod
    def get_fourMultiplOne():
        answer = 'quatro vezes um é igual a quatro'

        return answer

    @staticmethod
    def get_fourMultiplTwo():
        answer = 'quatro vezes dois é igual a oito'

        return answer

    @staticmethod
    def get_fourMultiplThree():
        answer = 'quatro vezes três é igual a doze'

        return answer

    @staticmethod
    def get_fourMultiplFour():
        answer = 'quatro vezes quatro é igual a dezesseis'

        return answer

    @staticmethod
    def get_fourMultiplFive():
        answer = 'quatro vezes cinco é igual a vinte'

        return answer

    @staticmethod
    def get_fourMultiplSix():
        answer = 'quatro vezes seis é igual a vinte e quatro'

        return answer

    @staticmethod
    def get_fourMultiplSeven():
        answer = 'quatro vezes sete é igual a vinte e oito'

        return answer

    @staticmethod
    def get_fourMultiplEight():
        answer = 'quatro vezes oito é igual a trinta e dois'

        return answer

    @staticmethod
    def get_fourMultiplNine():
        answer = 'quatro vezes nove é igual a trinta e seis'

        return answer

    @staticmethod
    def get_fourMultiplTen():
        answer = 'quatro vezes dez é igual a quarenta'

        return answer
