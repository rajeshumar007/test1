# Start with a base image
FROM debian:bullseye

# Install Python, Tor, and procps
RUN apt-get update && apt-get install -y \
    tor \
    python3 \
    python3-pip \
    procps \
    && apt-get clean

# Install Python libraries
RUN pip3 install requests[socks]

# Set up Tor configuration
RUN echo "ControlPort 9051" >> /etc/tor/torrc && \
    echo "CookieAuthentication 0" >> /etc/tor/torrc && \
    echo "SocksPort 9050" >> /etc/tor/torrc



# Copy the Python script into the container
COPY script.py /app/script.py

# Set the working directory
WORKDIR /app

# Expose Tor ports
EXPOSE 9050
EXPOSE 9051

# Run a bash shell by default
CMD ["python3", "/app/script.py", "http://lhuxskdh7kutkmmw4bllxvkwphw53qmededwexd5w2grjdnvogljg6ad.onion", "20"]

