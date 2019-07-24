# base image
FROM node:lts-alpine

# update npm & install vue cli peer dependencies
RUN npm install -g http-server npm 
RUN npm install -g @vue/cli @vue/cli-service @vue/cli-plugin-babel @vue/cli-plugin-eslint

# set working directory
WORKDIR /app

# install and cache app dependencies
COPY client/package*.json ./
RUN npm install

COPY ./client /app

RUN npm run build

EXPOSE 8080
# start app
CMD ["http-server", "dist"]