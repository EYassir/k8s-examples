FROM ubuntu
WORKDIR /application
COPY ./main /application
EXPOSE 9000
RUN mkdir /var/lib/application
VOLUME [ "/var/lib/application" ]
CMD [ "./main" ]

