home_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
if [ ! -d ${home_dir}/.venv ]; then
    echo "setting up virtual env"
    virtualenv .venv
fi
source .venv/bin/activate
cat requirements | awk '{system("pip install " $1);}'
virtualenv --relocatable .venv
