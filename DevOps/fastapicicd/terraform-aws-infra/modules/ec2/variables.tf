variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
}

variable "instance_type" {
  description = "Instance type (t3.micro, t3.small, etc.)"
  type        = string
}

variable "subnet_id" {
  description = "Subnet ID where EC2 will be launched"
  type        = string
}

variable "vpc_id" {
  description = "VPC ID"
  type        = string
}

variable "key_name" {
  description = "SSH key name for instance login"
  type        = string
}

variable "assign_public_ip" {
  description = "Assign a public IP (true/false)"
  type        = bool
}

variable "allowed_ssh_cidrs" {
  description = "Allowed CIDRs for SSH access"
  type        = list(string)
}

variable "project_name" {
  description = "Project Name"
  type        = string
}

variable "environment" {
  description = "Deployment environment (dev/staging/prod)"
  type        = string
}

variable "instance_name" {
  description = "Name of the EC2 instance"
  type        = string
}
