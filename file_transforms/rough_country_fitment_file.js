const fs = require('fs');
const lines = fs.readFileSync(process.argv[2])
  .toString('utf-8')
  .split('\n')
  .map(line => line.replace('\n', ''))
  .filter(line => line)
  .slice(1);

const hashCode = stringToHash => {
  var hash = 0, i, charElem;

  if (stringToHash.length == 0) {
      return hash;
  }

  for (i = 0; i < stringToHash.length; i++) {
      charElem = stringToHash.charCodeAt(i);
      hash = ((hash << 5) - hash) + charElem;
      hash = hash & hash; // Convert to 32bit integer
  }

  return hash;
}

const outFile = fs.createWriteStream(process.argv[3]);
outFile.write('Email,Year,Make,Model,Drive,Hash\n');

const modelMapper = {
  "4-Runner": "4Runner",
  "JK Wrangler": "Wrangler JK (2 Door)",
  "ZJ Grand Cherokee": "Grand Cherokee",
  "XJ Cherokee": "Cherokee XJ",
  "TJ Wrangler": "Wrangler TJ",
  "Wrangler JL": "Wrangler JL (2 Door)",
  "JK Wrangler Unlimited": "Wrangler JK Unlimited",
  "YJ Wrangler": "Wrangler YJ",
  "XK Commander": "Commander",
  "TJ Wrangler Unlimited": "Wrangler TJ Unlimited",
  "KJ Liberty": "Liberty",
  "Yukon XL": "Yukon XL 1500",
  "S-15": "S-15 Pickup",
  "MJ Comanche": "Comanche MJ",
  "Gladiator": "Gladiator JT"
};

const dodgeModelMapper = {
  "1500": "Ram 1500",
  "100" : "W100 Pickup",
  "200" : "W200 Pickup",
  "150" : "W150 Pickup",
  "350" : "W350 Pickup",
  "250" : "W250 Pickup"
};

for (let line of lines) {
  let parts = line.split(',');
  let year = parts[0];
  let drive = parts[3];
  let make = (parts[1] === "Chevy") ? "Chevrolet" : parts[1];
  let model;

  if (make === "Dodge") {
    model = dodgeModelMapper[parts[2]] || parts[2];
  } else {
    model = modelMapper[parts[2]] || parts[2];
  }

  let email = parts[4];

  let hash = hashCode([year, drive, make, model].join(''));

  outFile.write([email,year,make,model,drive,hash].join(','));
  outFile.write('\n');
}

outFile.end();
