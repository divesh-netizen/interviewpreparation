resource "aws_db_subnet_group" "rds_subnet_group" {
  name       = "${var.project_name}-rds-subnet-group"
  subnet_ids = var.subnet_ids

  tags = {
    Name = "${var.project_name}-rds-subnet-group"
  }
}

resource "aws_db_instance" "rds_instance" {
  identifier             = "${var.project_name}-rds"
  engine                 = "postgres"
  engine_version         = "15"
  instance_class         = var.instance_type
  allocated_storage      = var.storage
  storage_encrypted      = true
  multi_az               = var.multi_az
  username               = var.db_username
  password               = var.db_password
  db_subnet_group_name   = aws_db_subnet_group.rds_subnet_group.name
  vpc_security_group_ids = [var.security_group_id]
  publicly_accessible    = false
  skip_final_snapshot    = true

  tags = {
    Name = "${var.project_name}-rds"
  }
}
