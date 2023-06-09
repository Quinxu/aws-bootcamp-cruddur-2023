# Week 6 — Deploying Containers

## Provision ECS Cluster - cruddur	
## Created ECR repos and pushed image for backend-flask	
## Deployed Backend Flask app as a service to Fargate	
## Created ECR repo and pushed image for fronted-react-js	
## Deployed Frontend React JS app as a service to Fargate	
## Provision and configure Application Load Balancer along with target groups	
## Managed domain using Route53 via hosted zone	
## Created an SSL certificate via ACM	
##  Setup a record set for naked domain to point to frontend-react-js	
## Setup a record set for api subdomain to point to the backend-flask	
##	Configure CORS to only permit traffic from our domain	
##	Secured Flask by not running in debug mode	
##	Implemented Refresh Token for Amazon Cognito	
##	Configure task definitions to contain x-ray and turn on Container Insights	
##	Changed Docker Compose to explicitly use a user-defined network	
##	Created Dockerfile specifically for production use case	
##	Used ruby generate out .env files for docker using erb templates