const fs = require('fs');
let namespaces = ["nike", "nike_australia", "nike_austria", "nike_austria_german", "nike_belgium", "nike_belgium_dutch", "nike_belgium_french", "nike_belgium_german", "nike_brazil", "nike_bulgaria", "nike_canada", "nike_canada_french", "nike_chile", "nike_croatia", "nike_czech_republic", "nike_czech_republic_czech", "nike_denmark", "nike_denmark_danish", "nike_egypt", "nike_finland", "nike_france", "nike_germany", "nike_great_britain", "nike_greece", "nike_hungary", "nike_hungary_hungarian", "nike_india", "nike_indonesia", "nike_ireland", "nike_israel", "nike_italy", "nike_japan", "nike_luxembourg", "nike_luxembourg_french", "nike_luxembourg_german", "nike_malaysia", "nike_mexico", "nike_morocco", "nike_morocco_french", "nike_netherlands", "nike_netherlands_dutch", "nike_new_zealand", "nike_norway", "nike_norway_norwegian", "nike_philippines", "nike_poland", "nike_portugal", "nike_portugal_portuguese", "nike_puerto_rico", "nike_romania", "nike_russia", "nike_saudi_arabia", "nike_singapore", "nike_slovakia", "nike_slovenia", "nike_south_africa", "nike_spain", "nike_sweden", "nike_sweden_swedish", "nike_switzerland", "nike_switzerland_french", "nike_switzerland_german", "nike_switzerland_italian", "nike_taiwan", "nike_thailand", "nike_turkey", "nike_uae", "nike_vietnam"];
for (let n of namespaces) {
  let manifestPath = `/src/integrations/manifests/${n}.build.manifest`;
  let newManifest = fs.readFileSync(manifestPath).toString('utf-8')
    .replace("if (!window.hasOwnProperty('__tmClass')) {", "")
    .replace("}", "")
    .replace(/    \$INCLUDE/g, "$INCLUDE")
    // .replace(/\$INCLUDE triggermail_core\.js|\$INCLUDE triggermail_core\.modhash\.js|\$INCLUDE common\/vanillajs\/triggermail_core\.js|\$INCLUDE common\/vanillajs\/triggermail_core\.modhash\.js/, '$INCLUDE common/vanillajs/triggermail_core_localStorage\.js')
    // .replace('$INCLUDE initializer.js', '$INCLUDE common/vanillajs/initializer.js')
    // .replace('$INCLUDE mixpanel.js', '$INCLUDE common/vanillajs/mixpanel.js')
    // .replace(/\s*\$INCLUDE prettyprint\.js\$\s*/, '\n');

  try {
    fs.writeFileSync(manifestPath, newManifest);
    console.log(n, '- success');
  } catch(e) {
    console.log('NOPE');
  }
}

// "acklands_grainger" "caratlane" "cdwg" "century21" "dealnews" "evo" "northern_tool" "planet_blue" "planet_shoes" "reallygoodstuff" "reef" "amsoil" "amsoil_ca" "g_by_guess" "gg_alzheimers" "gg_diabetes" "gg_hopefaithlove" "gg_theanimalrescuesite" "gg_theautismsite" "gg_thebreastcancersite" "gg_thehungersite" "gg_theliteracysite" "gg_therainforestsite" "gg_theveteranssite" "guess" "guess_ca" "guess_factory" "guess_factory_ca" "ice" "king_power" "lens_direct" "marciano" "marciano_ca" "minnetonka" "smartpak" "ssww" "vineyard_vines" "zozi" "express" "ashton_drake" "atlantic_superstore" "bby" "beekman_1802" "bradford_exchange" "bradford_exchange_ca" "bradford_exchange_checks" "brooks_sports" "brooks_sports_de" "brooks_sports_uk" "champssports" "clothing_shop_online" "diesel" "dominion" "dr_martens" "eagle_creek" "eastbay" "ecopurehome" "ecowater" "eight_watch" "footaction" "footlocker" "footlocker_ca" "fortinos" "fsa_store" "ftf_nyc" "gnc" "hamilton_collection" "happyxnature" "haute_rogue" "hay_us" "his_room" "her_room" "hsa_store" "icm" "jtv" "katespade_jp" "kids_footlocker" "lady_footlocker"

// "cdw" "cdw1" "grassland_beef" "oriental_trading" "tjmaxx"


// "nike", "nike_australia", "nike_austria", "nike_austria_german", "nike_belgium", "nike_belgium_dutch", "nike_belgium_french", "nike_belgium_german", "nike_brazil", "nike_bulgaria", "nike_canada", "nike_canada_french", "nike_chile", "nike_croatia", "nike_czech_republic", "nike_czech_republic_czech", "nike_denmark", "nike_denmark_danish", "nike_egypt", "nike_finland", "nike_france", "nike_germany", "nike_great_britain", "nike_greece", "nike_hungary", "nike_hungary_hungarian", "nike_india", "nike_indonesia", "nike_ireland", "nike_israel", "nike_italy", "nike_japan", "nike_luxembourg", "nike_luxembourg_french", "nike_luxembourg_german", "nike_malaysia", "nike_mexico", "nike_morocco", "nike_morocco_french", "nike_netherlands", "nike_netherlands_dutch", "nike_new_zealand", "nike_norway", "nike_norway_norwegian", "nike_philippines", "nike_poland", "nike_portugal", "nike_portugal_portuguese", "nike_puerto_rico", "nike_romania", "nike_russia", "nike_saudi_arabia", "nike_singapore", "nike_slovakia", "nike_slovenia", "nike_south_africa", "nike_spain", "nike_sweden", "nike_sweden_swedish", "nike_switzerland", "nike_switzerland_french", "nike_switzerland_german", "nike_switzerland_italian", "nike_taiwan", "nike_thailand", "nike_turkey", "nike_uae", "nike_vietnam"
