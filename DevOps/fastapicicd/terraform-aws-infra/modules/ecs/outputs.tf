output "ecs_cluster_id" {
  value = aws_ecs_cluster.main.id
}

output "ecs_service_id" {
  value = aws_ecs_service.app.id
}

output "ecs_task_definition" {
  value = aws_ecs_task_definition.app.arn
}

output "ecs_scaling_target_id" {
  value = aws_appautoscaling_target.ecs_target.id
}

output "ecs_scaling_policy_out_id" {
  value = aws_appautoscaling_policy.scale_out.id
}

output "ecs_scaling_policy_in_id" {
  value = aws_appautoscaling_policy.scale_in.id
}
