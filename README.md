# Sistema MQTT com Flask, Paho-MQTT e SQLAlchemy

## Descrição
Este projeto é um sistema MQTT desenvolvido utilizando Flask, Paho-MQTT e SQLAlchemy. Ele permite a comunicação entre dispositivos IoT através do protocolo MQTT e armazena dados em um banco de dados relacional.

## Tecnologias Utilizadas
- **Flask**: Um micro framework para desenvolvimento web em Python.
- **Paho-MQTT**: Biblioteca cliente MQTT para Python.
- **SQLAlchemy**: Biblioteca de ORM (Object-Relational Mapping) para Python.

## Instalação
1. Clone o repositório:
    ```bash
    git clone https://github.com/danilotec/sistema_mqtt.git
    cd sistema_mqtt
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Configuração
1. Configure as variáveis de ambiente necessárias no arquivo `.env`:
    ```plaintext
    exemplo no .env-example
    ```

## Uso
1. Inicie o servidor Flask:
    ```bash
    python run.py
    ```

2. O sistema estará disponível em `http://127.0.0.1:5000/`.


## Contribuição
1. Faça um fork do projeto.
2. Crie uma nova branch: `git checkout -b minha-nova-feature`.
3. Faça suas alterações e commit: `git commit -m 'Adiciona nova feature'`.
4. Envie para o repositório remoto: `git push origin minha-nova-feature`.
5. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.