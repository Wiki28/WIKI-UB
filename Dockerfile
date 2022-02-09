# We're using Ubuntu 20.10
FROM mrismanaziz/man-userbot:buster

RUN git clone -b WIKI-UBOT https://github.com/Wiki38/WIKI-UBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/mrismanaziz/Man-Userbot/Man-Userbot/requirements.txt

CMD [ "bash", "start" ]
