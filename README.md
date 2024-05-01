01) Crear entorno virtual
        python -m venv (nombre sin paréntesis (venv))


02) Activar el entorno
        .\venv\Scripts\activate

    desactiva el entorno
        .\venv\Scripts\deactivate


03) Para instalar las dependencias dentro de requirements.txt
        pip install -r requirements.txt

    03-1) Instalar FASTAPI
            pip install fastapi 

    03-2) Instalar uvicorn para tener funciones acincronas
            pip install "uvicorn[standard]"
    
    03-3) Istalar SQLAlchemy que es un ORM compatible con FastAPI
            pip install sqlalchemy

    03-4) Instalar bcrypt para el sifrado de la contraseña
            pip install bcrypt

    03-5) Crear un archivo requirements.txt
            pip freeze > requirements.txt


04) Crea el archivo principal en este caso es (main.py) y agregas este que es la configuracion minima de para iniciar un servidor 
        from fastapi import FastAPI
        from typing import Union

        # Crea una instancia de la clase FastAPI y la asigna a la variable app. Esta instancia será nuestra aplicación web FastAPI principal donde definiremos nuestras rutas y lógica de
        #   manejo de solicitudes.
        app = FastAPI()


        # Esto es un decorador que especifica que la función siguiente manejará las solicitudes GET en la ruta /
        # Si o si tenes que pasaarle una ruta al decorador
        @app.get("/")
        def read_root():
                return {"Funciono": "Mas bien loquita"}


        @app.get("/items/{item_id}")
        def read_item(item_id: int, q: Union[str, None] = None):
            return {"item_id": item_id, "q": q}

05) Asi ejecutas el servidor en el puerto por defecto que es el (8000) tambien pedes agregar esto al final (--host 0.0.0.0 --port 8000) para elegir el host y el puerto
        uvicorn main:app --reload

    El comando uvicorn main:app se refiere a:
        main: el archivo main.py (el"modulo" de Python).
        app: el objeto creado dentro de main.py con la línea app = FastAPI().
        --reload: hace que el servidor se reinicie después de cambios en el código. Esta opción solo debe ser usada en desarrollo.

06) FastAPI viene con swagger incluido y se accede asi con (/docs) y tambien tiene una documentacion alternativa (/redoc)
        http://127.0.0.1:8000/docs
        http://127.0.0.1:8000/redoc