# Establecer la imagen base
FROM node:16-alpine

# Instalar Vue CLI globalmente
RUN npm install -g @vue/cli && vue --version

# Crear un directorio de trabajo
WORKDIR /app

# Copiar el package.json y package-lock.json en el directorio de trabajo
COPY easy-eats/package*.json ./

# Instalar las dependencias
RUN npm ci

# Copiar el resto de los archivos del proyecto en el directorio de trabajo
COPY easy-eats ./

# Ejecutar la aplicación
CMD ["npm", "run", "serve"]
