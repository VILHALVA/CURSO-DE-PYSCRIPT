# LOOP USING PYSCRIPT

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
        <div id="test-output" class="p-3"></div>
        <py-script>
            from js import console
            def my_function(*args, **kwargs):
                test_number = Element("test-input").element.value
                for i in range(int(test_number)):
                    console.log("hello ",i)
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
            <div id="test-output" class="p-3"></div>
            <py-script>
                from js import console
                def my_function(*args, **kwargs):
                    test_number = Element("test-input").element.value
                    for i in range(int(test_number)):
                        console.log("hello ", i)
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

    - **Div para Saída**:
        ```html
        <div id="test-output" class="p-3"></div>
        ```
        Cria um div vazio com o ID `test-output` para possível uso futuro, estilizado com padding pela classe `p-3`.

    - **Bloco `py-script`**:
        ```html
        <py-script>
            from js import console
            def my_function(*args, **kwargs):
                test_number = Element("test-input").element.value
                for i in range(int(test_number)):
                    console.log("hello ", i)
        </py-script>
        ```
        Este bloco contém o código Python executado pelo PyScript:

        - `from js import console`: Importa o objeto `console` da API JavaScript para permitir o uso de funções de log do console.
        
        - `def my_function(*args, **kwargs)`: Define a função `my_function` que será chamada quando o botão for clicado.

            - `test_number = Element("test-input").element.value`: Obtém o valor digitado no campo de entrada com o ID `test-input`.

            - `for i in range(int(test_number))`: Itera de 0 até o valor digitado.

                - `console.log("hello ", i)`: Registra a mensagem "hello" seguida do valor da iteração no console do navegador.

## Resultado Esperado
Quando você carrega esta página HTML em um navegador compatível com PyScript e digita um número no campo de entrada seguido de um clique no botão "Click me":

- A função `my_function` é chamada.
- O valor digitado é obtido do campo de entrada.
- Para cada número de 0 até o valor digitado, uma mensagem "hello " seguida pelo número é registrada no console do navegador.

## Conclusão
Este exemplo demonstra como capturar a entrada do usuário, iterar sobre um intervalo de números e usar a funcionalidade de console do JavaScript para registrar mensagens no navegador. Ele mostra a integração de PyScript com o DOM e como o Python pode ser usado para manipular diretamente elementos HTML e utilizar APIs do JavaScript.