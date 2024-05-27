# Use an existing image as a base
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the program files into the container
COPY . /app

# Install any necessary dependencies
RUN pip install paho-mqtt

# Set environment variables
ENV MQTT_BROKER_IP 0.0.0.0
ENV MQTT_BROKER_PORT 1883

# Command to run the MQTT logging messages program
CMD ["python", "mqtt_logging_messages.py"]
