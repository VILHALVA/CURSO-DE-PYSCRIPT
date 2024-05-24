# SIMPLE INPUT AND OUTPUT USING PYSCRIPT
```html
<!DOCTYPE html>
<html>
<head>
  <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>
<body>
    <div>Type an sample input here</div>
    <input type="text" id="test-input"/>
    <button id="submit-button" type="submit" pys-onClick="my_function">OK</button>
    <div id="test-output"></div>
  <py-script>
      from js import console

      def my_function(*args, **kwargs):
          console.log(f'args: {args}')
          console.log(f'kwargs: {kwargs}')
          
          text = Element('test-input').element.value
          console.log(f'text: {text}')

          Element('test-output').element.innerText = text
  </py-script>
</body>
</html>
```

## Explicação Linha por Linha:
1. **Cabeçalho (`<head>`)**:
    ```html
    <head>
        <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    </head>
    ```
    - Carrega a biblioteca PyScript, permitindo a execução de código Python no navegador. A palavra-chave `defer` garante que o script seja executado após a página HTML ser completamente carregada.

2. **Corpo (`<body>`)**:
    ```html
    <body>
        <div>Type an sample input here</div>
        <input type="text" id="test-input"/>
        <button id="submit-button" type="submit" pys-onClick="my_function">OK</button>
        <div id="test-output"></div>
        <py-script>
            from js import console

            def my_function(*args, **kwargs):
                console.log(f'args: {args}')
                console.log(f'kwargs: {kwargs}')
                
                text = Element('test-input').element.value
                console.log(f'text: {text}')

                Element('test-output').element.innerText = text
        </py-script>
    </body>
    ```
    - **Mensagem de Entrada**:
        ```html
        <div>Type an sample input here</div>
        ```
        Exibe uma mensagem orientando o usuário a digitar uma entrada.

    - **Campo de Entrada**:
        ```html
        <input type="text" id="test-input"/>
        ```
        Cria um campo de entrada de texto com o ID `test-input`.

    - **Botão de Envio**:
        ```html
        <button id="submit-button" type="submit" pys-onClick="my_function">OK</button>
        ```
        Cria um botão com o ID `submit-button`. O atributo `pys-onClick="my_function"` associa o clique no botão à função `my_function` definida no PyScript.

    - **Div para Saída**:
        ```html
        <div id="test-output"></div>
        ```
        Cria um div vazio com o ID `test-output` para exibir a saída.

    - **Bloco `py-script`**:
        ```html
        <py-script>
            from js import console

            def my_function(*args, **kwargs):
                console.log(f'args: {args}')
                console.log(f'kwargs: {kwargs}')
                
                text = Element('test-input').element.value
                console.log(f'text: {text}')

                Element('test-output').element.innerText = text
        </py-script>
        ```
        
        Este bloco contém o código Python executado pelo PyScript:

        - `from js import console`: Importa o objeto `console` da API JavaScript para permitir o uso de funções de log do console.
        
        - `def my_function(*args, **kwargs)`: Define a função `my_function` que será chamada quando o botão for clicado.

            - `console.log(f'args: {args}')` e `console.log(f'kwargs: {kwargs}')`: Registra os argumentos e palavras-chave recebidos pela função no console do navegador.

            - `text = Element('test-input').element.value`: Obtém o valor digitado no campo de entrada com o ID `test-input`.

            - `console.log(f'text: {text}')`: Registra o texto digitado no console do navegador.

            - `Element('test-output').element.innerText = text`: Define o texto do elemento com o ID `test-output` para o texto digitado pelo usuário, exibindo-o na página.

## Resultado Esperado
Quando você carrega esta página HTML em um navegador compatível com PyScript e digita algo no campo de texto seguido de um clique no botão "OK":

- A função `my_function` é chamada.
- O valor digitado é registrado no console do navegador.
- O texto digitado é exibido no div com o ID `test-output`.

## Conclusão
Este exemplo demonstra como capturar a entrada do usuário, manipulá-la e exibi-la usando PyScript. Ele mostra como PyScript pode ser usado para integrar Python diretamente em páginas web, interagindo com o DOM e utilizando funções JavaScript como o console do navegador.