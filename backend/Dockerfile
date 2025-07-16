FROM python:latest

WORKDIR /bike-configurator

ARG WWWGROUP
ARG WWWUSER
ARG USERNAME

RUN mkdir bike-configurator

COPY /app /bike-configurator/app
#COPY /demo /bike-configurator/demo
#COPY /templates /bike-configurator/
#COPY /test /bike-configurator/

#COPY create_content.py /bike-configurator/
#COPY create_user.py /bike-configurator/

COPY requirements.txt /bike-configurator/requirements.txt

#RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN groupadd -g $WWWGROUP -o $USERNAME
RUN useradd -m -u $WWWUSER -g $WWWGROUP -o -s /bin/bash $USERNAME
USER $USERNAME

#CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "80"]