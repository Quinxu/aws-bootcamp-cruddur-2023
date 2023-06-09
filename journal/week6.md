# Week 6 — Deploying Containers

##1. Provision ECS Cluster - cruddur	
##2. Created ECR repos and pushed image for backend-flask	
##3. Deployed Backend Flask app as a service to Fargate	
##4. Created ECR repo and pushed image for fronted-react-js	
##5. Deployed Frontend React JS app as a service to Fargate	
##6. Provision and configure Application Load Balancer along with target groups	
##7. Managed domain using Route53 via hosted zone	
##8. Created an SSL certificate via ACM	
##9.  Setup a record set for naked domain to point to frontend-react-js	
##10. Setup a record set for api subdomain to point to the backend-flask	
##11.	Configure CORS to only permit traffic from our domain	
##12.	Secured Flask by not running in debug mode	
##13.	Implemented Refresh Token for Amazon Cognito	
##14.	Configure task definitions to contain x-ray and turn on Container Insights	
##15.	Changed Docker Compose to explicitly use a user-defined network	
##16.	Created Dockerfile specifically for production use case	
##17.	Used ruby generate out .env files for docker using erb templates