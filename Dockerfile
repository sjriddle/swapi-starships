FROM python:3.7-alpine
COPY ./requirements.txt /root/home/requirements.txt
WORKDIR /root/home
RUN pip install -r requirements.txt
COPY . /root/home
ENTRYPOINT [ "python", "./swapi_api.py" ]
