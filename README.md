# Overiew
AWS Account Password Policy Resource Type Demo. 
This will allow to create a private Resource Type called MY::IAM::PasswordPolicy

# Install python cfn plugin and verify it
python -m pip install --upgrade cloudformation-cli-python-plugin
cfn --version 

# To test the Resource Type
cfn test

# To Submit the Resource Type to AWS Cloudformation Registry
cfn submit --set-default

# To create resource using the Resource Type 
aws cloudformation deploy --stack-name my-iam-passwordpolicy-stack --template-file test-resource-type.yaml
