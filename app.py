from flask import Flask, request, redirect, url_for, render_template
import json

app = Flask(__name__)

# Ruta principal que muestra todos los productos
@app.route('/')
def index():
    try:
        with open('data.json', 'r') as f:
            productos = json.load(f)
    except FileNotFoundError:
        productos = []
    return render_template('index.html', productos=productos)

# Ruta que procesa el formulario para agregar un nuevo producto
@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form.get('nombre')
    imagen = request.form.get('imagen')
    precio = request.form.get('precio')
    lugar = request.form.get('lugar')
    precio_descuento = request.form.get('precio_descuento')

    producto = {
        "nombre": nombre,
        "imagen": imagen,
        "precio": precio,
        "lugar": lugar,
        "precio_descuento": precio_descuento
    }

    try:
        with open('data.json', 'r') as f:
            productos = json.load(f)
    except FileNotFoundError:
        productos = []

    productos.append(producto)

    with open('data.json', 'w') as f:
        json.dump(productos, f, indent=4)

    return redirect(url_for('index'))

# Ruta de búsqueda de productos
@app.route('/buscar')
def buscar():
    query = request.args.get('q', '')
    # Cargar productos
    try:
        with open('data.json', 'r') as f:
            productos = json.load(f)
    except FileNotFoundError:
        productos = []

    # Filtrar los productos que incluyen el término de búsqueda en el nombre
    resultados = [p for p in productos if query.lower() in p.get('nombre', '').lower()]

    # Renderizar una plantilla con los resultados
    return render_template('busqueda.html', query=query, resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)

