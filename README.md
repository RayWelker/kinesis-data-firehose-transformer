# AWS Lambda Kinesis Data Firehose Log Transformer

This is a Python script designed to be used as an AWS Lambda function for Kinesis Data Firehose. It acts as a log stream transformer for badly formatted messages.

## Overview

The script processes incoming records, attempting to decode and load JSON data. If a record is found to be badly formatted, the script will attempt to transform the record and include additional information, such as a timestamp and a flag indicating the bad format.

If there are invalid logs that cannot be transformed, the function will print the firehose stream and the invalid logs.

## Requirements

- Python 3.8 or later
- An AWS Lambda environment configured with the necessary IAM roles and permissions
- A Kinesis Data Firehose delivery stream

## Setup

1. Create a new Lambda function in the AWS Management Console.
2. Set the runtime to Python 3.8 or later.
3. Upload the provided script as the function code.
4. Configure the Lambda function with the appropriate IAM roles and permissions for accessing Kinesis Data Firehose.
5. Configure the Kinesis Data Firehose delivery stream to use the Lambda function as a data transformation step.

## Usage

The script is intended to be executed automatically by the Kinesis Data Firehose service when records are delivered to the stream.

## Function Input

The AWS Lambda function handler receives an `event` object as input, which contains the following keys:

- `deliveryStreamArn`: The ARN of the Kinesis Data Firehose delivery stream.
- `records`: An array of records to be processed, where each record is an object with the following keys:
  - `recordId`: The unique identifier for the record.
  - `data`: The base64-encoded data payload.

## Function Output

The function returns an object with the following keys:

- `records`: An array of processed records, where each record is an object with the following keys:
  - `recordId`: The unique identifier for the record.
  - `result`: A string indicating the result of the processing ('Ok' if successful).
  - `data`: The base64-encoded transformed data payload (if the record was transformed due to a bad format).

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
