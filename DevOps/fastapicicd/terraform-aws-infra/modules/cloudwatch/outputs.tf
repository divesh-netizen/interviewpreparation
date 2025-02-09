output "ecs_log_group" {
  value = aws_cloudwatch_log_group.ecs_log_group.name
}

output "rds_log_group" {
  value = aws_cloudwatch_log_group.rds_log_group.name
}
