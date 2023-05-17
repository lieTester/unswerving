echo "BUILD START"
python3.9 -m pip install -r requirements.txt 

echo "make migrations"
python3.9 -m python manage.py makemigrations --noinput
python3.9 -m python manage.py migrate --noinput

echo "collectstatic"
python3.9 -m python manage.py collectstatic --noinput --clear
echo "BUILD END"