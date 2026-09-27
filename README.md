# Sistema Inteligente de Rutas

## Descripción

Este proyecto consiste en el desarrollo de un sistema inteligente de rutas utilizando Python.

El sistema permite seleccionar una estación de origen y una estación de destino. A partir de una base de conocimiento que contiene las estaciones y sus conexiones, el programa busca una ruta disponible entre los dos puntos.

Para facilitar la interacción con el usuario, cada estación tiene asignada una letra. El usuario solamente debe ingresar la letra correspondiente a la estación de origen y a la estación de destino.

## Objetivo

Desarrollar un sistema básico de Inteligencia Artificial capaz de utilizar una base de conocimiento y un mecanismo de búsqueda para encontrar rutas entre diferentes estaciones.

## Tecnologías utilizadas

* Python
* Estructuras de datos
* Diccionarios
* Funciones recursivas
* Base de conocimiento
* Algoritmo de búsqueda

## Funcionamiento

El sistema contiene una base de conocimiento donde se encuentran registradas las estaciones y sus conexiones.

Cada estación tiene asignada una letra:

* A. Portal Norte
* B. Calle 100
* C. Héroes
* D. Calle 72
* E. Calle 63
* F. Calle 57
* G. Calle 45
* H. Marly
* I. Museo Nacional
* J. Centro
* K. Avenida El Dorado

El usuario selecciona una estación de origen y una estación de destino mediante las letras.

Por ejemplo:

```text
Ingrese la letra de la estación de origen: A
Ingrese la letra de la estación de destino: J
```

El sistema identifica las estaciones seleccionadas y realiza la búsqueda de una ruta.

## Ejemplo de resultado

```text
MEJOR RUTA ENCONTRADA

Portal Norte -> Calle 100 -> Héroes -> Calle 72 -> Calle 63 -> Centro

Número de estaciones: 6
```

## Estructura del proyecto

```text
sistema-inteligente-rutas/
│
├── sistema_rutas.py
│
└── README.md
```

## Características

* Permite seleccionar estaciones mediante letras.
* Valida que las estaciones ingresadas existan.
* Evita ciclos durante la búsqueda.
* Encuentra una ruta entre el origen y el destino.
* Muestra el recorrido encontrado.
* Indica el número de estaciones de la ruta.

## Autor

Adrian Garrido

## Contexto académico

Proyecto desarrollado como actividad académica para la asignatura de Inteligencia Artificial.
