# Get Lambda Instances

Use GitHub Actions to get the lambda cloud instances you want.

## Setup

1. Fork this repo

2. Add your Lambda [cloud token](https://cloud.lambdalabs.com/api-keys) as a new [repository secret](https://github.com/hamelsmu/get-lambda/settings/secrets/actions) named `LAMBDA_CLOUD_TOKEN`.  You should also set the `LAMBDA_CLOUD_TOKEN` environment variable locally.

3. Setup a new [ssh key in lambda](https://cloud.lambdalabs.com/ssh-keys) named `lambda-new`.  And save the private key locally. You will need the private key to ssh into the instance after it is created.

## Run the workflow to get your Lambda instance

4. Go to your Actions tab and enable workflows if they aren't already enabled.  Then click on the `Create Instance` workflow and select the kind of GPU that works for you:

![](actions.png)







