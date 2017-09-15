FROM python:3
COPY . /app
WORKDIR /app
RUN pip install requirements.txt
EXPOSE 5000 15672
ENTRYPOINT ["python"]
CMD ["pyserver.py"]