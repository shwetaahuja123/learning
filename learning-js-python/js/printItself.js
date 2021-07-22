const fs = require('fs')

fs.readFile('printItself.js', (err, data) => {
    if (err) throw err;

    console.log(data.toString());
})