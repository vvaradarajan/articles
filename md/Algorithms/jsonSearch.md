Recursive Search of Json

## Overview

When is the last time that you had to search a Json object for some node with a specific value for an attribute? I got into this because of this situation. The json tree was a file directory tree and the user was to select a file or a node in that tree. This was on the user-interface. However when the user selected a file, only the filename was obtained.  To locate the file, we need the complete path. This involves tracing the path to the file, from the top level.

## Design Analysis
Searching a json for a node with a specific value or an attribute can be done via recursion.  To keep track of the path taken as the recursion proceeds a path parameter is included in the recursion call. This is initially empty, but as the search proceeds by travelling down the tree, this nodes in the path of travel are appended to the path parameter.  If a node in the path satisfies the search attribute criteria, then both the node and the path parameter are returned. This return <path, node> is also returned by the ancestor recursive call, by checking if the node is not null (i.e. found).

If the node is not found on a particular path, the search continues recursively on the other paths.

## Implementation

### Weakness of design in implementation

On trying to implement this the straight forward, it was found that the keeping track of the parentArray along every search pass was too complex. The realization that the only time the parentArr matters is when the search is successful and this is the Eureka! moment. Therefore the trick of adding to the parentArr only if the search successful was implemented by passing the 'parent' to the recursive loop. That loop will then add the parent only if the result of the search is successful. 

### Weakness in implementation on use case

It turns out (!) that json objects often have arrays. So we have to figure out a way to search arrays. Luckily using the 'typeof' feature of Javascript, we can determine if an array is involved, and in that case use the index into the array as another parent associated with the array.

### Initial values for parent and parentArr
Initially there is no parent or parentArr, however these parameters must be passed. The parent is passed as 'null''(no parent), and the parentArr as an empty array.

The design is implemented in Javascript below:

```javascript
  function recurSearch(treeData,key,val,pP,parentArr) {
    //pP=potential parent (i.e. caller)
    //recursively look for key with val
    for (const k of Object.keys(treeData)) {
        if ((k==key) && (treeData[k]==val)) {
            return {'parentArr':parentArr, 'rslt':treeData}
        }
        pP=k
        if (typeof treeData[k] == 'object') {
                if (treeData[k] instanceof Array){
                    for (const [idx,e] of treeData[k].entries()) {
                        let retVal = recurSearch(e,key,val,k,parentArr)
                        //console.log(`retVal = ${retVal}`)
                        if (retVal != null) {
                            retVal.parentArr.unshift(idx)
                            retVal.parentArr.unshift(pP)
                            return retVal
                        }
                    }
                }
            else {
                //console.log(`K=${k}`)
                let retVal = recurSearch(treeData[k],key,val,pP,parentArr)
                if (retVal != null) {
                    retVal.parentArr.unshift(pP) //add parent only on successful search
                    return  retVal
                }
            }
        }
    }
    return null

}
```

## Testing

The test module written in javascript, dwarfs the implementation in terms of size. Here it is:

```javascript
import { recurSearch } from './util.mjs'  //import the recurSearch to be tested from an external file
treeData = {  //sample json tree to search 
    "categories": {
            "label": "Categories",
            "id": "1",
            "children": {
                "patient": {
                    "label": "Patients",
                    "id": "2",
                    "children": {
                        "patient:janeDoe": {
                            "label": "Jane Doe",
                            "icon": "Woman.png",
                            "id": "3",
                            "children": {
                                "jd:plans": {
                                    "label": "Plans",
                                    "id": "4",
                                    "children": {
                                        "plan:JDHI1": {
                                            "label": "Health Insurance JDHI1",
                                            "icon": "Plan.png",
                                            "id": "5"
                                        },
                                        "plan:JDDI1": {
                                            "label": "Dental Insurance JDDI1",
                                            "icon": "Plan.png",
                                            "id": "6"
                                        },
                                        "plan:JDVI1": {
                                            "label": "Vision Insurance JDVI1",
                                            "icon": "Plan.png",
                                            "id": "7"
                                        }
                                    },
                                    "babies":[
                                        {"email":"v@v.com"}
                                    ]
                                }
                            }
                        },
                        "person:briannen": {
                            "label": "Briannen Storm",
                            "icon": "Woman.png",
                            "id": "8",
                            "children": {
                                "bs:plans": {
                                    "label": "Plans",
                                    "id": "9",
                                    "children": {
                                        "plan:BSHI1": {
                                            "label": "Health Insurance BSHI1",
                                            "id": "10",
                                            "icon": "Plan.png"
                                        },
                                        "plan:BSDI1": {
                                            "label": "Dental Insurance BSDI1",
                                            "id": "11",
                                            "icon": "Plan.png"
                                        },
                                        "plan:BSVI1": {
                                            "label": "Vision Insurance BSVI1",
                                            "icon": "Plan.png",
                                            "id": "14"
                                        }
                                    }
                                }
                            }
                        },
                        "person": {
                            "label": "Thomas Key",
                            "icon": "Man.png",
                            "id": "15",
                            "children": {
                                "group:KTplans": {
                                    "label": "Plans",
                                    "id": "16",
                                    "children": {
                                        "plan:TKHI1": {
                                            "label": "Health Insurance HI2",
                                            "icon": "Plan.png",
                                            "id": "17"
                                        },
                                        "plan:TKDI1": {
                                            "label": "Dental Insurance DI2",
                                            "icon": "Plan.png",
                                            "id": "18"
                                        },
                                        "plan:TKVI1": {
                                            "label": "Vision Insurance VI2",
                                            "icon": "Plan.png",
                                            "id": "19"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        ,"id":"20"
    }

    let foundObj = recurSearchNew(treeData,"label","Briannen Storm",[])  //search for Briannen Storm
    if (!foundObj) console.log(`Not found: ${JSON.stringify(foundObj)} for ${i}`)
        else console.log(`Found: ${JSON.stringify(foundObj,undefined,indent=3)} for ${i}`)

```
### Test result:
In the test result below, we see that we can find the (key,value) pair ("label","Briannen Storm") by following the path in the parentArr:
categories => children => patient => children => "person:briannen"

Result Output:

```
Found: {
   "parentArr": [
      "categories",
      "children",
      "patient",
      "children",
      "person:briannen"
   ],
   "rslt": {
      "label": "Briannen Storm",
      "icon": "Woman.png",
      "id": "8",
      "children": {
         "bs:plans": {
            "label": "Plans",
            "id": "9",
            "children": {
               "plan:BSHI1": {
                  "label": "Health Insurance BSHI1",
                  "id": "10",
                  "icon": "Plan.png"
               },
               "plan:BSDI1": {
                  "label": "Dental Insurance BSDI1",
                  "id": "11",
                  "icon": "Plan.png"
               },
               "plan:BSVI1": {
                  "label": "Vision Insurance BSVI1",
                  "icon": "Plan.png",
                  "id": "14"
               }
            }
         }
      }
   }
}
```

The result is good!
Thank you for reading..