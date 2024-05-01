# Use a imagem base do PostgreSQL
FROM postgres:latest

# Informações sobre o mantenedor
LABEL maintainer="Willamy <willamy.wlp@gmail.com>"

# Definir variáveis de ambiente
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD admin@123
ENV POSTGRES_DB fichamed

# Expor a porta padrão do PostgreSQL
EXPOSE 5433

# Comandos para executar ao iniciar o container
# docker build -t db_ps_fichamed .
# docker run --name container_db_ps_fichamed -d -p 5433:5432 db_ps_fichamed