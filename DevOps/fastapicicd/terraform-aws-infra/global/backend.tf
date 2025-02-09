terraform {
  backend "s3" {
    bucket         = "my-terraform-state-bucket" # Replace with your bucket name
    key            = "global/terraform.tfstate"
    region         = "us-east-1" # Change based on your AWS region
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}
