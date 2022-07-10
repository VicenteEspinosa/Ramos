resource "aws_security_group" "app_server" {
  name   = "security-group-app-server"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "ssh"
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "HTTP"
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "HTTPS"
  }
  ingress {
    from_port   = 5672
    to_port     = 5672
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "rabbitmq-5672"
  }

  ingress {
    from_port   = 9000
    to_port     = 9000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Backend"
  }

  ingress {
    from_port   = 9001
    to_port     = 9001
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "async-services"
  }

  ingress {
    from_port   = 15672
    to_port     = 15672
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "rabbitmq-15672"
  }


  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    description = "All Ports Egress"
  }
}

resource "aws_eip" "lb" {
  instance = aws_instance.app_server.id
  vpc      = true
}


resource "aws_instance" "app_server" {
  ami           = "ami-0022f774911c1d690"
  instance_type = "t2.micro"
  vpc_security_group_ids = [aws_security_group.app_server.id]

  tags = {
    Name = "InstanciaEC2Terraform"
  }
}

resource "aws_apigatewayv2_api" "api" {
  name = "Terraform API"
  description = "API Gateway generada por Terraform"
  protocol_type = "HTTP"
}
resource "aws_apigatewayv2_route" "route" {
  api_id    = aws_apigatewayv2_api.api.id
  route_key = "$default"
}




# INTENTO CON API GATEWAY V1


# resource "aws_api_gateway_rest_api" "AppAPI" {
#   name        = "API Gateway Terraform"
#   description = "API Gateway generada por Terraform"
# }

# resource "aws_api_gateway_resource" "AppAPI" {
#   rest_api_id = aws_api_gateway_rest_api.AppAPI.id
#   parent_id   = aws_api_gateway_rest_api.AppAPI.root_resource_id
#   path_part   = "mydemoresource"
# }

# resource "aws_api_gateway_rest_api" "api" {
#   name = "Terraform API"
#   description = "API Gateway generada por Terraform"
# }


# INTENTO INTEGRACION API GATEWAY V2

# resource "aws_apigatewayv2_integration" "integration" {
#   api_id           = aws_apigatewayv2_api.api.id
#   # integration_type = "AWS"
#   integration_type = "AWS"
#   # integration_type = "HTTP_PROXY"


#   connection_type           = "INTERNET"
#   content_handling_strategy = "CONVERT_TO_TEXT"
#   description               = "Terraform API Gateway"
#   integration_method        = "ANY"
#   integration_uri           = aws_instance.app_server.arn
#   # uri = "http://www.ucfriends.tk"
#   # integration_uri           = "http://www.ucfriends.tk/{proxy}"
#   passthrough_behavior      = "WHEN_NO_MATCH"
# }

# resource "aws_api_gateway_method" "api" {
#   rest_api_id   = aws_api_gateway_rest_api.MyDemoAPI.id
#   resource_id   = aws_api_gateway_resource.sendCardResource.id
#   http_method   = "GET"
#   authorization = "NONE"
# }

# resource "aws_apigateway_integration" "integration" {
#   api_id           = aws_apigatewayv2_api.api.id
#   # integration_type = "AWS"
#   integration_type = "HTTP"
#   # integration_type = "HTTP_PROXY"


#   connection_type           = "INTERNET"
#   content_handling_strategy = "CONVERT_TO_TEXT"
#   description               = "Terraform API Gateway"
#   integration_method        = "ANY"
#   # integration_uri           = aws_instance.app_server.arn
#   uri = "http://www.ucfriends.tk"
#   # integration_uri           = "http://www.ucfriends.tk/{proxy}"
# }

# resource "aws_apigatewayv2_stage" "stage" {
#   api_id = aws_apigatewayv2_api.api.id
#   name   = "$default"
# }




