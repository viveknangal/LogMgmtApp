provider "aws" {
  region = "eu-central-1"
}

terraform {
  backend "s3" {
    bucket  = "prod-tf-state-honestbee"
    key     = "prod/terraform.tfstate"
    region  = "eu-central-1"
    encrypt = true
  }
}

resource "aws_s3_bucket" "nginx-logs" {
  bucket = "prod-nginx-logs"
  acl    = "private"

  tags {
    Name        = "prod-nginx-logs"
    Environment = "Prod"
  }
}
