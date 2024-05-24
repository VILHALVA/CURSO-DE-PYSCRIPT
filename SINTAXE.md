# SINTAXE
A sintaxe do PyScript é bastante simples e segue padrões familiares para quem já está acostumado a programar em Python. Aqui está um exemplo básico de como seria a sintaxe do PyScript incorporada em um arquivo HTML:

```html
<!DOCTYPE html>
<html>
<head>
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <py-script class="text-center"> print('Hello, World!') </py-script>
        <py-script> print('Hello, World!') </py-script>
        <py-script> print('Hello, World!') </py-script>
    </div>
</body>
</html>
```

Neste exemplo:

- O código Python dentro do script é escrito normalmente, seguindo as convenções da linguagem.
- Você pode definir funções, variáveis, realizar operações, interagir com o DOM (Document Object Model) e muito mais, tudo usando Python.
- O PyScript é então incluído na página através de uma tag `<py-script>` com o atributo `src` apontando para a CDN onde o arquivo JavaScript do PyScript está hospedado.

Essa é apenas uma visão geral básica da sintaxe. À medida que você avança no desenvolvimento com o PyScript, você encontrará recursos mais avançados e maneiras de aproveitar ao máximo essa ferramenta.