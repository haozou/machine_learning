source .venv/bin/activate
cat requirements | awk '{system("pip install " $1);}'
virtualenv --relocatable .venv
