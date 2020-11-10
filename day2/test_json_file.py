# Author:xqkang
# Date:2020/9/20 上午11:15
import json
ipTable = ['1.1.1.1', '18.9.14.13', '58.59.14.21']
fileObject = open('sampleList.txt', 'a')
for ip in ipTable:
    fileObject.write(ip)
    fileObject.write('\n')
fileObject.close()
'''
dictObj = {
    'andy':{
        'age': 23,
        'city': 'shanghai',
        'skill': 'python'
    },
    'william': {
        'age': 33,
        'city': 'hangzhou',
        'skill': 'js'
    }
}

jsObj = json.dumps(dictObj)
fileObject = open('jsonFile.json', 'a')
fileObject.write(jsObj)
fileObject.close()
'''