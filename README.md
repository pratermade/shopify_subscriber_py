# shopify_subscriber_py
Lambda functions for dealing with new subscribers to a shopify store



To Deploy:
```
mkdir deployment
cd deployment
pip install -r ../requirements.txt --target package
cp ../lambda_function.py .
pip install -r ../requirements.txt --target package
cd ..
aws lambda update-function-code --function-name shopify_subscriber --zip-file fileb://shopify_subscriber.zip
```