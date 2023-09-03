# Usa l'immagine Python ufficiale come base
FROM python:3.10

# Crea una directory per il tuo progetto Django all'interno del container
RUN mkdir /app

COPY . /app/

# Imposta la directory di lavoro come /app
WORKDIR /app

# Installa le dipendenze del progetto
RUN pip install -r requirements.txt

EXPOSE 8000

# Porta su cui il server web di Django sarà in ascolto (modificabile)

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
