cd easy-eats-app
npm install
npm run serve

cd ..

docker build -t easyeatsfrontapp .

docker run -it -p 5000:8080 easyeatsfrontapp