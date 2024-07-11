FROM python:3.10.0-slim-buster

# Install Flask, specifying a version compatible with rq-dashboard
RUN pip install Flask==2.0.3 Werkzeug==2.0.3

# Uninstall click if it's already installed
RUN pip uninstall -y click

# Install rq-dashboard and a compatible version of click
# click breaks workers: https://github.com/rq/rq/issues/1469; pin click version
RUN pip install rq-dashboard==0.5.1 click==7.1.2

EXPOSE 9181

CMD ["rq-dashboard"]
