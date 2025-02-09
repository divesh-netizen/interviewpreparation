output "rds_endpoint" {
  value = aws_db_instance.rds_instance.endpoint
}

output "rds_arn" {
  value = aws_db_instance.rds_instance.arn
}
