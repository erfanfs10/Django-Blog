FROM nginx:1.25-bookworm

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
WORKDIR /app
EXPOSE 80
