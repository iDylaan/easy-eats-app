# easy-eats-front

## Project setup
```
npm install
```
## CLI Vue
npm install -g @vue/cli

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


### DOCKER ###
cd /client/

docker build -t easyeatsfrontapp .

docker run -it -p 5000:8080 easyeatsfrontapp