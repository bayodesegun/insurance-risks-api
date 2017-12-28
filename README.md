# insurance-risks-api
A serverless Django API project.

[![Build Status](https://travis-ci.org/bayodesegun/insurance-risks-api.svg?branch=master)](https://travis-ci.org/bayodesegun/insurance-risks-api)

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines.
* [DRF](http://www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs.
* [Zappa](https://github.com/Miserlou/Zappa): Serverless Python Web Services.


## Run It Locally
To run your own build, please follow the steps below.

### Prerequisites
* Ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* Confirm that you have installed virtualenv globally as well. If not, run this:
  ```bash
  $ pip install virtualenv
  ```
* Git-clone this repo:
  ```bash
  $ git clone https://github.com/bayodesegun/insurance-risks-api.git
  ```
* Provide your own project settings:
  - Rename ```settings.ini.example``` to ```settings.ini``` and set your variables.
  - Use the settings in ```sample_zappa_settings.json``` as a guide when you optionally configure Zappa (below).

### Install Dependencies
* Cd into the cloned repo:
  ```bash
  $ cd insurance-risks-api
  ```
* Create and fire up a virtual environment:
  ```bash
  $ virtualenv  venv -p python2
  $ source venv/bin/activate
  ```
* Install the dependencies needed to run the app:
  ```bash
  $ pip install -r requirements.txt
  ```
* Run migrations:
  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

### Run or Test
- Run on localhost:
  ```bash
  $ python manage.py runserver
  ```
- Test:
  ```bash
  $ python manage.py test
  ```
- Browsable API endpoints (*test users/passwords*: geek/password, nerd/password):
  - [http://127.0.0.1:8000/risks/](http://127.0.0.1:8000/risks/)  - list all risks for a given user
  - [http://127.0.0.1:8000/risks/{riskId}](http://127.0.0.1:8000/risks/1) - display details for a given risk

- Fire GET requests the API endpoints (*test users/passwords*: geek/password, nerd/password):
  - Make a POST call to endpoint ```http://127.0.0.1:8000/obtain_token/``` to obtain a token. Example using shell cURL:
    ```bash
    curl --request POST \
    --url http://127.0.0.1:8000/obtain-token/ \
    --header 'cache-control: no-cache' \
    --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
    --form username=geek \
    --form password=password
    ```
  - Make the respective GET calls using obtained token: 
     - /risks/ endpoint
     ```bash
     curl --request GET \
      --url http://127.0.0.1:8000/risks/ \
      --header 'authorization: Token 08ec57851cc4dd4e252cc0cefd6b56421f3c35f6' \
      --header 'cache-control: no-cache' \
      --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'     
     ```
     - /risks/{riskId} endpoint
      ```bash
      curl --request GET \
        --url http://127.0.0.1:8000/risks/1/ \
        --header 'authorization: Token 08ec57851cc4dd4e252cc0cefd6b56421f3c35f6' \
        --header 'cache-control: no-cache' \
        --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'     
      ```
     
- Configure and use Zappa:
  - Check out [this helpful guide](https://edgarroman.github.io/zappa-django-guide/).
