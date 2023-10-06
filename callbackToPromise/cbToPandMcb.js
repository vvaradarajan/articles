function getLinkedPromiseAndMcb(cb) {
    //get the promise to await and the modified cb that will
    //fulfill the promise
    //Glossary: r=resolve fcn, lp=linked promise, Mcb=modified callback
    let r=null //declared here so it non-local to functions in this scope
    let lp=new Promise((resolve,reject) => {
      r=resolve
    })
    let Mcb =(...args)=> {
      r(cb(...args))
    }
    return [lp,Mcb]
  
}

async function tester() {
    let cb=(rslt)=>{console.log(`Result = "${rslt}" received`)} //sample callback
    let [lp,Mcb] = getLinkedPromiseAndMcb(cb)
    //simulate an external process returning after 5000 ms
    let rt=5000
    setTimeout(()=>Mcb('callback Rslt'),rt) //simulates external process calling back cb with a result
    console.log("Awaiting callback")
    await lp
    console.log('done')
}

tester()
