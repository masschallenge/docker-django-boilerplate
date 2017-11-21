FROM python:3.6

WORKDIR /wwwroot

COPY directory /wwwroot

COPY scripts/start.sh /usr/bin

COPY scripts/start-nodaemon.sh /usr/bin

RUN apt-get update -y

# python2.7 is required to run supervisor
RUN apt-get install -y netcat mysql-client python2.7 python-setuptools nginx

COPY nginx/nginx.conf /etc/nginx

RUN pip install --upgrade pip

RUN easy_install-2.7 supervisor

RUN pip3 install -r requirements/dev.txt

RUN useradd -s /bin/bash -u 3000 -M directory_user

RUN chown directory_user /usr/bin/start.sh

RUN chown -R directory_user /wwwroot

RUN apt-get install -y gettext

USER directory_user

ENV PYTHONUNBUFFERED 1

ARG localhost_port

EXPOSE ${localhost_port}

CMD ["/bin/bash" , "/usr/bin/start.sh"]
