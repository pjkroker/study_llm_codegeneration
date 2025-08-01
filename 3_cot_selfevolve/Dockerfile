# Use Python 3.8 as base
FROM python:3.8.18

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install poetry==1.3.2

#RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/tqtensor/cot-selfevolve.git .

# Download and install AWS CLI v2
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf awscliv2.zip aws


# Install build tools and curl
RUN apt-get update && \
    apt-get install -y build-essential clang && \
    apt-get clean

RUN poetry install
