# BIENVENIDOS AL BACKEND DE ADMINISTRACIÓN DE PRODUCTOS

_Este proyecto tiene como objetivo crear, actualizar, borrar y consultar catalogos los cuales tienen asociados productos._

_La lógica de negocio es la siguiente: Primero se debe crear un SUPER ADMINISTRADOR este tiene todos los privilegios en
la API REST utilizando el CRUD, además puede cambiar el Rol de los USUARIOS ANÓNIMOS, después que se registran los cuales por
defecto son USUARIOS ANÓNIMOS, el SUPER ADMINISTRADOR puede cambiar el rol de estos a un perfil de ADMINISTRADORES y también
pueden eliminar a los USUARIOS ANÓNIMOS y a los ADMINISTRADORES registrados, por otro lado, los ADMINISTRADORES
tienen todos los privilegios del CRUD excepto que no pueden eliminar al SUPER ADMINISTRADOR , consultar todos los usuarios, ni tampoco eliminar a los usuarios,
si los ADMINISTRADORES o el SUPER ADMINISTRADOR actualizan cualquier producto, se le notificara al correo electrónico de cada uno de ellos
con el cual se registraron, y se notificara el cambio registrado.
Los USUARIOS ANÓNIMOS registrados pueden consultar todos los catálogos, los productos y cada uno de los productos, cuando se consulta
un producto en específico se guardara la información de la cantidad de veces que consulto el producto con el nombre de este y el nombre
de usuario que realizo la acción, los USUARIOS ANÓNIMOS no pueden actualizar, borrar y crear catálogos, productos y usuarios.
Para finalizar el PUBLICO EN GENERAL que no se registre en la API REST puede consultar todos los catálogos y todos los productos solamente_.

_Nota: Para todos los usuarios registrados incluyendo el SUPER ADMINISTRADOR , deben logearse y el token generado lo deben ingresar en el candado
de autorización, de esta manera tendra todas las funcionalidades de la API REST de acuerdo al perfil_.

![Aquí la descripción de la imagen por si no carga](https://raw.githubusercontent.com/ManuelOg16/Products-Challenge-Zeb/master/assets/Ingresar-token.png)
![Aquí la descripción de la imagen por si no carga](https://raw.githubusercontent.com/ManuelOg16/Products-Challenge-Zeb/master/assets/token.png)

\_Restricciones:
Primero se deben crear los catálogos y luego los productos para cada catálogo, si se intenta crear un producto sin un catalogo id valido la API REST expondrá un mensaje de error personalizado.

Segundo no se pueden crear catálogos, usuarios y productos ya existentes, de lo contrario la API REST expondrá un mensaje de error personalizado\_.

## Opción 1 Instalación en tu máquina local 🔧

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos
de desarrollo y pruebas._

### Ambiente Virtual

Desde la raiz del proyecto se crea el ambiente virtual de la siguiente manera:

```
---cd folder del proyecto

---Configurar un ambiente virtual con el comando:

  ##Windows c/s path:
      python -m venv venv
  ##Linux:
      virtualenv -p /usr/bin/python3.8 venv
```

### Activar el Ambiente Virtual

```
---comandos:

  ##Windows c/s path:
      venv\Scripts\Activate
  ##Linux:
      source venv/bin/activate
```

### Instalar las Librerias

```
---comandos:

    pip install -r requirements.txt

```

### Base de Datos

Se crea la base de datos en PostgreSQL con el siguiente nombre:

```
products

```

### Variables de Entorno

#Crear el archivo .env en la raiz del proyecto

#Para este proyecto se cuenta con las siguientes variables de entorno:

```
# CONFIG PROJECT

JWT_SECRET=somethingsecret152654235
MAIL_USERNAME=USUARIO DE CORREO
MAIL_PASSWORD=PASSWORD DE 16 DIGITOS
MAIL_FROM=CORREO ELECTRONICO
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
MAIN_FROM_NAME =Update fields Products

# CONFIG BASE DE DATOS

DATABASE_URL='postgresql://user:password@localhost:5432/products'

```

NOTA: El password de 16 digitos se habilita en la cuenta del correo electronico con la autenticación de dos pasos,
y luego se genera el password de 16 digitos para permitir que la API pueda enviar correos electrónicos.

### Run del proyecto

```
##Con el ambiente virtual activo ejecutar el siguiente comando:

    uvicorn app.main:app --reload

```

### Ingresar a la Web:

Consumir la API REST desde la web por ejemplo:

```
    http://127.0.0.1:8000/docs#/

```

### Crear el SUPER ADMINISTRADOR

```
---crear el super administrador por primera vez por linea de comandos desde la raiz del proyecto:

    ## Windows
      set  PYTHONPATH=./
      python app/commands/create_super_user.py -f Primer_Nombre -l Segundo_nombre -e correo@gmail.com -p numero_celular -pa password

    ## Linux
      export PYTHONPATH=./
      python app/commands/create_super_user.py -f Primer_Nombre -l Segundo_nombre -e correo@gmail.com -p numero_celular -pa password

```

## Opción 2 Ejecución del DOCKER 🔧

### Variables de Entorno

#Crear el archivo .env en la raiz del proyecto

#Para este proyecto se cuenta con las siguientes variables de entorno:

```
# CONFIG PROJECT

JWT_SECRET=somethingsecret152654235
MAIL_USERNAME=USUARIO DE CORREO
MAIL_PASSWORD=PASSWORD DE 16 DIGITOS
MAIL_FROM=CORREO ELECTRONICO
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
MAIN_FROM_NAME =Update fields Products
DATABASE_URL='postgresql://user:password@localhost:5432/products'

```

NOTA: La base de datos usuario y password se crean de manera automatica cuando se ejecute el docker compose, agregar las variables que considere en
DATABASE_URL para su base de datos.

### Generar las Imagenes y Correr Los Contenedores

Desde la raiz del proyecto ejecutar el siguiente comando:

```
docker-compose up -d --build

```

### Comprobar el Funcionamiento de los Contenedores

comando:

```
docker-compose logs -f

```

Si No hay errores

### Crear el SUPER ADMINISTRADOR desde el bash del contenedor de nuestra API

comando:

```
Docker exec -it products-challenge-zeb-web-1 bash

```

En el bash ejecutar los comando:

```
   export PYTHONPATH=./
   python app/commands/create_super_user.py -f Primer_Nombre -l Segundo_nombre -e correo@gmail.com -p numero_celular -pa password

```

### Ingresar a la Web:

Consumir la API REST desde la web por ejemplo:

```
    http://127.0.0.1:8008/docs#/

```
