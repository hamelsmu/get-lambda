# Get Lambda Instances

Use GitHub Actions to get the lambda cloud instances you want.

## Setup

1. Fork this repo

2. Add your Lambda [cloud token](https://cloud.lambdalabs.com/api-keys) as a new [repository secret](https://github.com/hamelsmu/get-lambda/settings/secrets/actions).

3. Setup a new [ssh key in lambda](https://cloud.lambdalabs.com/ssh-keys) named `lambda-new`.  And save the private key locally. You will need the private key to ssh into the instance after it is created.

4. Go to your Actions tab and enable workflows if they aren't already enabled.  Then click on the `Lambda Instance Creation`





