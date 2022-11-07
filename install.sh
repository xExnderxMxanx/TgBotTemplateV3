echo "create virtual python env..."
python3 -m venv env
source ./env/bin/activate

echo "install requirements..."
python -m pip install pip -U
pip install -r requirements.txt

echo "create config file..."
cp -v ./utils/conf/config.ini.example ./utils/conf/config.ini