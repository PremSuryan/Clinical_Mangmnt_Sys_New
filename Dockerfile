FROM python:3.10
# RUN apt-get update && apt-get install -y wget gtk3.0
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONWRITTENBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /clinical-prod
WORKDIR /clinical-prod
COPY requirements.txt .
# RUN python -m venv .venv
# RUN .venv/Scripts/Activate.ps1
RUN pip install -r requirements.txt
COPY . .
RUN playwright install-deps
RUN apt-get update && apt-get install -y xvfb xauth
# COPY NandhaKumaranDentalClinic/NandhaKumaranDental/manage.py .
EXPOSE 8100
# CMD ["python", "/NandhaKumaranDentalClinic/NandhaKumaranDental/manage.py", "runserver", "0.0.0.0:8100"]
# CMD ["gunicorn", "NandhaKumaranDentalClinic.NandhaKumaranDental.DentalCare.wsgi:application", "--bind", "0.0.0.0:8100"]
# ENTRYPOINT ["gunicorn", "DentalCare.wsgi:application"]
ENTRYPOINT ["/bin/sh", "-c", "xvfb-run --auto-servernum gunicorn DentalCare.wsgi:application"]
# CMD ["bash", "-c", "cd NandhaKumaranDentalClinic\NandhaKumaranDental\manage.py && python manage.py runserver 0.0.0.0:8100"]
# CMD python NandhaKumaranDentalClinic/NandhaKumaranDental/manage.py runserver
# CMD gunicorn DentalCare.wsgi:application --bind 0.0.0.0:8100
# NandhaKumaranDentalClinic.NandhaKumaranDental.