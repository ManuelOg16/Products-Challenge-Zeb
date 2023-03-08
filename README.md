# Welcome to the Product Administration Backend

_This project aims to create, update, delete and query catalogs which have associated products_.

_The business logic is as follows: First, a SUPER ADMINISTRATOR must be created, who has all privileges in the API REST using the CRUD, and can also change the Role of ANONYMOUS USERS, after they are registered, which by default are ANONYMOUS USERS, the SUPER ADMINISTRATOR can change the role of these to an ADMINISTRATOR profile and can also delete the registered ANONYMOUS USERS and ADMINISTRATORS, on the other hand, the ADMINISTRATORS have all the privileges of the CRUD except they cannot delete the SUPER ADMINISTRATOR, query all users, or delete users, if the ADMINISTRATORS or the SUPER ADMINISTRATOR update any product, an email will be sent to each of them with which they registered and the change registered will be notified.
Registered ANONYMOUS USERS can query all catalogs, products and each of the products, when a specific product is consulted, the information of the number of times that the product was consulted with the name of the product and the name of the user who made the action will be saved, ANONYMOUS USERS cannot update,Anonymous users can not update, delete and create catalogs, products and users.
Finally, the general public who does not register in the REST API can only consult all catalogs and all products_.

_Note: For all registered users including the SUPER ADMINISTRATOR, they must log in and the generated token must be entered in the authorization lock, in this way they will have all the functionalities of the REST API according to the profile_.

![Aquí la descripción de la imagen por si no carga](https://raw.githubusercontent.com/ManuelOg16/Products-Challenge-Zeb/master/assets/Ingresar-token.png)
![Aquí la descripción de la imagen por si no carga](https://raw.githubusercontent.com/ManuelOg16/Products-Challenge-Zeb/master/assets/token.png)

_Restrictions:
First the catalogs must be created and then the products for each catalog, if an attempt is made to create a product without a valid catalog ID the REST API will expose a personalized error message_.

Second, you cannot create catalogs, users and products that already exist, otherwise the REST API will expose a custom error message\_.

## Option 1 Installation on your local machine 🔧

_These instructions will get you a copy of the project up and running on your local machine for development and testing purposes_.

### Virtual Environment

From the root of the project, the virtual environment is created as follows:

```
---cd project folder

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

## Propuesta de diseño de arquitectura

\_El diseño de arquitectura que se propone es el siguiente:

1. Como se puede llegar a tener demasiada volumetría de productos y catálogos, esto puede afectar el performance de los componentes en donde este alojado el Back end suponiendo que este en una Cloud Run de Google Cloud Platform , lo cual podría causar time out demasiado largos e interrumpir el proceso masivo de creación de catálogos y productos.
2. Lo anterior se podría solucionar de varias maneras, pero propongo lo siguiente: la arquitectura que implementaría seria la siguiente, seguimos teniendo la Cloud Run en el cual estará alojado el Back end , debido a que el Cloud Run puede auto escalar de manera automática si el proceso lo demanda y de esta manera tener flexibilidad, pero para la creación masiva de catálogos y productos se implementaría un Dataflow el cual se podría alimentar de la información de manera estática a través de archivos planos o tipo Batch en línea , de esta manera todo el procesamiento de la data se realizaría a través de Dataflow el cual es un componente especializado para transformación de datos a grandes volúmenes y no se afectaría el rendimiento de performance de la Cloud Run.\_

![Aquí la descripción de la imagen por si no carga](https://raw.githubusercontent.com/ManuelOg16/Products-Challenge-Zeb/master/assets/Diseño-Arquitectura.jpg)
