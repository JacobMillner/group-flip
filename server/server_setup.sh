#!/bin/bash

echo "Installing Requirements as: $APP_ENV"
if [ "$APP_ENV" == "development" ]; then
    pip install -r dev_req.txt
else
    pip install -r prod_req.txt
fi
