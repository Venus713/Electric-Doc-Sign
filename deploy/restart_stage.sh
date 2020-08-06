export PROJECT_HOME=/var/sites/docsign
export ENV_HOME=/var/venvs/docsign/bin
cd "$PROJECT_HOME"
source "$ENV_HOME/activate"
git pull origin dev
pip install -r requirements.txt
python manage.py migrate --settings=config.settings.stage
python manage.py collectstatic --settings=config.settings.stage --noinput
sudo systemctl restart uwsgi
sudo systemctl restart nginx

