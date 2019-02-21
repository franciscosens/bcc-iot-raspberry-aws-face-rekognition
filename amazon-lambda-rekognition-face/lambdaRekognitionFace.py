import json
import boto3

bucket = 'aws-rekognition-face'
collectionId = 'FotosPerfilCollection'
nomeFoto = ''

def lambda_handler(event, context):
    # TODO pegar o nome da foto
    
    # criar_collection()
    index_face_to_collection()
    reconhecer_foto() # TODO obter percentual do resultado

    # Enviar por mqtt para o percentual da resposta

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


def index_face_to_collection():
    photo = 'photo'

    client = boto3.client('rekognition')

    response = client.index_faces

    response = client.index_faces(CollectionId=collectionId,
                                  Image={'S3Object': {
                                      'Bucket': bucket, 'Name': photo}},
                                  ExternalImageId=photo,
                                  MaxFaces=1,
                                  QualityFilter="AUTO",
                                  DetectionAttributes=['ALL'])

    print('Results for ' + photo)
    print('Faces indexed:')
    for faceRecord in response['FaceRecords']:
        print('  Face ID: ' + faceRecord['Face']['FaceId'])
        print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))

    print('Faces not indexed:')
    for unindexedFace in response['UnindexedFaces']:
        print(' Location: {}'.format(
            unindexedFace['FaceDetail']['BoundingBox']))
        print(' Reasons:')
        for reason in unindexedFace['Reasons']:
            print('   ' + reason)


def criar_collection():
    maxResults = 2

    client = boto3.client('rekognition')

    print('Criando a coleção:' + collectionId)
    response = client.create_collection(CollectionId=collectionId)
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Criado com sucesso...')


def reconhecer_foto():
    fileName = 'foto.jpg'
    threshold = 70
    maxFaces = 2

    client = boto3.client('rekognition')

    response = client.search_faces_by_image(CollectionId=collectionId,
                                            Image={'S3Object': {
                                                'Bucket': bucket, 'Name': fileName}},
                                            FaceMatchThreshold=threshold,
                                            MaxFaces=maxFaces)

    faceMatches = response['FaceMatches']
    print('Matching faces')
    for match in faceMatches:
        print('FaceId:' + match['Face']['FaceId'])
        print('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
        print
