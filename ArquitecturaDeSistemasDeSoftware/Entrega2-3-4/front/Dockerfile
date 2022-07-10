FROM node:17
WORKDIR /usr/src/app
COPY ./package.json ./
COPY ./ ./
RUN npm i --force
CMD ["npm", "run", "start"]