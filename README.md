I tried building the project called CV Challenge, which I came across in a video by [LuNiZz (Can Değer)](https://github.com/LuNiZz) on YouTube. It was a highly educational process for me in terms of both improving my technical skills and gaining hands-on project experience.

For those who want to get detailed information about the challenge, I am leaving the GitHub documentation in roadmap format prepared by Can Değer here:
[CV Challenge Documentation](https://github.com/LuNiZz/siber-guvenlik-sss/blob/master/Belgeler/Dokumanlar/CV_Challenge.md)

How Did I Build the Project?
• I designed a blog site in CV format using HTML and CSS.
• I transferred the site folder to a GitHub repository using GitHub Desktop.
• Using AWS CodePipeline, I integrated this repository with an S3 Bucket and enabled the static web hosting feature.
• I published the site via the domain provided by AWS. Later, I set up a CloudFront distribution to add HTTPS support.
• For a more professional look, I purchased the halitsen.online domain and integrated it with the CloudFront distribution using Route 53.

Visitor Counter Feature:
• I added a visitor counter to the page using HTML/CSS.
• I wrote a JavaScript script to fetch the counter data.
• I used AWS DynamoDB as the data source.
• For a secure connection, I routed communication through AWS API Gateway rather than directly to the database.
• I created an AWS Lambda function with Python + boto3 to increment the counter value.
• Since I offer the site in two languages, English and Turkish, I wanted to use a separate counter for each language. For this purpose, I added a second counter field to DynamoDB and a separate Lambda function. I then integrated this new Lambda function with the same API Gateway.
• By placing another CloudFront layer in front of the API Gateway, I improved both performance and security. Additionally, I configured CORS settings to accept requests only from my own domain.

CI/CD and Testing Process:
• I created a separate GitHub repository for my Lambda functions.
• I used the unittest and mock libraries to test my code.
• I set up an automated testing and deployment process with GitHub Actions. Thus, once my code passes the tests, it is deployed autonomously to the AWS Lambda functions.

If You Want to Visit My Page:
👉 [halitsen.cloud](https://halitsen.cloud/)

To better explain the project, I have prepared a topological architecture diagram showing all components and their relationships. You can visually explore the entire structure, from GitHub to AWS, and from the database to the Lambda functions.

<img width="905" height="698" alt="Ekran Resmi 2025-08-16 10 21 42" src="https://github.com/user-attachments/assets/4ecb42be-cd86-4757-af87-52e5d698dedb" />

