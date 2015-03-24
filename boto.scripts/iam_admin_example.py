"""
IAM boto examples:
In this example, we show how to create a group
for administrators who have full access to IAM
functionality but no access to other AWS services.
"""
import boto

#
# First create a connection to the IAM service
#
iam = boto.connect_iam()

#
# Create an Admin group for users who have admin privilege
# First, create the group
#
response = iam.create_group('Admins')

#
# Next, associate a JSON policy with the group that provides
# access to all IAM actions.
#
admin_policy = """
{
   "Statement":[{
      "Effect":"Allow",
      "Action":"*",
      "Resource":"*"
      }
   ]
}"""
response = iam.put_group_policy('Admins', 'AdminPolicy', admin_policy)

#
# Now create a new user and add her to the Admin group.
#
response = iam.create_user('Sue')
user = response.user

response = iam.add_user_to_group('Admins', 'Sue')
