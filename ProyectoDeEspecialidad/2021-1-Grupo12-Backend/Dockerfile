FROM python:3.8

RUN pip install --upgrade pip \
    && pip install cryptography==3.4.7 \
    && pip install poetry==1.1.4
# RUN poetry install 

COPY ./osam_backend /app 

WORKDIR /app 

COPY poetry.lock  /app/
COPY pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]