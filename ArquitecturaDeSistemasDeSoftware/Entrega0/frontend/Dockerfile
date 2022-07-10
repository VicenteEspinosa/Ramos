# Se hace pull de la imagen de node desde dockerhub  / same as image in docker-compose
FROM --platform=linux/x86_64 node:current-alpine   

# Correr comando dentro del container
RUN mkdir /frontend
# ubicarme en el directorio app dentro del container
WORKDIR /frontend

# Copiar los json en el directorio app
COPY package.json package-lock.json ./
RUN npm install -g npm@latest
RUN npm install
RUN mkdir -p node_modules/.cache && chmod -R 777 node_modules/.cache

# Exponer aplicación en el puerto 3001 "de docker"
EXPOSE 3001
