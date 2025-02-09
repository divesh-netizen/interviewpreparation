output "instance_id" {
  value = aws_instance.main.id
}

output "public_ip" {
  value = var.assign_public_ip ? aws_instance.main.public_ip : null
}

output "private_ip" {
  value = aws_instance.main.private_ip
}
