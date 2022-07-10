FROM node:17

WORKDIR /usr/src/app

COPY package*.json ./

RUN wget -O /bin/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
RUN chmod +x /bin/wait-for-it.sh

RUN npm install

COPY . .

EXPOSE 9001
CMD [ "npm", "run", "start" ]
