	○ Guía de Despliegue. (DS_2022_GRXX_Guia de Despliegue.pdf)
		§ Requisitos Técnicos: -- 
		• PC con 8 GB de memoria RAM, procesador de dos núcleos y GPU de 2 GB de RAM
		• Algún editor de texto para escribir código, puede ser Sublime Text, Atom o https://code.visualstudio.com/download” target=”_blank”>Visual Studio Code
		• Sistema operativo: macOS Snow Leopard/superior o Windows 7/superior
		
		§ Instrucciones para Instalación del Proyecto:
		1- Clonar el repositorio https://github.com/arielmagro/proyectofinal_python.git (cambiar por mi url)
		
		2- Ejecutar los comandos:
		python manage.py runserver
		
		3- Redirijirse a http://127.0.0.1:8000/
		
		§ Diagrama de Despliegue de los Artefactos Software.
	○ Código Fuente del Proyecto (DS_2022_GRXX_CodigoFuente.zip)
		§ Deben subir un archivo comprimido con las fuentes. Si tienen el código fuente en algún repositorio, deben descargarlo y subir con la nomenclatura indicada. Ok
	 
	○ Script Base de Datos SQL
		§ Script para Creación del Esquema/ Estructura de la BD.
		python manage.py makemigrations 
		python manage.py migrate 
		python manage.py shell >> seed_data.py (insertar datos de los objetos creados)
	
		§ Script con datos mínimos necesarios para el funcionamiento de la aplicación. 
	○ Video del Trabajo (DS_2022_GRXX_Video.mp4)
		§ Duración Máxima 20 Minutos
		§ En el video deben hacer una transferencia de conocimiento y experiencia sobre el Trabajo de Campo abordado a lo largo del año teniendo en cuenta cada una de las etapas y entregas realizadas (Desde los requerimientos hasta la implementación).
Pueden subir todo en archivos separados mediante la plataforma pero tiene un límite de 200 MB por archivo (Esto se lo comentamos en particular por el video)