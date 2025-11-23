# All in One helpers

## Whatsapp Social Media link posting:
This uses OG headers:
1. Make the image 150x150 px  
2. Whenever the image etc is updated, cache is a big issue in testing:  
a. Post on your phone (that generally clears out the cache easily)  
b. On linux: clear browser cache, then delete:  
cd ~/.config/google-chrome/Default/IndexedDB  
rm -rf /https_web.whatsapp.com_0.indexeddb.*  
Login again into whatsapp, and then post the social media link.  

2. Debug using 'Sharing debuge' site from facebook. Each time you make a change, be sure o click on 'scrape again' - small text button
3. Use the Url to be the same as the website => Do the redirection in the body

Deleting Whatsapp cache from chrome: three dots=>settings=>privacy and security=>site settings => Third Party Cookies (under content)
=> 'see all site data and permissions' and search for Whatsapp..
## Lessons Learnt

## Lessons: 
Javascript/Typescript/snowpack:
0. Install the snowpack with the typescript extension and snowpack.config.js to use that extension for building  
If you get ./parse/lib not found etc, remove 'npm uninstall @snowpack/plugin-typescript' and cross-spawn and typescript and reinstall only npm uninstall @snowpack/plugin-typescript. That installs cross=spawn and typescript with proper libraries. The same goes for lib-toast. For some reason these may get installed without the lib's and suitable node_modules inside lit-toast   

1. Use TypeScript right away. Also create the tsconfig.json file (tsc --init) in each client directory.  

2. If you get errors like 'Cannot find module './lib/index.js' =>npm  uninstall snowpack and run again (it will use the global snowpack)  

3. Sometimes the client (eg: chess) wants its own 'img' to be served. However this request to img goes to 'spa/img' and not to 'spa/chess/img' which is what is needed.  The new design is to have this as an option.  

## Annoyances:  

### Yaml
1. In yaml if a string contains ': ' it becomes a variable. So use ';' without a space after, in a string

### chrome setting 'Navigate ..' has to be off , otherwise a blinking cursor pops up when clicking on a unicode piecelsnp  

### Javascript annoyances:  
Object.entries converts numbers into string  

### npm annoyances  
Issues in client build:  
snowpack may get installed locally and globally. Use the one that works. use 'npm uninstall snowpack' to remove the local version  
Sometimes the snowpack cache is corrupted. (Happens when 'npx snowpack dev' is done on server)  
Use: npx snowpack build --reload  

### tsc annoyances  
The outDir option in tsconfig does not see to work, so js files get mixed with ts  

### CSS annoyances:  
grid-start-col (or row) always starts at 1 (not 0)  
css is a beast => custom-element styling from outside is :host does not work with :host(**). Unique solutions exist everywere (ex: custom property styling via javascript instead of class)  

### vscode annoyances:  
opens wrong file with same name, due to history. Do 'clear editor history'  

### Certificate expiration
If browser says that site is not secure and crosses out the 'https' it means that the SSL certificate has expired. Use an online tool 'trackssl' (https://app.trackssl.com/..) and it will show the reason. Since we use letsencrypt, issue the command on the server 'sudo certbot renew' and it should renew. You may have to stop nginx to free up port 80

### Social Media posting annoyances:
Generally og headers are painful, and use the 'sharing debugger from Meta' to debug these ('https://developers.facebook.com/tools/debug/)

# Steps to Add an app to the 'articles' framework
The articles framework allows you to create a webcomponent App. The webcomponent App javascript/typescript is in the client.

client:
ex: appNm='socialMedia'
1. Create a folder with the $name in the articleWeb/client and put the Lit components for this app into cComponents.js (or you could have the import statements in cComponents.js to import the components). These are dynamically imported (all in tree.js). The dynamic import occurs when document is clicked on the tree, which makes a request getDocHtml (to server). Server reads the {appNm}.md file and returns The a json of html and cComponents, and the cComponents is dynamically imported and then the html is rendered using the lit-element render.
2. Have all the import statements for the app's <comp>.js in cComponents.js

Server:
1. create $appNm.py (copy chess.py) and add a route/routes for $name. Also change the classname inside it.
In main.py
2. Add 'from ${appNm} import ${className - the $name with caps in first char usually}
3. Instantiate an instance of the class near the end of main.py
(ex: formGet=FormGen(app,G))

articles:
1. Create the file ${appNm}.md and indicate that has the following sections (templated here):
!application: {appNm}
# Desc: like 'form Generator application (generates form  from yaml file)!'
# Section components to be imported in client (relativge to the client folder)
!componentJs: ./{appNm}/cComponents.js 
# section that defines variables to substitute into the html
!def_{key}: {value}
!def_{key}: {value}
..
# section that goes into the initial html page (using the components defined in the previous line)
# The {attribs} here are left over (i.e. did not have substutions) def_detail variablespassed as key=value
<menu-element>
<form-gen serverUrlPrefix="${serverUrlPrefix}/retirement" ${attribs}></form-gen>
</menu-element>

# blah ..blah!

Notes: Don't forget to 'npx snowpack build' in the client folder

# main.py (common to all applications):
## Intro:
This is the main app invoked by this framework:
1. It creates the starlette webserver app, a global object G and passes it on to all the applications. Each application has an {appNm}.py which contains the app as a class, that receives the app and G parameters from main.py
2. The {appNm}.py then adds routes (prefidex by appNm) and handles these routes. These routes are used by the client (browser: javascript/typescript application) see Server section.
2. It generates the 'docTree' that has the folder structure of all the applications/articles when the website is invoked. It handles routes related to docTree. If the route includes a 'path' parameter: ex "path=Finance,3Bucket.md", this is CSV seperated down the docTree with the last part being a document name with md extension. That document could be simply a markdown file or a special markdown file identifying an application (see articles section):
a. If a simple markdown file, it is displayed as an html page.
b. If it is an application, the application is invoked by including the application component html (see articles section) in the application framework html page. This framework html page is just a header with a back button to return to previous page.

3. In main.py import the {appNm.py} at the top of the file, and create the appNM object at the bottom. 
# app specific configs:
If any app specific configs are required, they can be placed in server/configs/config.yml. These will be in G that is passed to that specific app.

Miscellaneous:
1. To find some python function somewhere:
find . -name **.py -exec grep -H 'pnp(' {} \; #finds all python files with 'pnp('
