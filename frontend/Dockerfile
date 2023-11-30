FROM node:lts-alpine
WORKDIR /app

COPY ./app .

# RUN npm install

# RUN npm run build

RUN chmod +x entrypoint.sh

EXPOSE 8080
# CMD [ "http-server", "dist" ]
#CMD [ "npm", "run", "preview", "--", "--host"]
# ENTRYPOINT [ "/app/entrypoint.sh" ] 
CMD ["sh", "/app/entrypoint.sh"]