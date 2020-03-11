const fs = require('fs');
const lines = fs.readFileSync(process.argv[2])
  .toString('utf-8')
  .split('\n')
  .map(line => line.replace('\n', ''))
  .filter(line => line)
  // .slice(1);

const outFile = fs.createWriteStream(process.argv[3]);
outFile.write('country,languages\n');

let mapper = {};

for (let i = 0; i < lines.length; i++) {
  try {

    if (i !== 0) {
      let parts = lines[i].split('|');
      let country = parts[4];
      let language = parts[5];

      if (mapper[country]) {
        if (!mapper[country].includes(language)) {
            mapper[country].push(language);
        }
      } else {
        mapper[country] = [language];
      }
    }

  } catch(e) {
    console.log(e);
  }
}

let entries = Object.entries(mapper);

for (let k of entries) {
  outFile.write(`${k[0]},${k[1].join('|')}\n`);
}

outFile.end();
