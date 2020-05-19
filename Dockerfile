FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /personal_blog
WORKDIR /personal_blog
ADD . /personal_blog/
RUN pip install -r requirements.txt