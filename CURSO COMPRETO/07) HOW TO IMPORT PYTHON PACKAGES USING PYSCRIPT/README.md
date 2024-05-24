# HOW TO IMPORT PYTHON PACKAGES USING PYSCRIPT
```html
<!DOCTYPE html>
<html>
<head>
    <!-- <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" /> -->
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    <py-env>
        - numpy
        - matplotlib
    </py-env>
</head>
<body>
    <h1>My First Heading</h1>
    <div id="plot"></div>
    <py-script output="plot">
        import matplotlib.pyplot as plt
        import numpy as np

        x = np.random.randn(1000)
        y = np.random.randn(1000)

        fig, ax = plt.subplots()
        ax.scatter(x, y)
        fig
    </py-script>
</body>
</html>
```

## Explicação
1. **Cabeçalho (`<head>`)**:
    ```html
    <head>
        <!-- <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" /> -->
        <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
        <py-env>
            - numpy
            - matplotlib
        </py-env>
    </head>
    ```
    - **PyScript**: Carrega a biblioteca PyScript, permitindo a execução de código Python no navegador.
    - **`<py-env>`**: Define as dependências necessárias para o script Python. Neste caso, `numpy` e `matplotlib` são especificados.

2. **Corpo (`<body>`)**:
    ```html
    <body>
        <h1>My First Heading</h1>
        <div id="plot"></div>
        <py-script output="plot">
            import matplotlib.pyplot as plt
            import numpy as np

            x = np.random.randn(1000)
            y = np.random.randn(1000)

            fig, ax = plt.subplots()
            ax.scatter(x, y)
            fig
        </py-script>
    </body>
    ```
    - **Título**:
        ```html
        <h1>My First Heading</h1>
        ```
        Exibe o título da página.

    - **Div para o Gráfico**:
        ```html
        <div id="plot"></div>
        ```
        Cria um div com o ID `plot`, onde o gráfico será exibido.

    - **Bloco `py-script`**:
        ```html
        <py-script output="plot">
            import matplotlib.pyplot as plt
            import numpy as np

            x = np.random.randn(1000)
            y = np.random.randn(1000)

            fig, ax = plt.subplots()
            ax.scatter(x, y)
            fig
        </py-script>
        ```
        Este bloco contém o código Python executado pelo PyScript:

        - `import matplotlib.pyplot as plt`: Importa o módulo `pyplot` do Matplotlib, que fornece uma interface para criar gráficos.
        
        - `import numpy as np`: Importa o NumPy, uma biblioteca para computação numérica em Python.
        
        - `x = np.random.randn(1000)`: Gera uma array de 1000 números aleatórios com distribuição normal (média 0 e desvio padrão 1) para o eixo x.
        
        - `y = np.random.randn(1000)`: Gera uma array de 1000 números aleatórios com distribuição normal para o eixo y.
        
        - `fig, ax = plt.subplots()`: Cria uma figura (`fig`) e um conjunto de eixos (`ax`) para o gráfico.
        
        - `ax.scatter(x, y)`: Cria um gráfico de dispersão com os dados gerados aleatoriamente.
        
        - `fig`: Retorna a figura criada, que será exibida no div com o ID `plot`.

## Conclusão
Este exemplo demonstra como configurar e usar PyScript para exibir gráficos interativos diretamente em uma página web. Ao carregar as bibliotecas NumPy e Matplotlib como dependências, o PyScript permite a criação de visualizações de dados complexas no navegador, sem a necessidade de instalar essas bibliotecas localmente. Este método é útil para aplicações de ciência de dados, visualização de dados e educação, onde a interatividade e a simplicidade são cruciais.