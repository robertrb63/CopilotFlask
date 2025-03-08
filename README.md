Título: Aplicación de Gestión de Productos BARMON

Descripción: Tu aplicación es una plataforma desarrollada con Flask que permite a los usuarios gestionar una lista de productos. Incluye funcionalidades como agregar productos con detalles personalizados (nombre, imagen, precio, lugar y precio con descuento), buscar productos por nombre y mostrar los resultados en una página específica. Todo esto se complementa con un diseño atractivo y responsivo, usando CSS personalizado y Bootstrap.

Características principales:

Interfaz de Usuario:

Un banner en la parte superior que muestra el título "BARMON".

Un carrusel (carousel) en el encabezado que presenta imágenes desplazables.

Productos organizados en un diseño de cuadrícula de 4 columnas en la página principal.

Funcionalidades de Backend:

Un formulario para agregar productos con todos sus detalles.

Almacenamiento de los productos en un archivo JSON para mantener los datos persistentes.

Ruta de búsqueda para filtrar productos según el término ingresado.

Diseño Visual:

Uso de CSS para personalizar la apariencia de los elementos (como centrar contenido, establecer dimensiones y estilizar componentes).

Bootstrap para componentes dinámicos como el carrusel y un diseño responsivo.

Tecnologías Usadas:

Python (Flask): Framework backend para manejar las rutas, la lógica de negocio y la persistencia de datos.

Jinja2: Motor de plantillas para renderizar el contenido dinámico en HTML.

HTML/CSS: Desarrollo de la interfaz de usuario.

JSON: Almacenamiento local de los productos.

Bootstrap: Framework CSS para diseño responsivo y componentes dinámicos

tu_proyecto/
├── app.py            # Archivo principal de la aplicación Flask
├── data.json         # Archivo para almacenar los datos de los productos
├── templates/        # Carpeta para las plantillas HTML
│   ├── index.html    # Página principal
│   ├── busqueda.html # Página de resultados de búsqueda
├── static/           # Carpeta para archivos estáticos (CSS, imágenes)
│   └── styles.css    # Archivo CSS personalizado
└── requirements.txt  # Lista de dependencias del proyecto
