FROM fusuf/asenauserbot:latest
RUN git clone https://github.com/fastuserbot/fastuserbot /root/fastuserbot
WORKDIR /root/fastuserbot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
