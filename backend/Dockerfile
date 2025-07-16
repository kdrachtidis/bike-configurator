FROM python:latest

ARG WWWGROUP
ARG WWWUSER
ARG NAME

WORKDIR /home/$NAME/bike-configurator

COPY /app /home/$NAME/bike-configurator/app
#COPY /demo /bike-configurator/demo
#COPY /templates /bike-configurator/
#COPY /test /bike-configurator/

#COPY create_content.py /bike-configurator/
#COPY create_user.py /bike-configurator/

COPY requirements.txt /home/$NAME/bike-configurator/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN groupadd -g $WWWGROUP -o $NAME
RUN useradd -m -u $WWWUSER -g $WWWGROUP -o -s /bin/bash $NAME
USER $NAME

CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "80"]