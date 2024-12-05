FROM python:3.12
COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["/bin/bash"]