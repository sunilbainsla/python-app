FROM python:3.6.6
COPY server.py /
COPY requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python", "-u", "server.py" ]
RUN /bin/bash -c 'echo this is generally a configuration'
ENV myCustomEnvVar="This is a sample. "\
    otherEnvVar="this is also a sample."