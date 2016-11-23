# Sistemas de operación

## En desarrollo: tarea 2

### Problemas 
* Problemas con el uso de varios hilos y sqlite. Se necesita un algoritmo más elaborado que permita realizar correctamente esta prueba.
* [**SOLUCIONADO**] Faltan las pruebas de MySQL.
* La distribución de procesos es incorrecta (0 asignados) al usar 10 queries con 50 procesos.

### Requisitos
#### Actividad 1
* Elaborar un programa o script que llene una base de datos con 1.000.000 de entradas
* Llenarla la tabla con los datos especificados

#### Actividad 2
##### Constantes definidas para las tablas
* **Columnas**: 1, 10 o 50 concurrencias
* **Filas**: 10, 100, 100.000 o 300.00 queries

##### Escenarios a cumplir
1. insert + multi-proceso
2. insert + multi-hilo
3. select + multi-proceso + index
4. select + multi-hilo + index
5. select + multi-proceso
6. select + multi-hulo

#### Actividad 3
* Analizar los resultados, ¿qué sucede a nivel de
  * SO?
  * BD?

* Proponga extensiones del estudio para averiguar otros aspectos de rendimiento