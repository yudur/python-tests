import requests


class Person:
    def __init__(self, first_name, last_name, data_obtained=False):
        self.first_name = first_name
        self.last_name = last_name
        self.data_obtained = data_obtained

    def get_all_data(self):
        answer = requests.get('https://translate.google.com.br/?hl=pt-BR')

        if answer.ok:
            self.data_obtained = True
            return 'CONECTADO'
        else:
            self.data_obtained = False
            return 'ERRO 404'