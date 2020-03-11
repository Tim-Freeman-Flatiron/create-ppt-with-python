const fs = require('fs');
const os = require('os')

const basePath = `${os.homedir()}/Downloads/sql`;
let files = fs.readdirSync(basePath).map(file => `${basePath}/${file}`);

// files = files.slice(0,1);

const outFile = fs.createWriteStream('./namespaces_with_audience_customer_attributes.csv');
outFile.write('namespace,attributes_used\n');
const mapper = {};

for (let f of files) {
  let namespace = f.match(/sql\/(.+)\.txt/)[1];
  mapper[namespace] = new Set();
  let lines = fs.readFileSync(f).toString('utf-8').split('\n');

  for (let l of lines) {
    if (l.includes('== True')) {
      let truth = (l.match(/\s([A-Za-z0-9_]+)\s==\sTrue/) || [null,null])[1];
      truth && truth !== 'continuous_delivery' && mapper[namespace].add(truth);
    }
  }

  if (mapper[namespace].size > 0) {
    outFile.write(`${namespace},"${Array.from(mapper[namespace]).join(',')}"\n`);
  } else {
    console.log(namespace);
  }
}

outFile.end();
