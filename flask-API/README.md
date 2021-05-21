FLASK app to demonstrate REST API
==============================

This is a bare-bones example of a task specified in Devsnest's [`WEB DEV Intro | Python Flask Framework Basics`](https://www.youtube.com/watch?v=uK7pKciYRis&ab_channel=Devsnest)

The entire application is contained within the [`flaskapi.py`](flaskapi.py/) file.

The repo also holds [`devsnest-flask-api.postman_collection.json`](devsnest-flask-api.postman_collection.json/) which can be imported as POSTMAN collection
## Install
`pip3 install -r requirements.txt`

## Run the app
`python3 flask.py`

# REST API

The REST API to the API app is described below.

## ADD A STRING

### Request [GET]

`GET /add/<your string>`

    curl -i -H 'Accept: application/json' http://localhost:5000/add/helloworld

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    The string helloworld has been saved in the server!

### Request [POST]

`POST /add`
    
    curl -i --header "Content-Type: application/json" --request POST --data '{"string":"helloworld"}' http://localhost:5000/add

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Content-Length: 36

    The string helloworld has been saved in the server!

## Concat all the strings that have been submitted

### Request

`GET /concat`

    curl -i -H 'Accept: application/json' http://localhost:5000/concat

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 36

    helloworld helloworld