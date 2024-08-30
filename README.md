# Game Project 

Para correr el juego debes seguir las siguientes instrucciones en la terminal:

```sh
cd game 
python3 main.py

```

# ver los modulos instalados
pip3 freeze 

# si es que necesitamos otra version de una libreria 
pip3 install matploplib==3.7.5

# Verificar donde se esta ejecutando python y pip

which python3

which pip3

### ENTORNOS VIRTUALES

# para activar el uso de entornos virtuales
# debemos instalar el siguiente paquete

apt install -y python3-venv

# dentro de la carpeta del proyecto

python3 -m venv env-app 

# activamos el entorno 

source env-app/bin/activate  

# ejecutando el comando "pip3 freeze"
# no encontramos ninguna libreria

# podemos instalar una libreria de una version especifica
# en el entorno virtual
pip3 install matploplib==3.6.0

# desactivamos el entorno 

deactivate 

### DEPENDENCIAS 

pip3 freeze > requirements.txt 

# instala las dependencias y modulos 
# necesarias para este proyectos 

pip3 install -r requirements.txt

# para que alguien pueda ejecutar nuestro 
# programa debe seguir las siguientes instrucciones

``` sh 
git clone 
cd app
source env/bin/activate 
pip3 install -r requirements.txt
python3 main.py 


```




