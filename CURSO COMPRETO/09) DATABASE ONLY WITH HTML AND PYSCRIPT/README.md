# DATABASE ONLY WITH HTML AND PYSCRIPT 
```html
<!DOCTYPE html>
<html>
<head>
    <title>Web SQL Database with HTML and Javascript</title>
    <meta name="viewport" content="user-scalable=no,width=device-width" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    <py-script src="./database_handler.py"></py-script>
</head>
<body style="margin:30px">
    <div class="container">
        <h1 class="text-center">School of Thought</h1> 
        <h3 class="text-center pb-5">PyScript</h3> 

        <div class="row">
            <form>
                <fieldset>
                    <legend>Item Name</legend>
                    <input type="text" class="form-control" name="" id="item">

                    <legend>Quantity</legend>
                    <input type="number" class="form-control" id="quantity" name="">
                    <br>
                    <button type="button" id="insert" class="btn btn-success" pys-onClick="insert">Insert</button>

                    <button type="button" id="create" class="btn btn-success" pys-onClick="create">Create Table</button>

                    <button type="button" id="remove" class="btn btn-danger">Delete Table</button>

                    <button type="button" id="list" class="btn btn-success" pys-onClick="fetch">Fetch Record</button>
                    <p><small><b>Note:</b> Table must be created first before inserting or performing any
                            transaction</small></p>
                </fieldset>
            </form>
            <hr>
            <h4>Record</h4>
            <table class="table table-bordered table-hover" id="itemlist">
            </table>
        </div>
    </div>
</body>
</html>
```

## Script Python (`database_handler.py`):
```python
import sqlite3
from js import console

conn = sqlite3.connect('database.db')

def create(*args, **kwargs):
    conn.execute('''CREATE TABLE items
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    item_name           TEXT    NOT NULL,
    quantity            INT     NOT NULL)''')
    console.log("Table created")

def insert(*args, **kwargs):
    item = Element('item').element.value
    quantity = Element('quantity').element.value
    conn.execute("INSERT INTO items (item_name, quantity) VALUES ('{}', {})".format(item, quantity))
    console.log("Item inserted")

def fetch(*args, **kwargs):
    cursor = conn.execute("SELECT id, item_name, quantity FROM items")
    for row in cursor:
        console.log(row[0], row[1], row[2])
```

### Explicação do Código:
#### Cabeçalho (`<head>`):
- Inclui Bootstrap para estilização.
- Inclui PyScript para carregar e executar scripts Python diretamente no navegador.
- Carrega o script `database_handler.py`.

```html
<head>
    <title>Web SQL Database with HTML and Javascript</title>
    <meta name="viewport" content="user-scalable=no,width=device-width" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    <py-script src="./database_handler.py"></py-script>
</head>
```

#### Corpo (`<body>`):
- Cria um formulário para inserir `item` e `quantity`.
- Botões para criar a tabela, inserir dados e buscar registros.
- Tabela para exibir os registros.

```html
<body style="margin:30px">
    <div class="container">
        <h1 class="text-center">School of Thought</h1> 
        <h3 class="text-center pb-5">PyScript</h3> 

        <div class="row">
            <form>
                <fieldset>
                    <legend>Item Name</legend>
                    <input type="text" class="form-control" name="" id="item">

                    <legend>Quantity</legend>
                    <input type="number" class="form-control" id="quantity" name="">
                    <br>
                    <button type="button" id="insert" class="btn btn-success" pys-onClick="insert">Insert</button>

                    <button type="button" id="create" class="btn btn-success" pys-onClick="create">Create Table</button>

                    <button type="button" id="remove" class="btn btn-danger">Delete Table</button>

                    <button type="button" id="list" class="btn btn-success" pys-onClick="fetch">Fetch Record</button>
                    <p><small><b>Note:</b> Table must be created first before inserting or performing any
                            transaction</small></p>
                </fieldset>
            </form>
            <hr>
            <h4>Record</h4>
            <table class="table table-bordered table-hover" id="itemlist">
            </table>
        </div>
    </div>
</body>
```

## Script Python (`database_handler.py`):
- **Importações e Conexão**: Importa `sqlite3` para manipulação do banco de dados e `console` para logs no navegador. Cria uma conexão com `database.db`.

```python
import sqlite3
from js import console

conn = sqlite3.connect('database.db')
```

- **Função `create`**: Cria uma tabela `items` com colunas `id`, `item_name` e `quantity`. Loga no console do navegador que a tabela foi criada.

```python
def create(*args, **kwargs):
    conn.execute('''CREATE TABLE items
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    item_name           TEXT    NOT NULL,
    quantity            INT     NOT NULL)''')
    console.log("Table created")
```

- **Função `insert`**: Insere um item e sua quantidade na tabela `items`. Loga no console que o item foi inserido.

```python
def insert(*args, **kwargs):
    item = Element('item').element.value
    quantity = Element('quantity').element.value
    conn.execute("INSERT INTO items (item_name, quantity) VALUES ('{}', {})".format(item, quantity))
    console.log("Item inserted")
```

- **Função `fetch`**: Busca e loga no console todos os registros da tabela `items`.

```python
def fetch(*args, **kwargs):
    cursor = conn.execute("SELECT id, item_name, quantity FROM items")
    for row in cursor:
        console.log(row[0], row[1], row[2])
```

## Conclusão
Este exemplo mostra como usar PyScript para interagir com um banco de dados SQLite diretamente em uma página web. A combinação de HTML, Bootstrap, e PyScript permite criar uma interface amigável e funcional para gerenciar dados, demonstrando a versatilidade e o poder do PyScript em aplicações web.