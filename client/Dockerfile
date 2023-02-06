FROM alpine:3.16

RUN apk add --no-cache nodejs npm
RUN npm install -g @vue/cli && vue --version

WORKDIR /app/easy-eats-front

COPY . /app

RUN npm install

CMD ["npm", "run", "serve"]