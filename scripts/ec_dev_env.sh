#!/bin/bash

# NOTE: Execute as $ source ec_dev_env.sh
# ./ec_dev_env will not work for the virtual environment
# place this in home directory for quick execution

# to change "user" to your username, there are two options
# $ sed -i "s/user/your_username/g" ~/ec_dev_env.sh
# open in vi/m and execute :%s/user/your_username/g and :wq


# for backend development
set -e
source /home/user/elcaudillo/venv/bin/activate
cd /home/user/elcaudillo/backend

# for frontend development
gnome-terminal --tab -- bash -c "cd /home/user/elcaudillo/frontend; exec bash"

# for git management
gnome-terminal --tab -- bash -c "cd /home/user/elcaudillo; exec bash"

# for docker-compose build/up/down
gnome-terminal --tab -- su -c "cd /home/user/elcaudillo; exec bash"
gnome-terminal --tab -- su -c "cd /home/user/elcaudillo; exec bash"

# for testing in the browser
gnome-terminal --tab -- bash -c \
  "google-chrome http://localhost:3000 & \
  google-chrome http://localhost:8000; exec bash"
