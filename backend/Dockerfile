FROM python:3.13.7

# declare build-time arguments (with defaults)
ARG USERNAME=appuser
ARG UID=1000
ARG GID=1000

# make sure ARG is visible in this layer
ENV USERNAME=${USERNAME} UID=${UID} GID=${GID}

# create group and user
RUN groupadd --gid $GID $USERNAME \
    && useradd --uid $UID --gid $GID -m $USERNAME

# set working dir inside user's home
WORKDIR /home/$USERNAME/app

# install dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project files
COPY . .

# set ownership
RUN chown -R $USERNAME:$USERNAME /home/$USERNAME

# switch to non-root user
USER $USERNAME

# RUN python demo/create_content.py
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]