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

### Activate Virtual Environment

```
---commands:

  ##Windows c/s path:
      venv\Scripts\Activate
  ##Linux:
      source venv/bin/activate
```

### Install Libraries

```
---commands:

    pip install -r requirements.txt

```

### Database

The database is created in PostgreSQL with the following name:

```
products

```

### Environment Variables

#Create the .env file in the root of the project

#For this project we have the following environment variables:

```
# CONFIG PROJECT

JWT_SECRET=somethingsecret152654235
MAIL_USERNAME=USUARIO DE CORREO
MAIL_PASSWORD=PASSWORD DE 16 DIGITOS
MAIL_FROM=CORREO ELECTRONICO
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
MAIN_FROM_NAME =Update fields Products

# CONFIG DATABASE

DATABASE_URL='postgresql://user:password@localhost:5432/products'

```

NOTE: The 16-digit password is enabled on the email account with two-step authentication, and then the 16-digit password is generated to allow the API to send emails..

### Run project

```
##With the virtual environment active, execute the following command:

    uvicorn app.main:app --reload

```

### Enter the website:

Consume the REST API from the web for example:

```
    http://127.0.0.1:8000/docs#/

```

### Create the SUPER ADMINISTRATOR

```
---create the super administrator for the first time by command line from the root of the project:

    ## Windows
      set  PYTHONPATH=./
      python app/commands/create_super_user.py -f Primer_Nombre -l Segundo_nombre -e correo@gmail.com -p numero_celular -pa password

    ## Linux
      export PYTHONPATH=./
      python app/commands/create_super_user.py -f Primer_Nombre -l Segundo_nombre -e correo@gmail.com -p numero_celular -pa password

```

## Option 2 Running the DOCKER 🔧

### Environment Variables

#Create the .env file in the root of the project

#For this project we have the following environment variables:

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

NOTE: The user and password database are automatically created when the docker compose is executed, add the variables you consider in DATABASE_URL for your database.

### Generate the Images and Run the Containers

From the root of the project run the following command:

```
docker-compose up -d --build

```

### Check the Operation of the Containers

command:

```
docker-compose logs -f

```

If there are no errors

### Create the SUPER ADMINISTRATOR from the bash of our API container

command:

```
Docker exec -it products-challenge-zeb-web-1 bash

```

In bash execute the command:

```
   export PYTHONPATH=./
   python app/commands/create_super_user.py -f Primer_Nombre -l Segundo_nombre -e correo@gmail.com -p numero_celular -pa password

```

### Enter the website:

Consume the REST API from the web for example:

```
    http://127.0.0.1:8008/docs#/

```

## Proposed Architecture Design

\_The architecture design proposed is as follows:

1. As there could be too much product and catalogue volume, this could affect the performance of the components where the Back end is hosted assuming it is on a Google Cloud Platform Cloud Run, which could cause too long time outs and interrupt the massive catalogue and product creation process.
2. The above could be solved in various ways, but I propose the following: the architecture to be implemented would be the following, we still have the Cloud Run in which the Back end will be hosted, due to the fact that the Cloud Run can auto-scale automatically if the process demands it and thus have flexibility, but for the massive creation of catalogues and products a Dataflow would be implemented which could be fed with the information in a static way through flat files or Batch type online, thus all the data processing would be carried out through Dataflow which is a component specialized in data transformation to large volumes and the performance performance of the Cloud Run would not be affected.\_

![Aquí la descripción de la imagen por si no carga](https://raw.githubusercontent.com/ManuelOg16/Products-Challenge-Zeb/master/assets/Diseño-Arquitectura.jpg)
