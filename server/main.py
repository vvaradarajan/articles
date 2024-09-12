from sanic import Sanic, response
import markdown
import json
import yaml

import os
installDir = os.path.dirname(os.path.realpath(__file__))

app = Sanic(name='DiyArticle')
#read config file
def getConfig():
    configFileNm = f'{installDir}/etc/config.yml'
    with open(configFileNm, "r") as f:
        G = yaml.safe_load(f.read())
    print(f'[global]ConfigFileName: {configFileNm}\nConfig:\n{json.dumps(G,indent=4)}')
    return G

G=getConfig()

clientDir = f'{installDir}/../{G["clientLoc"]}'
baseUrl = f'{G["clientResourcePrefix"]}'
#clientDir = '/home/vv/git/ASrvrClntIn1/client/deploy'
print(f'Vasan: clientDir={clientDir}')

app.static(f'/{G["clientResourcePrefix"]}', clientDir)
#app.static('/img',f'{installDir}/../img')
print(f'imgDir = {installDir}/../img')


@app.route("/saveform",methods=['POST'])
async def test(request):
    return response.text("Your Form is saved on the Server!")

@app.route("/")
async def clientSPA(request):
    with open(f'{clientDir}/index.html','r') as f:
        indexHtml = f.read()
    #modify and insert the baseUrl and the serverUrlPrefix (to call server api from client)
    indexHtml = indexHtml.replace('${baseUrl}',baseUrl)
    indexHtml = indexHtml.replace('${serverUrlPrefix}',G["serverUrlPrefix"])
    print(f'Vasan:\n{indexHtml}')

    return response.html(indexHtml)

@app.route("/twinPrimes")
async def twinPrimes(request):
    with open(f'{installDir}/../twinPrimes/writeup.md', "r", encoding="utf-8") as input_file:
        text = input_file.read()
        html = markdown.markdown(text, extensions=['fenced_code', 'codehilite'])
    return response.html(html)

@app.route("/article/<artMdNm>")
async def showArticle(request,artMdNm):
    style=('<style type="text/css" rel="stylesheet">' +
           'table, th, td {border: 1px solid;}' +
            '</style>')
    with open(f'{installDir}/../md/{artMdNm}.md','r') as f:
        md =style+ f.read()
    html= markdown.markdown(md,extensions=['tables'])
    return response.html(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=G['port'])