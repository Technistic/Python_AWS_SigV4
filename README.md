# Python_AWS_SigV4

## Introduction
A basic Python script that tests AWS Signature V4 authentication signing requests.

It uses the [requests-auth-aws-sigv4](https://github.com/andrewjroth/requests-auth-aws-sigv4) module that adds
AWS Signature v4 signing to the Python [requests](https://requests.readthedocs.io/en/latest/) module.

Rather than coding your AWS access key and secret in the script, you can set the AWS_ACCESS_KEY and AWS_SECRET environment variables as follows:

```
export AWS_ACCESS_KEY_ID=MyAccessKey
export AWS_SECRET_ACCESS_KEY=ThisIsSecret
export AWS_SESSION_TOKEN=ThisIsTheToken
```

Set the Logging Level of the [requests-auth-aws-sigv4](https://github.com/andrewjroth/requests-auth-aws-sigv4) module to DEBUG to see the generated headers and signature.