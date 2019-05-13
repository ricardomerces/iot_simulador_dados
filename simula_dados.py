### Gerador de Dados (IoT) v1.0
### Ricardo Merces - Twitter: r_merces
### https://github.com/ricardomerces/iot_simulador_dados.git


import paho.mqtt.client as paho
import json
from random import randint
from time import sleep

cliente_mqtt = paho.Client('python-mqtt')

with open('config.json') as arquivo_configuracao:
    configuracao = json.load(arquivo_configuracao)

### Configuração --> Arquivo config.json
broker = configuracao['broker']
port = configuracao['port']
usuario = configuracao['usuario']
senha = configuracao['senha']
topico = configuracao['topico']
intervalo_publicacao = configuracao['intervalo_publicacao']


def configura_mqtt():
    cliente_mqtt.username_pw_set(username=usuario,password=senha)
    cliente_mqtt.connect(broker,port)
    cliente_mqtt.loop_start()

def publica_dados():
    while True:
        mensagem = randint(1,100)
        cliente_mqtt.publish(topico,mensagem, qos=1, retain=True)
        print(f'Mensagem: {mensagem}')
        sleep(intervalo_publicacao)

def main():
    configura_mqtt()
    publica_dados()

main()