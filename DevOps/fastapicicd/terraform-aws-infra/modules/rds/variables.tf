variable "project_name" {
  description = "Project Name"
  type        = string
}
variable "subnet_ids" {
  description = "List of subnet IDs"
  type        = list(string)
}
variable "security_group_id" {
  description = "Security Group ID for RDS"
  type        = string
}
variable "db_username" {
  description = "Database username"
  type        = string
}
variable "db_password" {
  description = "Database password"
  type        = string
}
variable "storage" {
  description = "Allocated storage (GB)"
  type        = number
  default     = 20
}
variable "instance_type" {
  description = "RDS instance type"
  type        = string
  default     = "db.t3.micro"
}
variable "multi_az" {
  description = "Enable Multi-AZ for HA"
  type        = bool
  default     = false
}
