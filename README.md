#Simulador de Dados (IoT)

### Dependências

[paho-mqtt](https://pypi.org/project/paho-mqtt/)

###Broker MQTT

[cloudmqtt.com](https://www.cloudmqtt.com)


###Arquivo de configuração

```config.json```

```
{
	"broker" : "postman.cloudmqtt.com",
	"port": 18848,
	"topico": "labs/mensagem",
	"intervalo_publicacao":1,
	"usuario":"XXXXXXX",
	"senha":"XXXXXXX"
}
```