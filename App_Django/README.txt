	
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Desarrollador @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Santiago Garcés @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Aplicación para hacer pedidos de materiales SENA.

    Aplicaciones necesarias: 
        -Python 3.6. 
        -Gestor de bade de datos como por ejemplo mysql, postgres u otro. Para esta app se usa mysql
        por ello se instala el complemento u conector de mysql en el entorno virtual.

    1.Crear un entorno virtual:
    #python venv -m NombreDelEntorno

    2.Activar el entorno por cmd en Windows o por teminal en Linux:
    Windows: #.\Script\activate
    Linux: #source bin/activate

    3.Instalar complementos para django en el entorno:
        #pip install Django==2.2.4
        #pip install django-filter==2.2.0
        #pip install mysqlclient==1.4.2.post1
        #pip install Pillow==6.1.0
        #pip install pytz==2019.2
        #pip installreportlab==3.5.23
        #pip install sqlparse==0.3.0
    4.Copiar la carpeta src_pedido y la carpeta static_env en su entorno virtual. 

    5.Abrir el src en un editor de texto, una vez abierto el src buscar la carpeta pedidos para editar
    el settings.py. 
    Cambiar en settings.py la cadena de conexión (Línea 93), nombre de la base de datos, 
    nombre del usuario, contraseña, host y puerto.

    6.Hacer migraciones a la base de datos desde el cmd en Windows o terminal en Linux.
    Acceder a la carpeta src_pedido desde el cmd en Windows o terminal en Linux y colocar el siguiente
    código en el cmd en Windows o terminal en Linux: 
        Windows: #python manage.py migrate
        Linux: #python manage.py migrate

    7.Collect static desde el cmd en Windows o terminal en Linux:
        Windows: #python manage.py collectstatic
        Linux: #python manage.py collectstatic

    8.Importar el script .sql a la base de datos.

    9.Crear super usuario desde el cmd en Windows o terminal en Linux:
        Windows: #python manage.py createsuperuser
        Linux: #python manage.py createsuperuser

    10.Inicializar el servidor desde el cmd en Windows o terminal en Linux:
        Windows: #python manage.py runserver
        Linux: #python manage.py runserver
    
Esta aplicacion fue desarrollada con los parametros necesarios para el SENA, como por ejemplo roles, areas,
materiales, estados de pedido entre otros.

Si se encuentra con algun error o problema contactar al correo del desarrollador: sgarce57@misena.edu.co 




