from rest_framework.authentication import BasicAuthentication, BaseAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from node.models import Node
from base64 import b64decode
import json


class BasicOrTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Check if basic authentication credentials are provided
        auth = request.headers.get("Authorization")
        #print(request.GET)
        sender_host_list = request.GET.getlist("request_host")
        if sender_host_list:
            sender_host = sender_host_list[0]
            if sender_host[-1] == "/":
                sender_host = sender_host[0:-1]
            print("SENDER HOST", sender_host)
        else:
            print("No request host provided")
        if auth:
            print("auth provided")
            # Parse basic auth header
            try:
                auth_type, auth_string = auth.split()
                if auth_type.lower() == "basic":
                    username, password = (
                        b64decode(auth_string.encode()).decode().split(":")
                    )
                    print("stuff", username, password)
                    # print("Basic auth found", sender_host, username, password)
                    # check if the user exists in the database
                    node = Node.objects.get(
                        host=sender_host,
                        username=username,
                        password=password,
                        isActive=True,
                    )
                    # if authentication is successful, return success response
                    print("Node", node)
                    if node:
                        print("Basic auth successful")
                        return (node, None)
                    else:
                        # If the user does not exist, return failure response
                        print("Basic auth failed")
                        return AuthenticationFailed("Unauthorized")

            except:
                pass  # If parsing fails or credentials are incorrect, proceed to token authentication

        # If basic authentication fails or is not provided, try token authentication
        token_auth = JWTAuthentication()
        print("Trying token auth")
        try:
            user, token = token_auth.authenticate(request)

            if user is None:
                raise AuthenticationFailed(
                    "Unauthorized"
                )  # Return unauthorized response
            return user, token
        except:
            raise AuthenticationFailed("Unauthorized")
