import boto3

def detect_text(photo, bucket):

    client=boto3.client('rekognition')

    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
                        
    textDetections=response['TextDetections']
    texts = []
    for text in textDetections:
            texts += [text['DetectedText']]
    print(texts)
    return len(textDetections)

def main():

    bucket='herb-transcription'
    photo='00354320c.jpg'
    text_count=detect_text(photo,bucket)
    print("Text detected: " + str(text_count))

if __name__ == "__main__":
    main()
 
