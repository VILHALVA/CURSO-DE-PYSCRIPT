# IMPORT PYTHON FILE IN PYSCRIPT
```html
<!DOCTYPE html>
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    <py-env>
        - paths:
          - random_n.py
    </py-env>
</head>
<body>
    <div class="container p-5">
        <h1>PyScript Python File Import</h1>
        <py-script src="./our_script.py"></py-script>
        <input type="number" id="test-input" name="file" />
        <button type="button" id="test-button" pys-onclick="my_function">Test</button>
        <p id="test-output"></p>
        <py-script>
            from random_n import random_number
            print(random_number())
        </py-script>
    </div>
</body>
</html>
```

## Explicação dos Arquivos Python:
**`random_n.py`**:
```python
import random

def random_number():
    return random.randint(1, 10)
```

**`our_script.py`**:
```python
def my_function(*args, **kwargs):
    test_number = Element("test-input").element.value
    if int(test_number) % 2 == 0:
        Element("test-output").element.innerHTML = "Even"
    else:
        Element("test-output").element.innerHTML = "Odd"
```

## Explicação dos codigos:
1. **Cabeçalho (`<head>`)**:
    ```html
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
        <py-env>
            - paths:
              - random_n.py
        </py-env>
    </head>
    ```
    - **Bootstrap**: Inclui o Bootstrap para estilização.
    - **PyScript**: Carrega a biblioteca PyScript.
    - **`<py-env>`**: Define as dependências e caminhos dos arquivos Python que serão utilizados. Aqui, especificamos o arquivo `random_n.py`.

2. **Corpo (`<body>`)**:
    ```html
    <body>
        <div class="container p-5">
            <h1>PyScript Python File Import</h1>
            <py-script src="./our_script.py"></py-script>
            <input type="number" id="test-input" name="file" />
            <button type="button" id="test-button" pys-onclick="my_function">Test</button>
            <p id="test-output"></p>
            <py-script>
                from random_n import random_number
                print(random_number())
            </py-script>
        </div>
    </body>
    ```
    - **Container Bootstrap**: Utiliza classes do Bootstrap para estilização e formatação.
    - **Título**:
        ```html
        <h1>PyScript Python File Import</h1>
        ```
        Exibe o título da página.
    
    - **Importação de Script**:
        ```html
        <py-script src="./our_script.py"></py-script>
        ```
        Importa e executa o script `our_script.py`, que contém a definição da função `my_function`.

    - **Campo de Entrada e Botão**:
        ```html
        <input type="number" id="test-input" name="file" />
        <button type="button" id="test-button" pys-onclick="my_function">Test</button>
        <p id="test-output"></p>
        ```
        - Campo de entrada para número.
        - Botão que, ao ser clicado, executa a função `my_function`.
        - Parágrafo onde o resultado será exibido.

    - **Bloco `py-script`**:
        ```html
        <py-script>
            from random_n import random_number
            print(random_number())
        </py-script>
        ```
        - Importa e executa a função `random_number` do arquivo `random_n.py`.
        - Exibe o resultado da função `random_number()` no console.

## Conclusão
Este exemplo mostra como integrar arquivos Python externos em uma página web usando PyScript, permitindo a execução de código Python diretamente no navegador. A combinação de PyScript e Bootstrap proporciona uma interface estilizada e interativa, adequada para projetos que requerem visualizações dinâmicas e manipulação de dados.