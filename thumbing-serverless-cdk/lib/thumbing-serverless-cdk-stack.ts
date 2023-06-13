import * as cdk from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';
import { Construct } from 'constructs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class ThumbingServerlessCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here

    // example resource
    // const queue = new sqs.Queue(this, 'ThumbingServerlessCdkQueue', {
    //   visibilityTimeout: cdk.Duration.seconds(300)
    // });

    const buckName: string = process.env.THUMBING_BUCKET_NAME as string;
    const bucket= this.createBucket(buckName);


  }

  createBucket(buckName: string):s3.IBucket{
    const bucket = new s3.Bucket(this, 'ThumblingBucket', {
      bucketName: buckName,
      removalPolicy:cdk.RemovalPolicy.DESTROY
    });
    return bucket;
  }

}


