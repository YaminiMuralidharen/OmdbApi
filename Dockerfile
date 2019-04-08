FROM python:3.7
COPY . /src
ENTRYPOINT [ "python", "/src/omdbApiQuery.py"]
