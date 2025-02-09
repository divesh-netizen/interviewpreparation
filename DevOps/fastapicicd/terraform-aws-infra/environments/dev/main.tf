module "vpc" {
  source               = "../../modules/vpc"
  vpc_cidr             = "10.0.0.0/16"
  public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnet_cidrs = ["10.0.3.0/24", "10.0.4.0/24"]
  azs                  = ["us-east-1a", "us-east-1b"]
  project_name         = var.project_name
  environment          = var.environment
}

module "ec2_jenkins" {
  source            = "../../modules/ec2"
  ami_id            = "ami-0c55b159cbfafe1f0"
  instance_type     = "t3.micro"
  subnet_id         = module.vpc.public_subnet_ids[0]
  vpc_id            = module.vpc.vpc_id
  key_name          = "my-key"
  assign_public_ip  = true
  allowed_ssh_cidrs = ["0.0.0.0/0"]
  project_name      = var.project_name
  environment       = var.environment
  instance_name     = "jenkins-server"
}

module "alb" {
  source                     = "../../modules/alb"
  project_name               = var.project_name
  environment                = var.environment
  vpc_id                     = module.vpc.vpc_id
  public_subnet_ids          = module.vpc.public_subnet_ids
  acm_certificate_arn        = "arn:aws:acm:region:account-id:certificate/xxxxxx"
  enable_deletion_protection = false
}

module "ecs" {
  source               = "../../modules/ecs"
  project_name         = var.project_name
  aws_region           = var.aws_region
  vpc_id               = module.vpc.vpc_id
  private_subnets      = module.vpc.private_subnet_ids
  alb_target_group_arn = module.alb.target_group_arn
  ecs_sg_id             = module.security.ecs_sg_id
  container_image      = "123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:latest"

  ecs_task_cpu      = 512
  ecs_task_memory   = 1024
  ecs_desired_count = 2

  celery_broker_url     = var.redis_url
  celery_result_backend = var.celery_broker_url
  database_url          = module.rds.rds_endpoint
}



module "rds" {
  source            = "../../modules/rds"
  project_name      = var.project_name
  subnet_ids        = module.vpc.private_subnet_ids         # ✅ Fixing private_subnet_ids -> subnet_ids
  security_group_id = module.security.rds_sg_id # ✅ Fixing missing security group
  db_username       = "admin"                               # ✅ Fixing username -> db_username
  db_password       = "SuperSecurePassword123!"             # ✅ Fixing password -> db_password
}


module "s3" {
  source              = "../../modules/s3"
  project_name        = var.project_name
  s3_bucket_name      = "${var.project_name}-${var.environment}-tf-state" # ✅ Fixing missing s3_bucket_name
  dynamodb_table_name = "${var.project_name}-${var.environment}-tf-lock"  # ✅ Fixing missing dynamodb_table_name
}


module "cloudwatch" {
  source          = "../../modules/cloudwatch"
  app_name        = var.project_name
  alarm_sns_topic = "arn:aws:sns:us-east-1:123456789012:dev-alerts"
}

module "security" {
  source       = "../../modules/security"
  project_name = var.project_name
  vpc_id       = module.vpc.vpc_id
}

module "iam" {
  source       = "../../modules/iam"
  project_name = var.project_name
}

