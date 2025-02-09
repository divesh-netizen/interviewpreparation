variable "project_name" {
  description = "Project Name"
  type        = string
}
variable "aws_region" {
  description = "AWS Region"
  type        = string
}
variable "container_image" {
  description = "Docker Image for ECS"
  type        = string
}
variable "ecs_task_cpu" {
  description = "ECS Task CPU"
  type        = string
}
variable "ecs_task_memory" {
  description = "ECS Task Memory"
  type        = string
}
variable "ecs_desired_count" {
  description = "Number of ECS Tasks"
  type        = number
}
variable "vpc_id" {
  description = "VPC ID"
  type        = string
}
variable "private_subnets" {
  description = "List of Private Subnets"
  type        = list(string)
}
variable "ecs_sg_id" {
  description = "ECS Security Group ID"
  type        = string
}
variable "alb_target_group_arn" {
  description = "ALB Target Group ARN"
  type        = string
}
variable "database_url" {
  description = "PostgreSQL Database URL"
  type        = string
}
variable "celery_broker_url" {
  description = "Celery Broker URL"
  type        = string
}
variable "celery_result_backend" {
  description = "Celery Result Backend"
  type        = string
}
variable "min_task_count" {
  description = "Minimum number of ECS tasks"
  type        = number
  default     = 2
}

variable "max_task_count" {
  description = "Maximum number of ECS tasks"
  type        = number
  default     = 10
}

variable "desired_count" {
  description = "Desired Number of ECS Tasks"
  type        = number
  default     = 2
}