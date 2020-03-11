const fs = require('fs');
let namespaces = ["aerosoles", "moma", "mr_bigandtall", "tiptop_tailors", "acer", "payless", "staples_ca", "staples_ca_fr", "cavenders", "evacuumstore", "experticity", "peony", "primary", "tree_classics", "blindster", "omaha_steaks", "1stdibs_uk", "gilt_city", "yamibuy", "zwilling_us", "catbird", "g_by_guess", "guess", "guess_ca", "guess_factory", "guess_factory_ca", "kanes_furniture", "kat_von_d", "beekman_1802", "bestbuy_ca", "camping_world", "enchroma", "tigerdirect_ca", "haute_rogue", "marciano", "marciano_ca", "mercury_media", "truefacet", "bandier", "kuru", "lhasa_oms", "thinkgeek", "emsstore_witmer", "firestore_witmer", "mountain_hardwear_ca", "mountain_hardwear_us", "officerstore_witmer", "snobswap", "toolbarn"];

for (let n of namespaces) {
  let manifestPath = `/src/integrations/compiled/${n}.js`;
  fs.writeFileSync(manifestPath, '{}');

  let template = `/src/integration/src/templates/template.integration.js`;
  let integrationPath = `/src/integrations/src/${n}_integration`
}
