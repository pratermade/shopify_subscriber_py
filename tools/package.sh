#!/usr/bin/bash

pwd
rm -rf deployment
rm shopify_subscriber.zip
mkdir deployment
cd deployment
pip install -r ../requirements.txt --target package
cp ../lambda_function.py .
zip -r ../shopify_subscriber.zip .
cd ..
aws lambda update-function-code --function-name shopify_subscriber --zip-file fileb://shopify_subscriber.zip