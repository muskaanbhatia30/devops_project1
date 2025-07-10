from redhat/ubi8

RUN yum install python3 -y
RUN pip3 install flask

copy app.py /app.py

CMD ["python3", "/.app.py"]