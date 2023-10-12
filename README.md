# <p align="center"> AWS Vision Insights</p>

### <p align="center"> Image analysis and emotions classification with Amazon Rekognition </p>

  <p align="center" >
    <img src="https://img.shields.io/badge/-AWS%20API%20Gateway-000?&logo=amazonapigateway" height="25">
    <img src="https://img.shields.io/badge/-AWS%20Lambda-000?&logo=awslambda" height="25">
    <img src="https://img.shields.io/badge/-AWS%20Rekognition-000?&logo=amazon-aws" height="25">
    <img src="https://img.shields.io/badge/-AWS%20S3-000?&logo=amazons3" height="25">
    <img src="https://img.shields.io/badge/-Python-000?&logo=python&logoColor=3776AB" height="25">
    <img src="https://img.shields.io/badge/-Serverless-000?&logo=serverless" height="25">
  </p>

## 📖 Summary

- [1 - AWS Architecture](#anchor1)
- [2 - How to use](#anchor2)
- [3 - File structure](#anchor3)

<a id="anchor1"></a>

## 2 - AWS Architecture

![AWS Architecture](./assets/aws-architecture.png)

<a id="anchor2"></a>

## 2 - How to use:

Clone this repository:
```
git clone https://github.com/LuizScarsi/aws-vision-insights.git
```
Inside the `src` folder:
- Create a `.env` file to store the `BUCKET_NAME` and `AWS_REGION_NAME`:
    ```
    touch .env
    ```

- Follow the example from `example.env` file:

    ```
    BUCKET_NAME=bucket-name
    AWS_REGION_NAME=region-name
    ```

Install serverless framework. More information [here](https://www.serverless.com/framework/docs/getting-started)

```bash
npm install -g serverless
```

Create your credentials (AWS Acess Key and AWS Secret Access Key) with IAM. More information [here](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)

Run the following command inserting your credentials:

```bash
serverless config credentials \
  --provider aws \
  --key AKIAIOSFODNN7EXAMPLE \
  --secret wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

It is also possible to configure with [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) running the following command:

```
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-east-1
Default output format [None]: ENTER
```

To deploy in your AWS account access the `src` folder and run:

```bash
serverless deploy
```

<a id="anchor3"></a>

## 3 File structure:

- **src**
  - **controllers**
    - ```v1_controller.py```
    - ```v2_controller.py```
  - **routes**
    - **v1**
      - ```v1_description.py```
      - ```v1_vision.py```
    - **v2**
      - ```v2_description.py```
      - ```v2_vision.py```
    - ```health.py```
  - **services**
    - ```rekognition.py```
    - ```s3.py```
  - **utils**
    - `util.py`
  - `.example.env`
  - `serveless.yaml`
- `README.md`