# Usa l'immagine Python ufficiale come base
FROM python:3.10

# Imposta l'ambiente in modalità non interattiva
ENV PYTHONUNBUFFERED 1

# Crea una directory per il tuo progetto Django all'interno del container
RUN mkdir /app

# Imposta la directory di lavoro come /app
WORKDIR /app

# Copia il file requirements.txt nella directory /app del container
COPY requirements.txt /app/

# Installa le dipendenze del progetto
RUN pip install -r requirements.txt

# Copia il contenuto del progetto Django nella directory /app del container
COPY . /app/

COPY build.sh /app/

RUN chmod +x app/build.sh
EXPOSE 8000

CMD ["/app/build.sh"]

# Porta su cui il server web di Django sarà in ascolto (modificabile)
#EXPOSE 8000

# Comando per avviare il server web di Django
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
