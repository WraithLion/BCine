Para poder hacer uso del proyecto es importante, tener a disposición las siguientes dependencias instaladas para el dispositivo a usar

Django

Python

Java

Una vez adquiridas, para hacer utilizar el sitio, dispone de dos opciones.

Descargar el repositorio en formato ZIP y descomprimir

o bien

Clonar el repositorio al espacio de trabajo usando el siguiente enlace:

https://github.com/WraithLion/BCine.git

A continuación, se procede a la navegación de la carpeta del sitio llamada "BCine". En ella encontrará una carpeta y dos archivos, deberá abrir una terminal e ingresar el siguiente comando:

```bash
    conda env create -f environment.yml
```

Esto creara el entrono virtual e instalará sus respectivas dependencias sin comprometer la integridad de los archivos y medios fisicos.

Humanosoft es el nombre del entorno asignado alucivo a la empresa autora de su implementación

Finalizado el proceso, ahora se activa el entorno con el siguiente comando:

```bash
    conda activate Humanosoft
```

En su terminal se mostrará que el ambiente esta activado de la siguiente manera

```bash
    (Humanosoft) (Usuario_su_ruta_de_trabajo)
```

Ahora en la terminal se navega al interior de la carpeta Humanosoft, en ella encontrará un archivo con formato .py.

Deberá ejecutar el siguiente comando para montar el servidor:

```bash
    python manage.py runserver
```
Si el servidor se montó con éxito debería ver en su terminal lo siguiente:

![Muestra de servidor activado](/apoyo/Servidor_Montado.png)

Verá una dirección http puede copiarla o bien presionar Ctrl+clic para abrir el enlace en su navegador de preferencia.

Listo podrá navegar en el sitio BCine.

<a href="https://github.com/WraithLion/BCine.git">BCine</a> © 2025 by <a href="https://sites.google.com/ciencias.unam.mx/humanosoft/inicio">Humanosoft</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International</a><br><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nd.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">
