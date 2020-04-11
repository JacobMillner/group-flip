FROM node:13.12

RUN apt-get update

WORKDIR /var/www/client

COPY . .

RUN npm install

CMD ["npm", "start"]