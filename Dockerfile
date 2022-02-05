FROM mrismanaziz/man-userbot:buster

RUN git clone -b Wiki-Userbot https://github.com/wiki28/wiki-userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Wiki28/Wiki-Userbot/Wiki-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
