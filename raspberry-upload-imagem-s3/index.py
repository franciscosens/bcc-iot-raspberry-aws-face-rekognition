import wget, boto3, os

def gerar_menu():
  opcao = "0"
  while(opcao != "8001"):
    print()
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("|                   MENU                   |")
    print("|__________________________________________|")
    print("| 1    Tirar foto e enviar para amazon     |")
    print("|                                          |")
    print("| 8001 Sair                                |")
    print("|                                          |")
    print("|__________________________________________|")
    print()
    opcao = input()
    os.system('cls')
    if(opcao == "1"):
      obter_imagem_upload()
    elif(opcao == "8001"):
      print("Obrigado pro brincar com nosso software")
    else:
      print("Opção inválida jovem")

def obter_imagem_upload():
  # url = "http://201.54.201.38:8080/?action=snapshot"
  # nome = wget.download(url, out="foto.jpg")
  # print("Foto " + nome + " resgatada com sucesso: ")
  nome = "foto.jpg"
  client = boto3.client(
      's3',
      aws_access_key_id='AKIAJWHY4NS3KZ2YO6NA',
      aws_secret_access_key='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'
  )

  with open(nome, "rb") as data:
    print("Iniciando o processo de upload da foto....")
    client.upload_fileobj(data, "aws-rekognition-face", nome)
    print("Foto enviada com sucesso para amazon s3")

os.system("cls")
gerar_menu()