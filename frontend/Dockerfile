FROM node

ENV APP_ROOT /src

RUN mkdir /config
WORKDIR ${APP_ROOT}
ADD package.json /
RUN yarn install
RUN mkdir /shop_detection
RUN mkdir /frontend
WORKDIR /frontend
ENV HOST 0.0.0.0
