import base64
import datetime
import json
import re

def lambda_handler(event, context):
  result = []
  invalidLogs = []
  firehoseStream = event['deliveryStreamArn']
  for record in event['records']:
      try:
          payload = base64.b64decode(record['data'])
          data = json.loads(payload)
          result_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': record['data']
          }
          result.append(result_record)
      except:
          try:
              bdecoded = base64.b64decode(str.encode(record['data']))
              if re.search(b'[a-zA-Z]', bdecoded[:-2]) or sys.getsizeof(log) < 1000:
                data = base64.b64encode(json.dumps({'message': f"{bdecoded}",'@timestamp': f"{datetime.datetime.now().isoformat()}" + "Z",'BadFormat': "True"}).encode('utf-8') + b'\n').decode('utf-8')
                result_record = {
                  'recordId': record['recordId'],
                  'result': 'Ok',
                  'data': data
                }
                result.append(result_record)
          except Exception as e:
            print(f"Failed to transform record: {e}")
            invalidLogs.append(bdecoded)
            pass

  if invalidLogs:
      print(f'Firehose data delivery stream: {firehoseStream}')
      print(f'Invalid logs that cannot be transformed: {invalidLogs}')

  return {'records': result}
