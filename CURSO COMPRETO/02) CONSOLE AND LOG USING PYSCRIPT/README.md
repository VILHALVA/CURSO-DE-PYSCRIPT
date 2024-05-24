# CONSOLE AND LOG USING PYSCRIPT

```html
<!DOCTYPE html>
<html>
<head>
    <!-- Carrega a biblioteca PyScript -->
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>
<body>
    <h1>Welcome to Python Compiler</h1>
    <p>PyScript is Awesome</p>
    <py-script>
        from js import console
        console.log("Console Log from PyScript")
        console.warn("Console Warn from PyScript")
        console.error("Console Error from PyScript")
        console.info("Console Info from PyScript")
    </py-script>
</body>
</html>
```

## Explicação:
1. **Cabeçalho (`<head>`)**:
    ```html
    <head>
        <!-- Carrega a biblioteca PyScript -->
        <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    </head>
    ```
    - A linha `<script defer src="https://pyscript.net/alpha/pyscript.js"></script>` carrega a biblioteca PyScript, permitindo a execução de código Python diretamente no navegador. A palavra-chave `defer` garante que o script seja executado apenas após a página HTML ter sido carregada completamente.

2. **Corpo (`<body>`)**:
    ```html
    <body>
        <h1>Welcome to Python Compiler</h1>
        <p>PyScript is Awesome</p>
        <py-script>
            from js import console
            console.log("Console Log from PyScript")
            console.warn("Console Warn from PyScript")
            console.error("Console Error from PyScript")
            console.info("Console Info from PyScript")
        </py-script>
    </body>
    ```
    - **Título e Parágrafo**:
        ```html
        <h1>Welcome to Python Compiler</h1>
        <p>PyScript is Awesome</p>
        ```
        Esses elementos exibem um título e um parágrafo de introdução na página.

    - **Bloco `py-script`**:
        ```html
        <py-script>
            from js import console
            console.log("Console Log from PyScript")
            console.warn("Console Warn from PyScript")
            console.error("Console Error from PyScript")
            console.info("Console Info from PyScript")
        </py-script>
        ```
        Dentro deste bloco, você pode escrever código Python que será executado no navegador:

        - `from js import console`: Importa o objeto `console` da API JavaScript, permitindo o uso das funções do console do navegador dentro do Python.
        - `console.log("Console Log from PyScript")`: Envia uma mensagem de log normal para o console.
        - `console.warn("Console Warn from PyScript")`: Envia uma mensagem de aviso para o console.
        - `console.error("Console Error from PyScript")`: Envia uma mensagem de erro para o console.
        - `console.info("Console Info from PyScript")`: Envia uma mensagem informativa para o console.

## Resultado Esperado
Após carregar esta página HTML em um navegador que suporta PyScript, você verá o título e o parágrafo exibidos na página. Ao abrir o console do navegador (geralmente pressionando F12 ou Ctrl+Shift+I), você verá as seguintes mensagens:

- `Console Log from PyScript` como uma mensagem de log normal.
- `Console Warn from PyScript` como uma mensagem de aviso.
- `Console Error from PyScript` como uma mensagem de erro.
- `Console Info from PyScript` como uma mensagem informativa.

## Utilidade
Este exemplo é útil para entender como PyScript pode interagir com APIs JavaScript nativas do navegador, permitindo a manipulação direta do console do navegador através de código Python. Essa funcionalidade pode ser expandida para utilizar outras APIs JavaScript, proporcionando uma integração rica entre Python e JavaScript no contexto de desenvolvimento web.