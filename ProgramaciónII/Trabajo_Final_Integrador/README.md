# VINOTECA VIRTUAL

## El código ofrecido refiere a un aplicativo que expone servicios web para realizar consultas sobre la base de datos de una vinoteca virtual contenida en un archivo JSON.

## 1. Pasos necesarios para la ejecución del Proyecto 

### 1.1 Ubícate en el Directorio Correcto:

![image](https://github.com/user-attachments/assets/2bef4545-ff2d-4ffb-a13c-d8804a45a280)

### 1.2 Instalaciones necesarias: 

El aplicativo está soportado por el framework Flask, por lo que deberá previamente tenerlo instalado para poder correrlo. Para instalarlo corra el siguiente comando por consola:

   - pip install flask
   - pip install Flask-RESTful

### 1.3 Inicia el Servidor Flask:

![image](https://github.com/user-attachments/assets/8a275eb1-efcd-4ba7-b012-342df2ac52fd)

## 2. Los servicios que este aplicativo ofrece son los siguientes:

### 2.1 Buscar Información de una Bodega por ID

Obtiene la información de una bodega específica, incluyendo los vinos y cepas que esta ofrece.

- Para ello obtén la lista de bodegas (punto 2.2) y coloca el identificador único que quieras visualizar en la url como se muestra a continuación.  

- URL: http://localhost:5000/api/bodegas/a0900e61-0f72-67ae-7e9d-4218da29b7d8

### 2.2 Listar Todas las Bodegas

Consulta el listado completo de bodegas, incluyendo las cepas y la cantidad de vinos que ofrecen.

- URL: http://localhost:5000/api/bodegas

- Parámetros Opcionales:

      orden: Campo por el cual las bodegas deben ser ordenadas.

      reverso: Indica si el orden debe ser regular (no) o inverso (si).

Ejemplo:

      Orden Ascendente por Nombre: /api/bodegas?orden=nombre
  
      Orden Descendente por Nombre: /api/bodegas?orden=nombre&reverso=si

### 2.3 Buscar Información de una Cepa por ID

Obtiene la información de una cepa específica, incluyendo los vinos y bodegas que la ofrecen en sus botellas.

- Obtén la lista de cepas (punto 2.4) y coloca el identificador único que quieras visualizar en la url como se muestra a continuación.

- URL: http://localhost:5000/api/cepas//33ccaa9d-4710-9942-002d-1b5cb9912e5d

### 2.4 Listar Todas las Cepas

Consulta el listado completo de cepas, incluyendo los vinos y bodegas que las ofrecen en sus botellas.

- URL: http://localhost:5000/api/cepas

- Parámetros Opcionales:

      orden: Campo por el cual las cepas deben ser ordenadas.

      reverso: Indica si el orden debe ser regular (no) o inverso (si).

- Ejemplo:

      Orden Ascendente por Nombre: /api/cepas?orden=nombre

      Orden Descendente por Nombre: /api/cepas?orden=nombre&reverso=si

### 2.5 Buscar Información de un Vino por ID

Obtiene la información de un vino específico, incluyendo la bodega que lo produce, las cepas en las que se ofrece y las partidas con las que se cuenta para él.

- Obtén la lista de vinos (punto 2.6) y coloca el identificador único que quieras visualizar en la url como se muestra a continuación.

- URL: http://localhost:5000/api/vinos/54919dcb-7ada-70ee-db7d-605650ee41f7

### 2.6 Listar Todos los Vinos

Consulta el listado completo de vinos, incluyendo las bodegas que los producen, las cepas en las que se ofrecen y las partidas con las que se cuenta para ellos.

- URL: http://localhost:5000/api/vinos

- Parámetros Opcionales:

      orden: Campo por el cual los vinos deben ser ordenados.

      reverso: Indica si el orden debe ser regular (no) o inverso (si).

      anios: Indica los años de las partidas que deben incluir los vinos.

- Ejemplo:

      Filtrar por Año: /api/vinos?anios=2023

      Orden Ascendente por Nombre: /api/vinos?orden=nombre

      Orden Descendente por Nombre y Filtrar por Año: /api/vinos?orden=nombre&reverso=si&anios=2023,2022

## 3. Ejemplos, en general: 

- Buscar Bodega por ID: http://localhost:5000/api/bodegas/a0117be3-2ea6-8db1-8901-1be2adf61c29
- Listar Bodegas en Orden Descendente por Nombre: http://localhost:5000/api/bodegas?orden=nombre&reverso=si
- Buscar Cepa por ID: http://localhost:5000/api/cepas/33ccaa9d-4710-9942-002d-1b5cb9912e5d
- Listar Cepas en Orden Ascendente por Nombre: http://localhost:5000/api/cepas?orden=nombre
- Buscar Vino por ID: http://localhost:5000/api/vinos/54919dcb-7ada-70ee-db7d-605650ee41f7  
- Listar Vinos Filtrados por Año y en Orden Descendente por Nombre: http://localhost:5000/api/vinos?orden=nombre&reverso=si&anios=2023,2022









