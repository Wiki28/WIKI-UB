FROM mrismanaziz/man-userbot:buster

RUN git clone -b WIKI-UBOT https://github.com/Wiki28/WIKI-UBOT /home/wikiubot/ \
    && chmod 777 /home/wikiubot \
    && mkdir /home/wikiubot/bin/

WORKDIR /home/wikiubot/

CMD [ "bash", "start" ]
