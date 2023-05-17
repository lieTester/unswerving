echo "BUILD START"
python3.9 -m pip install -r requirements.txt 

echo "make migrations"
python3.9 -m manage.py makemigrations --noinput
python3.9 -m manage.py migrate --noinput

echo "collectstatic"
python3.9 -m manage.py collectstatic --noinput --clear
echo "BUILD END"