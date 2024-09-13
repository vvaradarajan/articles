# Learn to  Build a DIY Web App
<img src="img/diyWeb.jpeg" /> 

Gone are the days where every IT guy/girl/person had a specific job like QA, developer, architect etc. Good riddance, since we all are creative and want to have fun and indulge in more than we can handle! Welcome to the "full-stack" developer, whom, once you hire, you hold them responsible and heave a sigh of relief..


This article addresses a specific way of developing a web application and should be of interest to the 'full-stack' developer.


In today's normal design, a web application follows the same paradigm as client-server application. The client handles the 'front-end' user interactions and is mostly concerned with the user interface. The server is the 'back-end' and services requests from the front-end. One challenge here is how to coordinate the development of both so that they work with each other, and manage the complexities.


Such complexities include different languages for server(python)/client (javascript), configuration files that are interdependent, settings of middle-ware such as nginix, handling the git repositories for both and more. As a lone-wolf full-stack developer having to do everything, we need some cogent method.

## What if we do this?
Have a single repository with the server and client code in separate folders. This allows the developer to be able to view the client code/logic while working on the server code and vice-versa. This reduces the complexity of interfacing the client and server, reduces bugs and makes it easy to test. It also has advantages in deployment. Very often the web application has a small audience and efforts at scaling are not necessary. Hosting both the server and client in one physical server makes deployment easy. 'Version' mismatch between client and server is either elminated or minimized with the code for both client and server being in the same repo.


Have the server, serve the client at a user request from the browser. The server will also serve client requests. This way the server can control the configuration of the client. Further it opens up an opportunity of centralizing client control, such as limiting the number of clients gracefully, keeping track of resources assigment/usage by each client etc. It also reduces the number of 'ports' exposed for internet connections.


### Design concepts
The server runs on the backend, and serves ONE request directly from the user, which is the invoking of the application from the browser. The response by the server is to serve the client application to the user, which is a SPA (single page application almost always a Javascript application). The client which runs in the browser, then handles all user interactions and calls the server as necessary to satisfy user requests. The are many components in here - the server, the client, middleware (nginix) and each can be elaborate. Here we concentrate on the glue that binds these together. This glue is the configuration file.


### This is diagrammed below:
<img src="img/diyWeb2.jpeg" /> 

### The details of the config which is the core item in this architecture are:

| Config Item | Description |
| ----------- | ----------- |
|  port | This is port that the webapp runs on. User requests from the browser are routed to this port by nginx |
| url | This is the url that nginx routes to the webapp running on port |
| serverUrlPrefix |This url prefix is used by the client to make requests to the server. (Note: The client runs on the user's browser) |
| ClientResourcePrefix | This prefix is used to send requests to the server to access resources in the client folder. These are the static resources (images, javascript) of the client |
| client loc | Location of the client folder. The server serves the index.html from this location, as well the client's static resources |

### Logical:
a. The server is a normal back end server and has its own set of routes PLUS one route that serves the client.

b. The client is a separate folder in the repo named 'client'. It is a javascript single page App.


The application initiation and interactions are depicted in the flow diagram below. The numbers in the text show the sequence of events: 

<img src="img/diyWeb3.jpeg" />

### Implementation
An example app that follows this <modes is described below. For that demp app, the above logical design is implemented as:


- Server is implemented Using a python Sanic webserver
- Client is a Javascript Single Page App using lit-elements.
### Folder Structure:
- <b>Server folder:</b> This folder contains the server code. Here it is written in Python and uses the Sanic webserver.


- <b>Client folder:</b> This folder contains the client code that runs on the browser. Here it is a Javascript SPA (single page application) and uses the popular web-component framework Lit-element. The folder client/build is the output of ‘building’ the client app and is the actual folder where the final client code resides.


- <b>Main Folder:</b> contains the Server and Client folders. This folder can be considered as the git repository.


### Example:
<b>Application:</b> Fill up a form Client Javascript application: Display the form, collect data and send to server Server Python/Sanic Application: Receive form data Nginix App: Route user/client requests/responses


<b>Two Screen shots: 1. The form, 2. The server response are:</b> 

<img src="img/diyWeb6.jpeg" />

1. User filling form

After user clicks 'SaveMyForm':

<img src="img/diyWeb7.jpeg" />

The first screenshot is from the client and shows the form. The ‘SaveMyForm’ button causes the client to invoke the server with an api using the ‘serverUrlPrefix’. The second screenshot shows the response: a picture (a client resource) with a message from the Server at the bottom.


### Steps to implement the example:

Create the config file:
Develop the client: a. Index.html with placeholder for the config client related parameters b. The form page component (use lit element for convenience)
Develop the server: a. Read config file and use it to modify client index.html b. Have a route to serve the client (with modified index.html of step a) c, Have a route to receive the form data

The relevant code (config.yml, nginx, server app, client-index.html, form.js). Of these the config.yml contains the core part of this article. It is read, used and distributed to the client by the server app. In the example, the server app distributes the config to the client, by modifying the index.html. The entries in the config file are also distributed to the nginx config file via 'hardcoding'.


<b>The entries in the config file for this example are:</b>


| Config Item | value | Description |
| ----------- | ----- | ----------- |
| port| 8002 | This is port that the backed server of the webapp runs on. This port value and the url below are used in the nginx config file for routing. |
| url | localhost/diy | This is the url that nginx routes to the webapp running on port. The user enters this url in the browser to access the application |
| serverUrlPrefix | localhost/diy | This url prefix is used by the client to make requests to the server. Note: The client runs on the user's browser. Any request with this prefix is routed to the server app. |
| ClientResourcePrefix | spa | This prefix is used to send requests to the server to access resources in the client folder(see Client loc below). These are the static resources (images, javascript) of the client. The server uses the clientLoc (see below) to serve these requests. |
| clientLoc | client/build | Location of the client folder. The server serves the index.html from this location, as well as other client's resources |



The other related code is listed below. Hopefully these are self explanatory given some familiarity with the language/tools used.


<b>Config file:</b> This is a yaml file containing the items described above:

```
port: 8002  
url: 'localhost/diy'
serverUrlPrefix: 'localhost/diy'
clientResourcePrefix: 'spa'
clientLoc: 'client/build'
```
<b>Nginx config file:</b> (note the values from the config file are hardcoded here)
```
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri $uri/ =404;
        }
    set $diyPort 8002;
    location ~ /diy/(.*) {
        #pass the query params also!
        proxy_pass  http://0.0.0.0:$diyPort/$1$is_args$args;
    }
    location /diy {
       return 302 /diy/;
    }
}
```

<b>Server code:</b> This python module serves the client application at the ‘/’ route. It also services the client request ‘saveform’ (see the Application Flow diagram earlier in this article):

```python
from sanic import Sanic, response
import json
import yaml

import os
installDir = os.path.dirname(os.path.realpath(__file__))

app = Sanic(name='DiyArticle')
#read config file
def getConfig():
    configFileNm = f'{installDir}/config.yml'
    with open(configFileNm, "r") as f:
        G = yaml.safe_load(f.read())
    print(f'[global]ConfigFileName: {configFileNm}\nConfig:\n{json.dumps(G,indent=4)}')
    return G

G=getConfig()

clientDir = f'{installDir}/../{G["clientLoc"]}'
baseUrl = f'{G["clientResourcePrefix"]}'
#clientDir = '/home/vv/git/ASrvrClntIn1/client/deploy'

app.static(f'/{G["clientResourcePrefix"]}', clientDir)


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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=G['port'])
```

<b>Client code:</b> index.html (note the ‘${..}’ templated entries that are filled from the config file). This is the SPA (single page javascript app) and uses the custom component ‘diy-form’

```html
<!DOCTYPE html>
<html>
<head>
    <base href="${baseUrl}/" target="_blank">
    <script type="module" src="form.js"></script> 
</head>
<body>
    <div>
        <diy-form server-url-prefix="${serverUrlPrefix}""></diy-form>
    </div>
</body>
</html>
```
<b>Client code:</b> diy-form - The custom component written using the Lit element framework. This is the form.js file. Refer to the Lit element documentation for elaborate details.

```js
import {LitElement, html,css } from 'lit';
import {repeat} from 'lit/directives/repeat.js';

async function postDataToUrl(url = "", data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: "POST", // *GET, POST, PUT, DELETE, etc.
    mode: "cors", // no-cors, *cors, same-origin
    cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
    credentials: "same-origin", // include, *same-origin, omit
    headers: {
      "Content-Type": "application/json",
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: "follow", // manual, *follow, error
    referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data), // body data type must match "Content-Type" header
  });
  if (response.status != 200) {
    return `Status: ${response.status} : ${response.statusText}`
  }
  return await response.text()
}

class FormElement extends LitElement {
  static styles = css`
    input.invalid {
      border: 1px solid red;
    }
  `;

  constructor() {
      super();
      this.saveDataUrlSuffix='saveform'
      this.state='open'
      this.serverUrlPrefix = this.getAttribute('server-url-prefix')
  }

  async receiveConfigInfo(config,parentObj) {
    console.log(`Config info received in brRegForm: ${JSON.stringify(config)}`)
    this.parent=parentObj
    this.config = config

  }


  getFormData(myForm) {
    let result = (new FormData(this.form)).entries()
    let fd={}
    for (const element of result) {
      console.log(element);
      if (fd.hasOwnProperty(element[0])) 
        fd[element[0]].push(element[1])
      else fd[element[0]]=[element[1]]
    }
    //include value='' for radio buttons which were left blank
    let rbs=myForm.querySelectorAll('[type="radio"]')
    for (const element of rbs) {
      if (fd.hasOwnProperty(element.name)) continue;
      else fd[element.name]=['']
    }
    return fd
  }

  validateFormData(fd) {
    return ''
  }

  async submit(e) { 
    console.log('Form data')
    this.form = this.shadowRoot.querySelector('form')
    let fd = this.getFormData(this.form)
    console.log(fd)
    let errMsg = this.validateFormData(fd)
    if (errMsg) {
      let elmt = this.shadowRoot.querySelector("errMsg")
      elmt.innerText=errMsg
      elmt.style.display='block'
    } else {
      // await this.parent.setChart(fd);
      //this.parent.closeApp()
      let urlToPost=`http://${this.serverUrlPrefix}/${this.saveDataUrlSuffix}`
      console.log(`Form data submitted to ${urlToPost}`)
      this.serverMsgresp = await postDataToUrl(urlToPost,fd)
      if (this.serverMsgresp.includes('saved')) this.state='submitted'

    }
    this.requestUpdate()
  }


  render() {
    if (this.state=='submitted')
    return html`<img src="img/HalloweenThumbsUp.avif" /><br/>
      <span style="font-size: 200%;color: blue;">${this.serverMsgresp}</span>`
    return html`
      <form onsubmit="return false;">
      <div width="80%">
      <div>
      <h1>Form to be filled and submitted to Server</h1>

      Please fill out the following details and click on the 'I agree' button. <br/><br/>
      <b>Choose Like-NotSure: </b>
      <div id="session" class="flex-container">
        <label>
        <input type="radio" id="session1" name="session" value="session1">
        I like this article..
        </label>
        &nbsp;&nbsp;
        <label>
        <input type="radio" id="session2" name="session" value="session2">
        Not exactly sure..
        </label>
      </div>
      <br/>
      <b>contact detail:</b>
      <div class="flex-container">
        <label>Name in full: <input  id="Name" name="Name" style="width: 15em;"/></label>
        <label>Email: <input  id="Email"  name="Email" style="width: 15em;"/></label>
        <label>Phone #: <input  id="Phone" name="Phone" style="width: 10em;"/></label>
      </div>
      <b>Familiarity with both Python and javascript web components:</b>
      <div id="pranayama" class="flex-container">
      <label><input type="radio" name="pranayama" value="None">Not at all</label>
      &nbsp;&nbsp;
      <label><input type="radio" name="pranayama" value="somewhat">Somewhat (occasionaly develop in these)</label>  &nbsp;&nbsp;
      <label><input type="radio" name="pranayama" value="expert">Expert (regular and frequent practioner)</label> 
    </div>
    <br/>

    </div>
    </form>
    <errMsg id="errMsg" style="background-color:red; display=None;"></errMsg>

    <button id="save" style="background-color:lightgreen;" @click="${this.submit}">SaveMyForm</button>
    `
  }
}
customElements.define('diy-form', FormElement);

```

Apologies for a long article, but I am sure that the effort in the reading will be rewarded!

