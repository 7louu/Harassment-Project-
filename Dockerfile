FROM python:3.9

WORKDIR /usr/local/app

RUN python -m venv .venv

RUN pip install --upgrade pip \
    && pip install .

COPY src ./src

RUN useradd app

USER app

EXPOSE 8000


CMD ["fastapi","src.routes.main.app","--host","0.0.0.0","--port","8000"]
