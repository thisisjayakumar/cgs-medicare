FROM public.ecr.aws/lambda/python:3.9

RUN yum install -y google-chrome-stable
RUN yum install -y chromedriver

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["app.handler"]