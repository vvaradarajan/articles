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

## Lessons Learnt

Lessons:  
0. Install the snowpack with the typescript extension and snowpack.config.js to use that extension for building  
If you get ./parse/lib not found etc, remove 'npm uninstall @snowpack/plugin-typescript' and cross-spawn and typescript and reinstall only npm uninstall @snowpack/plugin-typescript. That installs cross=spawn and typescript with proper libraries. The same goes for lib-toast. For some reason these may get installed without the lib's and suitable node_modules inside lit-toast   

1. Use TypeScript right away. Also create the tsconfig.json file (tsc --init) in each client directory.  

2. If you get errors like 'Cannot find module './lib/index.js' =>npm  uninstall snowpack and run again (it will use the global snowpack)  

3. Sometimes the client (eg: chess) wants its own 'img' to be served. However this request to img goes to 'spa/img' and not to 'spa/chess/img' which is what is needed.  The new design is to have this as an option.  

## Annoyances:  
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

# Steps to Add an app to the 'articles' framework
The articles framework allows you to create a webcomponent App. The webcomponent App javascript/typescript is in the client.

client:
ex: name='socialMedia'
1. Create a folder with the $name and put the files cComponents.js, component.html,form.js (or a specific component/s for this app) and an index.html
2. Modify all these files to suit.
3. In tree.js add the import of 'import './${name}/cComponents.js'

Server:
1. create $name.py (copy chess.py) and add a route/routes for $name

Notes: Don't forget to 'npx snowpack build' in the client folder
