FROM python:3.9

WORKDIR /app

RUN python -m venv .venv

COPY src ./src

COPY pyproject.toml .

RUN pip install --upgrade pip \
    && pip install .


RUN useradd app

USER app

EXPOSE 8000


CMD ["fastapi","src.routes.main.app","--host","0.0.0.0","--port","8000"]
