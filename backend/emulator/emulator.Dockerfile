FROM python:3.11

WORKDIR /emulator

COPY data_emulator.py .

RUN pip install requests

CMD ["python", "data_emulator.py"]