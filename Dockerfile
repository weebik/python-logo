# Build the frontend
FROM node:22 AS build

WORKDIR /app/frontend
COPY frontend /app/frontend
RUN npm install
RUN npm run build

# Create Python image
FROM python:3.12-slim

RUN useradd -m user
USER user
WORKDIR /app

ENV PATH=/home/user/.local/bin:$PATH

COPY --chown=user:user . /app
COPY --from=build --chown=user:user /app/dist /app/dist
RUN pip install --no-cache-dir .

EXPOSE 5000
CMD ["gunicorn", "-k", "eventlet", "-b", "0.0.0.0:5000", "-w", "1", "--access-logfile", "-", "--error-logfile", "-", "app:app"]
