# Chat-IO
An efficient multi-user Chat WebApp built with Django, Web Sockets, and Channels 2.

#### Basic System Prerequisites:
```
Python == 3.6
pip >= 18.1
virtualenv >= 16.0.0
```
#### Redis Server Setup:
* For **Ubuntu** follow this [link](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04).
* For **Mac OS** follow this [link](https://medium.com/@petehouston/install-and-config-redis-on-mac-os-x-via-homebrew-eb8df9a4f298).
* **Redis** does not support Windows officially.

#### Fork this repo and run these commands after cloning the project and go inside the directory:
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```
#### TODOs:
- [ ] **Group Chat**
- [ ] Finding which user is currently **typing**
- [ ] User **Online / Offline**
- [ ] Finding out count of **messages unread** in a chat
