FROM node:boron
WORKDIR /usr/src/app
COPY package.json
RUN npm install
COPY . .
EXPOSE 20000
CMD ["npm","start"]