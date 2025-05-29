provider "aws" {
  region = "us-east-1"
}

# DynamoDB Table
resource "aws_dynamodb_table" "scheduler" {
  name         = "ec2_scheduler"
  billing_mode = "PAY_PER_REQUEST"
  attribute {
    name = "instance_id"
    type = "S"
  }
}

# Lambda Function
resource "aws_lambda_function" "ec2_scheduler" {
  filename      = "lambda_function.zip"
  function_name = "ec2_instance_scheduler"
  role          = aws_iam_role.lambda_role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.8"
}

# IAM Role for Lambda
resource "aws_iam_role" "lambda_role" {
  name = "lambda_execution_role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# EventBridge Rule (Every 5 minutes)
resource "aws_cloudwatch_event_rule" "every_5_min" {
  name        = "every-5-minutes"
  schedule_expression = "rate(5 minutes)"
}

resource "aws_cloudwatch_event_target" "lambda_target" {
  rule      = aws_cloudwatch_event_rule.every_5_min.name
  target_id = "LambdaScheduler"
  arn       = aws_lambda_function.ec2_scheduler.arn
}
