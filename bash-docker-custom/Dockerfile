FROM python:3.11.5-alpine3.18
WORKDIR /app

ARG nom
ENV nom=${nom} 
ARG prenom
ENV prenom=${prenom} 
# Copie le script dans le conteneur, dans le répertoire /app
COPY scripte.py script-hello-world.py

# Exécute le script
CMD ["python", "/app/script-hello-world.py"]