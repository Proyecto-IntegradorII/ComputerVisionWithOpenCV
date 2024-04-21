FROM python:3.8-slim
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN apt-get update && apt-get install -y libgl1-mesa-glx 
RUN pip install --upgrade pip setuptools
RUN pip install numpy pytesseract opencv-contrib-python-headless Flask waitress
RUN pip install flask-cors
RUN apt-get update && apt-get install -y tesseract-ocr
COPY ./ /code/
EXPOSE 5000
# Start the FastAPI application
CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "5000", "--reload"]