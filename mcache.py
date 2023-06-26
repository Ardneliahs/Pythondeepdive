from pymemcache.client import base
import json
client = base.Client(('192.168.1.7', 11211))
personal_data = {
    'name': 'Prakash',
    'age': 34,
    'programming_languages': ['python', 'C#', 'java'],
    'address':{
        'flat_no': 177,
        'area': 'Velachery',
        'pincode': 600042
    }
}
client.set('prakask_personal_data', json.dumps(personal_data))
data = json.loads(client.get('prakask_personal_data').decode("utf-8"))
print(data['address']['area'])
