import aws_cdk as core
import aws_cdk.assertions as assertions

from sales_lambda_athena_project.sales_lambda_athena_project_stack import SalesLambdaAthenaProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sales_lambda_athena_project/sales_lambda_athena_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SalesLambdaAthenaProjectStack(app, "sales-lambda-athena-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
