FROM tensorflow/tensorflow:2.16.1-gpu
# (Optional) Install any additional Python packages you need
RUN pip install matplotlib tensorflow-hub

# (Optional) Set working directory
WORKDIR /app