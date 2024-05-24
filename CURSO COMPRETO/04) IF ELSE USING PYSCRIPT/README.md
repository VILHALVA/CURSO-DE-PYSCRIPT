# IF ELSE USING PYSCRIPT
```html
<!DOCTYPE html>
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>
<body>
    <div class="container text-center p-5">
        <h1>Input and Output</h1>
        <input type="number" id="test-input"/> 
        <button id="test-button" pys-onclick="my_function">Click me</button>
        <p id="test-output" class="p-3"></p>
        <py-script>
            def my_function(*args, **kwargs):
                test_number = Element("test-input").element.value
                if int(test_number) % 2 == 0:
                    Element("test-output").element.innerHTML = "Even"
                else:
                    Element("test-output").element.innerHTML = "Odd"
        </py-script>
    </div>
</body>
</html>
```

## Explicação
1. **Cabeçalho (`<head>`)**:
    ```html
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    </head>
    ```
    - **Bootstrap CSS**: Inclui a biblioteca CSS Bootstrap para estilização.
    - **PyScript**: Carrega a biblioteca PyScript, permitindo a execução de código Python no navegador.

2. **Corpo (`<body>`)**:
    ```html
    <body>
        <div class="container text-center p-5">
            <h1>Input and Output</h1>
            <input type="number" id="test-input"/> 
            <button id="test-button" pys-onclick="my_function">Click me</button>
            <p id="test-output" class="p-3"></p>
            <py-script>
                def my_function(*args, **kwargs):
                    test_number = Element("test-input").element.value
                    if int(test_number) % 2 == 0:
                        Element("test-output").element.innerHTML = "Even"
                    else:
                        Element("test-output").element.innerHTML = "Odd"
            </py-script>
        </div>
    </body>
    ```

    - **Container Div**:
        ```html
        <div class="container text-center p-5">
        ```
        Define um contêiner centralizado com padding.

    - **Título**:
        ```html
        <h1>Input and Output</h1>
        ```
        Exibe o título da página.

    - **Campo de Entrada**:
        ```html
        <input type="number" id="test-input"/> 
        ```
        Cria um campo de entrada de número com o ID `test-input`.

    - **Botão**:
        ```html
        <button id="test-button" pys-onclick="my_function">Click me</button>
        ```
        Cria um botão com o ID `test-button`. O atributo `pys-onclick="my_function"` associa o clique no botão à função `my_function` definida no PyScript.

    - **Parágrafo para Saída**:
        ```html
        <p id="test-output" class="p-3"></p>
        ```
        Cria um parágrafo com o ID `test-output` para exibir a saída. O parágrafo possui um padding aplicado pela classe `p-3`.

    - **Bloco `py-script`**:
        ```html
        <py-script>
            def my_function(*args, **kwargs):
                test_number = Element("test-input").element.value
                if int(test_number) % 2 == 0:
                    Element("test-output").element.innerHTML = "Even"
                else:
                    Element("test-output").element.innerHTML = "Odd"
        </py-script>
        ```
        Este bloco contém o código Python executado pelo PyScript:

        - `def my_function(*args, **kwargs)`: Define a função `my_function` que será chamada quando o botão for clicado.

            - `test_number = Element("test-input").element.value`: Obtém o valor digitado no campo de entrada com o ID `test-input`.

            - `if int(test_number) % 2 == 0`: Verifica se o número é par.
                - `Element("test-output").element.innerHTML = "Even"`: Define o texto do elemento com o ID `test-output` para "Even" se o número for par.

            - `else`: Se o número não for par.
                - `Element("test-output").element.innerHTML = "Odd"`: Define o texto do elemento com o ID `test-output` para "Odd" se o número for ímpar.

## Resultado Esperado
Quando você carrega esta página HTML em um navegador compatível com PyScript e digita um número no campo de entrada seguido de um clique no botão "Click me":

- A função `my_function` é chamada.
- O valor digitado é obtido do campo de entrada.
- O valor é verificado se é par ou ímpar.
- O resultado ("Even" ou "Odd") é exibido no parágrafo com o ID `test-output`.

## Conclusão
Este exemplo demonstra como capturar a entrada do usuário, processá-la e exibir o resultado usando PyScript. Ele mostra a integração de PyScript com o DOM e como o Python pode ser usado para manipular diretamente elementos HTML em uma página web.