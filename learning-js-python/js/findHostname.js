const lineReader = require('line-reader');
const Promise = require('bluebird')
const os = require("os");

const hostname = os.hostname();
console.log(hostname)

var arr = []
const readlines = async () => {
  var eachLine = Promise.promisify(lineReader.eachLine)
  await eachLine('../resources/known.hosts', function(line) {
      arr.push(line);
  })
  const p =  new Promise((resolve,reject)=> {
      resolve(arr)
  })
  return p;
}

const findHostname = async () => {
   const arr1 = await readlines()
   console.log('arr1: ',arr1)
   for (var hn of arr1) {
        if(hn === hostname){
            return true
        }
   }
   return false
}

const main = async() => {
    const ret = await findHostname()
    if(ret === true)
        console.log("Hostname found!")
    else
        console.log("Hostname NOT found!")
}

main()