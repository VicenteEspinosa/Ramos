FROM --platform=linux/x86_64 ruby:3.1.2-alpine

RUN apk update && apk add --virtual build-dependencies build-base

RUN apk add --update --virtual \
    postgresql-client \
    build-base \
    libxml2-dev \
    libxslt-dev \
    nodejs \
    yarn \
    libffi-dev \
    readline \
    postgresql-dev \
    libc-dev \
    linux-headers \
    readline-dev \
    file \
    imagemagick \
    git \
    tzdata \
    wget \
    curl \
    && rm -rf /var/cache/apk/*

RUN gem update --system && gem install bundler

COPY Gemfile* /tmp/

WORKDIR /tmp

RUN bundle install

WORKDIR /app

COPY . /app/

ENTRYPOINT ["sh", "entrypoint_rails.sh"]

CMD [ "bin/rails"]

EXPOSE 3000
