FROM ubuntu:20.04
LABEL name: Komala Nand Pandey
LABEL email: komal.pnd@gmail.com
WORKDIR /test-project/
RUN apt-get update && apt install python3-pip && apt install default-jre
CMD [ pwd ]


