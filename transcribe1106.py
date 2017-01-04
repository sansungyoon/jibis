# [START import_libraries]
import argparse
import base64
import json

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials
# [END import_libraries]


# [START authenticating]
DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                 'version={apiVersion}')


# Application default credentials provided by env variable
# GOOGLE_APPLICATION_CREDENTIALS
def get_speech_service():
    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    credentials.authorize(http)

    return discovery.build(
        'speech', 'v1beta1', http=http, discoveryServiceUrl=DISCOVERY_URL)
# [END authenticating]


def transcribe(speech_file):
    """Transcribe the given audio file.

    Args:
        speech_file: the name of the audio file.
    """
    # [START construct_request]
    with open(speech_file,'rb') as speech:
        # Base64 encode the binary audio file for inclusion in the JSON
        # request.
        speech_content = base64.b64encode(speech.read())

    service = get_speech_service()
    service_request = service.speech().syncrecognize(
        body={
            'config': {
                # There are a bunch of config options you can specify. See
                # https://goo.gl/KPZn97 for the full list.
                'encoding': 'LINEAR16',  # raw 16-bit signed LE samples
                'sampleRate': 44100,  
                # See https://goo.gl/A9KJ1A for a list of supported languages.
                'languageCode': 'ko-KR',  # a BCP-47 language tag
	        #'languageCode': 'us-EN',
            },
            'audio': {

                'content': speech_content.decode('utf-8')
			   
                }
            })
    # [END construct_request]
    # [START send_request]
    response = service_request.execute()
    #return response
    """
    f=open("/home/sansungyoon/newtest1019.txt",'w')
    for i in response['results']:
    	#print response['results'][count]['alternatives'][0]['transcript']
    	temp=i['alternatives'][0]['transcript']
    	#f.write(temp.decode('unicode_escape').encode('utf8'))	
    	f.write(temp.encode('utf8'))
    f.close()
    """

    global temp
    if (response):
    	for i in response['results']:
        	temp=i['alternatives'][0]['transcript']
    		return temp
    #else return NULL

