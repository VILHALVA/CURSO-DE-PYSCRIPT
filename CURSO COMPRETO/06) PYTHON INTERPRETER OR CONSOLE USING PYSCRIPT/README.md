# PYTHON INTERPRETER OR CONSOLE USING PYSCRIPT
```html
<!DOCTYPE html>
<html>
<head>
    <!-- <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" /> -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>
<body>
    <div class="container p-5">
        <h1>PyScript py-repl</h1>
        <py-repl auto-generate="true"></py-repl>
    </div>
</body>
</html>
```

## Explicação
1. **Cabeçalho (`<head>`)**:
    ```html
    <head>
        <!-- <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" /> -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    </head>
    ```
    - **Bootstrap CSS**: Inclui a biblioteca CSS Bootstrap para estilização da página.
    - **PyScript**: Carrega a biblioteca PyScript, permitindo a execução de código Python no navegador.

2. **Corpo (`<body>`)**:
    ```html
    <body>
        <div class="container p-5">
            <h1>PyScript py-repl</h1>
            <py-repl auto-generate="true"></py-repl>
        </div>
    </body>
    ```
    - **Container Div**:
        ```html
        <div class="container p-5">
        ```
        Define um contêiner com padding para centralizar o conteúdo e aplicar estilo.

    - **Título**:
        ```html
        <h1>PyScript py-repl</h1>
        ```
        Exibe o título da página.

    - **Componente `py-repl`**:
        ```html
        <py-repl auto-generate="true"></py-repl>
        ```
        Cria um ambiente de REPL interativo onde os usuários podem digitar e executar código Python diretamente no navegador.

## Componente `py-repl`
O `py-repl` é um componente especial do PyScript que permite a execução de código Python de forma interativa. Atributos importantes:

- **`auto-generate="true"`**: Este atributo gera automaticamente uma interface de REPL na página, onde os usuários podem escrever e executar código Python. Sem este atributo, o REPL precisa ser configurado manualmente.

## Conclusão
Este exemplo ilustra como criar uma interface REPL interativa com PyScript, permitindo que os usuários escrevam e executem código Python diretamente em uma página web. É uma ferramenta poderosa para ensino, aprendizado e experimentação com Python, tudo dentro do ambiente do navegador. O uso de Bootstrap melhora a aparência da página, proporcionando uma experiência de usuário mais agradável.