FROM --platform=linux/x86_64 ruby:2.7.2-alpine

RUN apk add --update --virtual \
    runtime/deps \
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

WORKDIR /app

COPY . /app/

RUN bundle install

ENTRYPOINT ["sh", "entrypoint_rails.sh"]

CMD [ "bin/rails"]

EXPOSE 3000
