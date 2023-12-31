# Back-End

Este projeto é um Acervo Digital de livros, desenvolvido com o objetivo de entregar um MVP com funcionalidades integradas ao front-end.

---
## Como executar 

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Execute o seguinte comando para utilizar o ambiente virtual.

```
(Unix/macOS)
$ source env/Scripts/activate

(Windows)
$ .\env\Scripts\activate
```

Agora, estando no ambiente virtual, execute o comando abaixo

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.


> Caso ocorra algum erro de instalação com greenlet, execute o seguinte comando:

```
(env)$ pip install greenlet
```

Este comando instala a biblioteca, chamada Greenlet que permite a execução de tarefas concorrentes de forma controlada em um único thread.


Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução. 
