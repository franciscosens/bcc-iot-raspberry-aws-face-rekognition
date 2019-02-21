import wget, boto3


url = "http://201.54.201.38:8080/?action=snapshot"
name = wget.download(url, out="foto.jpg")
print()
print("obtida a foto: " + name)

client = boto3.client(
  's3', 
  aws_access_key_id = "AKIAIVZOZUKK27KAYUWA",
  aws_secret_access_key = "jxxReSah+YthD9gkeENpUsOaurh8F+pEOe5E6zvI0"
)

response = client.list_objects("aws-rekognition-face")
print(response)

# with open(name, "rb") as data:
#   print(name)
#   client.upload_fileobj(data, "aws-rekognition-face", 'mykey')
#   print("enviada a foto para amazon s3")

