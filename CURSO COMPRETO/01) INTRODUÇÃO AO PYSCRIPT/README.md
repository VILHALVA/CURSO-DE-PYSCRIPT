# INTRODUÇÃO AO PYSCRIPT
PyScript é uma estrutura que permite aos desenvolvedores integrar scripts Python diretamente em páginas HTML, possibilitando a execução de código Python no navegador, similarmente ao JavaScript. Ele utiliza Pyodide, um projeto que carrega o intérprete CPython compilado para WebAssembly, permitindo que bibliotecas Python sejam executadas no ambiente do navegador.

## Código HTML Completo:
```html
<!DOCTYPE html>
<html>
<head>
    <!-- Carrega o PyScript -->
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    <!-- CSS do Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>

<body>
    <div class="container">
        <h1>My First Heading</h1>
        <p>My first paragraph.</p>

        <!-- Elementos PyScript que imprimem 'Hello, World!' -->
        <py-script class="text-center"> print('Hello, World!') </py-script>
        <py-script> print('Hello, World!') </py-script>
        <py-script> print('Hello, World!') </py-script>
    </div>
</body>
</html>
```

## Explicação do Código
1. **Estrutura Básica do HTML**:
    ```html
    <!DOCTYPE html>
    <html>
    ```
    Define o documento como HTML5.

2. **Cabeçalho (`<head>`)**:
    ```html
    <head>
        <!-- Carrega o PyScript -->
        <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
        <!-- CSS do Bootstrap -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
    ```
    - **PyScript**: A linha `<script defer src="https://pyscript.net/alpha/pyscript.js"></script>` carrega a biblioteca PyScript, permitindo o uso de código Python diretamente no HTML.
    - **Bootstrap**: A linha `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">` carrega o CSS do Bootstrap, uma biblioteca de CSS popular para estilização.

3. **Corpo (`<body>`)**:
    ```html
    <body>
        <div class="container">
            <h1>My First Heading</h1>
            <p>My first paragraph.</p>

            <!-- Elementos PyScript que imprimem 'Hello, World!' -->
            <py-script class="text-center"> print('Hello, World!') </py-script>
            <py-script> print('Hello, World!') </py-script>
            <py-script> print('Hello, World!') </py-script>
        </div>
    </body>
    ```
    - **Container**: O `<div class="container">` é um contêiner Bootstrap que centraliza o conteúdo na página e aplica margens.
    - **Título e Parágrafo**: `<h1>My First Heading</h1>` e `<p>My first paragraph.</p>` são elementos HTML padrão que exibem um título e um parágrafo.
    - **Elementos PyScript**:
    ```html
    <py-script class="text-center"> print('Hello, World!') </py-script>
    <py-script> print('Hello, World!') </py-script>
    <py-script> print('Hello, World!') </py-script>
    ```
    Esses elementos contêm código Python que será executado pelo PyScript. O primeiro tem uma classe `text-center` que, teoricamente, deveria centralizar o texto (embora `print` não gere um elemento visual que possa ser estilizado com `text-center`).

## Considerações Adicionais:
1. **Uso do `print`**: Em PyScript, a função `print` não imprime no console do navegador como no ambiente de desenvolvimento, mas sim na página web. Cada `py-script` vai imprimir "Hello, World!" no documento HTML.

2. **Estilização com Bootstrap**: Embora o exemplo inclua Bootstrap, ele não afeta diretamente o output de `print` em PyScript. O Bootstrap é útil para estilizar outros elementos HTML na página.

3. **Possível Melhoramento**: Para realmente ver o efeito da centralização e estilização, podemos usar elementos de saída PyScript, como `Element.write()`, para inserir texto estilizado diretamente em elementos HTML.

Vamos melhorar o exemplo para centralizar e estilizar o texto corretamente:

### Exemplo Melhorado:
```html
<!DOCTYPE html>
<html>

<head>
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>

<body>
    <div class="container text-center">
        <h1>My First Heading</h1>
        <p>My first paragraph.</p>

        <!-- Espaço reservado para o output -->
        <div id="output1"></div>
        <div id="output2"></div>
        <div id="output3"></div>

        <py-script>
            from pyscript import Element

            Element("output1").write("Hello, World!")
            Element("output2").write("Hello, World!")
            Element("output3").write("Hello, World!")
        </py-script>
    </div>
</body>

</html>
```

### Explicação do Exemplo Melhorado:
1. **Container com Centralização**: O `div` com `class="container text-center"` centraliza todo o conteúdo dentro do contêiner.
2. **Elementos de Saída**: Adicionamos três `div` com IDs (`output1`, `output2`, `output3`) para serem usados como espaço reservado para o output.
3. **Uso de `Element.write()`**: No PyScript, usamos `Element("output1").write("Hello, World!")` para escrever "Hello, World!" dentro do respectivo `div`.

Com essas mudanças, o texto "Hello, World!" será corretamente inserido e centralizado na página, demonstrando o uso de PyScript com estilização Bootstrap.