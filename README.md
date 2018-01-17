# insurance-risks-api
A serverless Django API project. 

[![Build Status](https://travis-ci.org/bayodesegun/insurance-risks-api.svg?branch=master)](https://travis-ci.org/bayodesegun/insurance-risks-api)

## API Endpoints
- (*test users/passwords*: geek/password, nerd/password)
- ``POST`` ``/obtain-token/`` - obtain authentication token
- ``GET`` [/risks/](https://api.ins-risks.bayodesegun.com/risks/)  - list all risks for a given user
- ``GET`` [/risks/{riskId}](https://api.ins-risks.bayodesegun.com/risks/1) - display details for a given risk

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
- Test the API endpoints (*test users/passwords*: geek/password, nerd/password):
  - Make a POST call to endpoint ```/obtain-token/``` to obtain a token. Example using shell cURL:
    ```bash
    curl --request POST \
    --url https://api.ins-risks.bayodesegun.com/obtain-token/ \
    --header 'cache-control: no-cache' \
    --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
    --form username=geek \
    --form password=password
    ```
  - Make the respective GET calls using obtained token: 
     - /risks/ endpoint
     ```bash
     curl --request GET \
      --url https://api.ins-risks.bayodesegun.com/risks/ \
      --header 'authorization: Token 08ec57851cc4dd4e252cc0cefd6b56421f3c35f6' \
      --header 'cache-control: no-cache' \
      --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'     
     ```
     - /risks/{riskId} endpoint
      ```bash
      curl --request GET \
        --url https://api.ins-risks.bayodesegun.com/risks/1/ \
        --header 'authorization: Token 08ec57851cc4dd4e252cc0cefd6b56421f3c35f6' \
        --header 'cache-control: no-cache' \
        --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'     
      ```
     
- Configure and use Zappa:
  - Check out [this helpful guide](https://edgarroman.github.io/zappa-django-guide/).
