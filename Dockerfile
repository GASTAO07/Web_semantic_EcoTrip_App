# Utilisez l'image de base Python 3.9
FROM python:3.9

# UPDATE
RUN pip install --upgrade pip
RUN apt-get update -y && apt-get upgrade -y

# Définition du répertoire de travail dans le conteneur
WORKDIR /

# Copie des fichiers du projet dans le conteneur
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Installation des dépendances du projet
RUN pip install --no-cache-dir -r requirements.txt

# Commande à exécuter lorsque le conteneur démarre
COPY src /app
EXPOSE 8501
CMD [ "python", "/main.py" ]
