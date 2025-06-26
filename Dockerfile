FROM selenium/standalone-chrome:latest

USER root
WORKDIR /app

COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["pytest", "tests/"]
