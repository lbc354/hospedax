rm -rf hospedax/__pycache__

for app in usuario destino; do
  rm -rf $app/__pycache__
  rm -rf $app/migrations
  mkdir $app/migrations
  touch $app/migrations/__init__.py
done

rm -rf db.sqlite3