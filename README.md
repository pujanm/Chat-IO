# Chat-IO
An efficient multi-user Chat WebApp built with Django, Web Sockets, and Channels 2.

### Normal Setup
  #### - Basic System Prerequisites:
  ```
  Python >= 3.6
  virtualenv >= 16.0.0
  ```
  #### - Redis Server Setup:
  * For **Ubuntu** follow this [link](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04).
  * For **Mac OS** follow this [link](https://medium.com/@petehouston/install-and-config-redis-on-mac-os-x-via-homebrew-eb8df9a4f298).
  * **Redis** does not support Windows officially.

  #### - Fork this repo and run these commands after cloning the project and go inside the directory:
  ```
  virtualenv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
  python3 manage.py migrate
  python3 manage.py runserver
  ```

### Optional Docker Setup 
    ```
    # This builds the Docker image.
    docker build -t "pujanm/chat_app" .

    # This will start the container.
    docker run -itd --name chat_app_cont -p 8000:8000  pujanm/chat_app

    # To stop and remove the container
    docker stop chat_app_cont && docker rm chat_app_cont
    ```

You can access the WebApp at [http://localhost:8000](http://localhost:8000)



#### TODOs:
- [ ] **Group Chat**
- [ ] Finding which user is currently **typing**
- [ ] User **Online / Offline**
- [ ] Finding out count of **messages unread** in a chat
