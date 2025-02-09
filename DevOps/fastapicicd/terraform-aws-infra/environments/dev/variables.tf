variable "environment" {
  description = "The environment (dev, staging, prod)"
  type        = string
}

variable "project_name" {
  description = "The name of the project"
  type        = string
}

variable "aws_region" {
  description = "AWS region where resources will be deployed"
  type        = string
  default     = "us-east-1"
}

variable "vpc_id" {
  description = "VPC ID for the environment"
  type        = string
}

variable "public_subnet_ids" {
  description = "List of public subnet IDs for ALB, EC2, etc."
  type        = list(string)
}

variable "private_subnet_ids" {
  description = "List of private subnet IDs for ECS, RDS, etc."
  type        = list(string)
}

variable "database_url" {
  description = "The connection URL for the PostgreSQL database"
  type        = string
}

variable "redis_url" {
  description = "Redis connection URL for Celery"
  type        = string
}

variable "app_image_url" {
  description = "ECR URL of the application Docker image"
  type        = string
}

variable "desired_count" {
  description = "Desired number of ECS tasks"
  type        = number
  default     = 2
}

variable "min_task_count" {
  description = "Minimum number of ECS tasks in auto-scaling"
  type        = number
  default     = 2
}

variable "max_task_count" {
  description = "Maximum number of ECS tasks in auto-scaling"
  type        = number
  default     = 10
}

variable "cpu_target_value" {
  description = "Target CPU utilization for ECS auto-scaling"
  type        = number
  default     = 50
}

variable "memory_target_value" {
  description = "Target Memory utilization for ECS auto-scaling"
  type        = number
  default     = 50
}

variable "acm_certificate_arn" {
  description = "ARN of the ACM SSL certificate for the ALB"
  type        = string
}

variable "alarm_sns_topic" {
  description = "SNS Topic ARN for CloudWatch Alarms"
  type        = string
}

variable "db_name" {
  description = "Database name for RDS"
  type        = string
  default     = "fastapi_db"
}

variable "db_username" {
  description = "Database username for RDS"
  type        = string
}

variable "db_password" {
  description = "Database password for RDS"
  type        = string
  sensitive   = true
}

variable "celery_broker_url" {
  description = "Broker URL for Celery"
  type        = string
}