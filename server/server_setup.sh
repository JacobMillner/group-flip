#!/bin/bash

echo "Installing Requirements as: $APP_ENV"
if [ "$APP_ENV" == "production" ]; then
    pip install -r prod_req.txt
else
    pip install -r dev_req.txt
fi
