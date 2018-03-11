# sam-scheduled-lambda

This is a basic example of deploying a scheduled lambda using SAM
It is deployed using either [AWS Cloudformation](https://aws.amazon.com/cli/) or [SAM Local](https://github.com/awslabs/aws-sam-local)

*You will need to provide a S3 bucket when packaging for deployment*

## Testing locally using SAM Local ##

`sam local invoke --event event.json`

## Packaging for deployment
### AWS Cloudformation
`aws cloudformation package --template-file template.yaml --s3-bucket *your-s3-bucket* --output-template-file packaged.yaml`

### SAM Local
`sam package --template-file template.yaml --s3-bucket *your-s3-bucket* --output-template-file packaged.yaml`

## Deploying
### AWS Cloudformation
`aws cloudformation deploy --template-file ./packaged.yaml --stack-name ScheduledLambda --capabilities CAPABILITY_IAM`

### SAM Local
`sam deploy --template-file ./packaged.yaml --stack-name ScheduledLambda --capabilities CAPABILITY_IAM`
