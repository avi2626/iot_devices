# Airplane IOT devices REST API application

This is a API that support CRUD operations on IOT airplane devices.

The application uses the Django REST framework and a MongoDB Database.

The application uses Docker, please follow the install guidelines to run the application.

## Install

    docker build . -t iot_airplane_devices

## Run the app

    docker-compose up

# REST API

<!-- The REST API to the example app is described below. -->

## Get list of all devices

### Request

`GET /devices`

    curl --location --request GET 'http://localhost:8000/devices' \
    --header 'Accept-Encoding: application/json'

### Response

    [
    {
        "id": "device3",
        "serial_number": "12345678",
        "description": "A great device",
        "airplane": "airplane1"
    },
    {
        "id": "device4",
        "serial_number": "123456789",
        "description": "A great device",
        "airplane": "airplane2"
    }
    ]

## Create a new device

### Request

`POST /devices`

    curl --location --request POST 'http://localhost:8000/devices/' \
    --header 'Accept-Encoding: application/json' \
    --header 'Content-Type: application/json' \
    --data-raw '{
    "id": "device1",
    "serial_number": "1234567",
    "description": "A great device",
    "airplane": "airplane1"
    }'

### Response

    {
    "id": "device1",
    "serial_number": "1234567",
    "description": "A great device",
    "airplane": "airplane1"
    }

## Get a specific Device

### Request

`GET /devices/:id`

    curl --location --request GET 'http://localhost:8000/devices/device1' \
    --header 'Accept-Encoding: application/json'

### Response

    {
    "id": "device1",
    "serial_number": "1234567",
    "description": "A great device",
    "airplane": "airplane1"
    }

## Change a device field

### Request

`PATCH /devices/:id`

    curl --location --request PATCH 'http://localhost:8000/devices/device1' \
     --header 'Accept-Encoding: application/json' \
     --header 'Content-Type: application/json' \
     --data-raw '{
    "description": "A very great device"
    }'

### Response

    {
        "id": "device1",
        "serial_number": "1234567",
        "description": "A very great device",
        "airplane": "airplane1"
    }

## Mark a device as deleted

### Request

`DELETE /devices/id`

    curl --location --request DELETE 'http://localhost:8000/devices/device1'

### Response

    'Success'
