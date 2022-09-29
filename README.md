# Bike Stock Checker

Web scrapper that checks the stock of a product at a specified URL and sends text message / phone call when the stock changes.
* Uses AWS Lambda Function to run ever minute
* Uses AWS DynamoDB to store previous stock
* Uses Twilio Services to send and receive text messages
* CI/CD with Github, AWS Lambda function is auto updated on merge with main
