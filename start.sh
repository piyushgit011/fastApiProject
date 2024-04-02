apt-get update 
apt-get install python
apt-get install tmux 
pip install -r requirements.txt
tmux new
python3 -m venv env
source env/bin/activate
python main.py
