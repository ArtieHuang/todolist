# Dockerfile

FROM centos:7.9.2009
RUN yum makecache fast;
RUN yum install python3-devel python3-pip -y
RUN pip3 install requirements.txt
COPY todolist.py /opt
WORKDIR /opt
EXPOSE 5000
CMD ["python3","todolist.py"]
