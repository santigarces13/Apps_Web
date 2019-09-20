	
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Desarrollador @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Santiago Garcés @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Aplicacion Veterinaria. 

    Aplicaciones necesarias: 
        -Python 3.6. 
        -Gestor de bade de datos como por ejemplo mysql, postgres u otro. Para esta app se usa postgres
        por ello se instala el complemento u conector de postgres en el entorno virtual.

    1.Crear un entorno virtual:
    #python venv -m NombreDelEntorno

    2.Activar el entorno por cmd en Windows o por teminal en Linux:
    Windows: #.\Script\activate
    Linux: #source bin/activate

    3.Instalar complementos para django en el entorno:
        #pip install Django==1.10
        #pip install psycopg2-binary
        #pip install Pillow==6.1.0
        #pip install pytz==2019.2
        #pip installreportlab==3.5.23
        #pip install sqlparse==0.3.0
    4.Copiar la carpeta src en su entorno virtual. 

    5.Abrir el src en un editor de texto, una vez abierto el src buscar la carpeta probar para editar
    el settings.py. 
    Cambiar en settings.py la cadena de conexi´ón (Línea 93), nombre de la base de datos, 
    nombre del usuario, contraseña, host y puerto.

    6.Hacer migraciones a la base de datos desde el cmd en Windows o terminal en Linux.
    Acceder a la carpeta src desde el cmd en Windows o terminal en Linux y colocar el siguiente
    código en el cmd en Windows o terminal en Linux: 
        Windows: #python manage.py migrate
        Linux: #python manage.py migrate

    7.Collect static desde el cmd en Windows o terminal en Linux:
        Windows: #python manage.py collectstatic
        Linux: #python manage.py collectstatic

    8.Crear super usuario desde el cmd en Windows o terminal en Linux:
        Windows: #python manage.py createsuperuser
        Linux: #python manage.py createsuperuser

    9.Inicializar el servidor desde el cmd en Windows o terminal en Linux:
        Windows: #python manage.py runserver
        Linux: #python manage.py runserver
    






