const fs = require('fs');
// let partners = ["acklands_grainger", "caratlane", "cdwg", "century21", "dealnews", "evo", "northern_tool", "planet_blue", "planet_shoes", "reallygoodstuff", "reef", "amsoil", "amsoil_ca", "g_by_guess", "gg_alzheimers", "gg_diabetes", "gg_hopefaithlove", "gg_theanimalrescuesite", "gg_theautismsite", "gg_thebreastcancersite", "gg_thehungersite", "gg_theliteracysite", "gg_therainforestsite", "gg_theveteranssite", "guess", "guess_ca", "guess_factory", "guess_factory_ca", "ice", "king_power", "lens_direct", "marciano", "marciano_ca", "minnetonka", "smartpak", "ssww", "vineyard_vines", "zozi", "express", "ashton_drake", "atlantic_superstore", "bby", "beekman_1802", "bradford_exchange", "bradford_exchange_ca", "bradford_exchange_checks", "brooks_sports", "brooks_sports_de", "brooks_sports_uk", "champssports", "clothing_shop_online", "diesel", "dominion", "dr_martens", "eagle_creek", "eastbay", "ecopurehome", "ecowater", "eight_watch", "footaction", "footlocker", "footlocker_ca", "fortinos", "fsa_store", "ftf_nyc", "gnc", "hamilton_collection", "happyxnature", "haute_rogue", "hay_us", "his_room", "her_room", "hsa_store", "icm", "jtv", "katespade_jp", "kids_footlocker", "lady_footlocker", "lhasa_oms", "mmo_golf", "modcloth", "mountain_hardware_us", "mountain_hardwear_ca", "mountain_hardwear_us", "neutrogena", "nofrills", "pacsafe", "paulas_choice_au", "pcm_us", "provigo", "quest_nutrition", "real_canadian_superstore", "reed_and_barton", "smtw", "sorel_at", "sorel_be", "sorel_ca", "sorel_de", "sorel_es", "sorel_fi", "sorel_fr", "sorel_ie", "sorel_it", "sorel_nl", "sorel_uk", "sorel_us", "sorrel_us", "specialized", "sports_collectibles", "tequipment", "touchboards", "uncommonsense", "valumart", "yandy", "yig", "zehrs", "_semantic", "1000Bulbs", "1stdibs_uk", "24_sevres", "500_level", "511tactical", "abt", "acer", "ada", "adorama", "aerosoles", "airgas", "anthropologie", "audio_advice", "autoanything", "bassett_furniture", "bates", "beauty_boutique", "bentley_leathers", "bestbuy_ca", "bestseller_ca", "betsey_johnson", "beyond_the_rack", "bgz_brands", "blauer", "bliss", "blue_nile", "blue_nile_au", "blue_nile_ca", "blue_nile_uk", "brilliance", "cabelas_ca", "callaway_apparel", "camping_world", "carls_golfland", "catbird", "catherines", "catsfootwear", "cavenders", "cesco", "chacos", "coach_ca", "coach_de", "coach_es", "coach_fr", "coach_it", "coach_jp", "coach_outlet_jp", "coach_uk", "cole_haan", "connecting_threads", "converse_be", "converse_de", "converse_de_german", "converse_es", "converse_es_spanish", "converse_fr", "converse_fr_french", "converse_it", "converse_it_italian", "converse_nl", "converse_nl_dutch", "converse_uk", "cpo_outlets", "crown_and_caliber", "cubavera", "cvs", "daily_sale", "davids_bridal", "demandware_cert_test", "dior", "disney", "dvf", "edible_arrangements", "electronic_express", "emsstore_witmer", "enchroma", "EQ3", "experticity", "farah_uk", "firestore_witmer", "footjoy", "fossil_de", "fossil_fr", "fossil_it", "fossil_uk", "fossil_us", "george_richards", "glasses", "grasshoppers", "groupe_dynamite", "hammacher", "hanna_andersson", "harley_davidson_footwear", "herman_miller", "hibbett_sports", "horze", "horze_us", "hushpuppies", "indigo_books", "invicta", "james_avery", "jansport", "jcpenney", "jenson", "jeromes", "jockey", "jockey_ca", "joe_fresh", "kanes_furniture", "kat_von_d", "keds", "kipling", "knit_picks", "kotulas", "kuru", "la_z_boy", "lamps_plus", "lamps_plus_open_box", "lane_bryant", "lee", "loblaws_cc", "lowes_ca", "mac_mall", "masseys", "mavi_ca", "mavi_us", "mercury_media", "merrell", "midwest_supplies", "modloft", "mom365", "moma", "monicaandandy", "mr_bigandtall", "my_bobs", "myparkingsign", "nautica", "nba_store", "neiman_marcus", "newegg", "newegg_business", "newegg_ca", "nrhl", "nyandco", "online_shoes", "original_penguin", "original_penguin_uk", "outerknown", "pact", "paul_fredrick", "paulas_choice", "peony", "perfumania", "perry_ellis", "petcarerx", "pura_vida", "rcwilley", "rebecca_minkoff", "rei_us", "reno_depot", "road_runner_sports", "rockport", "rona_ca", "saucony", "servermonkey", "shoebuy", "sigma_beauty", "skagen", "skagen_germany", "skagen_uk", "smartwool", "snobswap", "speedo", "sperry", "staples_ca_fr_pcam", "staples_ca_pcam", "steve_madden", "steve_madden_ca", "strapworks", "striderite", "stuart_weitzman", "tail_activewear", "talbots", "techni_tool", "terez", "test_demandware_partner", "test_magento_2", "the_limited", "tigerdirect", "tigerdirect_ca", "timberland", "timbuk2", "timex", "timex_uk", "tiptop_tailors", "tommy_hilfiger", "toolbarn", "tous", "tree_classics", "truefacet", "tyler_tool", "vans", "vans_ca", "vermont_country_store", "vibram", "victorinox", "victorinox_uk", "vital_choice", "volcom", "volcom_ca", "we", "wineexpress", "wolverine", "wrangler", "yamibuy", "zwilling_us", "ariat", "1stdibs", "bandier", "cabelas", "gopro", "grand_and_toy", "james_allen", "living_spaces", "pamperedchef", "prana", "uspatriot", "world_market", "stuart_weitzman_eu", "columbia_at", "columbia_be", "columbia_ca", "columbia_de", "columbia_es", "columbia_fi", "columbia_fr", "columbia_ie", "columbia_it", "columbia_nl", "columbia_uk", "columbia_us", "david_yurman_ca", "david_yurman_fr", "heritage_brands", "motosport", "rough_country", "ashley", "bcb_generation", "bcbg_inc", "beautycounter", "belk", "chanel_usa", "coach", "coach_outlet", "company_store", "crocs", "crocs_au", "crocs_ca", "crocs_de", "crocs_fr", "crocs_jp", "crocs_uk", "david_yurman", "dermstore", "dollar_tree", "famsa", "fragrancex", "gamestop", "gapinc", "gapinc_ca", "gapinc_eu", "gapinc_jp", "gapinc_uk", "gilt_city", "hayneedle", "hopsy", "invaluable", "lilly_pulitzer", "magazine_store", "mydeal", "officerstore_witmer", "omaha_steaks", "oriental_trading", "parker", "pendleton", "perfume", "princess_auto", "rebecca_taylor", "reebok", "saatchi_art", "sephora", "shoes_for_crews", "sierra_trading_post", "society6", "stuart_weitzman_ca", "superior_threads", "swimsuitsforall", "tarte", "thinkgeek", "nike_greece_greek", "nike_spain_catalan", "brooks_brothers", "teleflora", "underarmour_ca", "underarmour_fr", "staples", "t_mobile", "soludos", "tommyjohn", "calvin_klein", "design_within_reach", "discountschoolsupply", "eyebuy", "eyebuy_ca", "jpcycles", "lucky_jeans", "primary", "serena_and_lily", "staples_advantage", "staples_ca", "staples_ca_fr", "tjmaxx", "underarmour", "underarmour_at", "underarmour_au", "underarmour_be", "underarmour_br", "underarmour_cl", "underarmour_de", "underarmour_dk", "underarmour_es", "underarmour_id", "underarmour_ie", "underarmour_it", "underarmour_mx", "underarmour_my", "underarmour_nl", "underarmour_nz", "underarmour_ph", "underarmour_pl", "underarmour_pt", "underarmour_se", "underarmour_sg", "underarmour_sk", "underarmour_th", "underarmour_tk", "underarmour_uk", "wwe", "zachys", "t_mobile_prepaid", "cdw", "cdw1"];
// let compiledFiles = fs.readdirSync('/src/integrations/compiled').filter(file => !file.includes('debug')).filter(file => partners.includes(file.replace('.js', '')));

// let yes = [];
// let no = [];
// for (let file of compiledFiles) {
//     let code = fs.readFileSync(`/src/integrations/compiled/${file}`).toString('utf-8');
//     let namespace = file.replace('.js', '');

//     let matched = code.match(/jQuery\.[^min]|[^check]jQuery\(|\$\.|\$\(/i);
//     // let matched = code.match(/checkJquery\(\)/)
//     if (matched) {
//         console.log(namespace, matched[0]);
//         yes.push(namespace);
//     } else {
//         console.log(namespace, 'NOOOOOOOO');
//         no.push(namespace);
//     }

//     // console.log(namespace, /jQuery\.|jQuery\(|\$\.|\$\(/.test(code))
// }

// console.log('-----------USES JQUERY------------')
// for (let n of yes) {
//     console.log(n)
// }

// console.log('----------------------------')
// console.log('----------------------------')
// console.log('----------------------------')
// console.log('-----------DOES NOT USE JQUERY------------')

// for (let n of no) {
//     console.log(n)
// }
let noJQuery = ["1stdibs_uk", "500_level", "511tactical", "EQ3", "_semantic", "abt", "ada", "amsoil_ca", "audio_advice", "bassett_furniture", "bby", "beautycounter", "bestseller_ca", "beyond_the_rack", "blue_nile_au", "blue_nile_ca", "blue_nile_uk", "cdw1", "cdwg", "champssports", "coach_ca", "coach_de", "coach_es", "coach_fr", "coach_it", "coach_uk", "converse_be", "david_yurman_fr", "dealnews", "eastbay", "ecowater", "edible_arrangements", "electronic_express", "footaction", "footlocker", "footlocker_ca", "gg_alzheimers", "gg_diabetes", "gg_hopefaithlove", "gg_theanimalrescuesite", "gg_theautismsite", "gg_thebreastcancersite", "gg_thehungersite", "gg_theliteracysite", "gg_therainforestsite", "gg_theveteranssite", "happyxnature", "hayneedle", "icm", "kids_footlocker", "lady_footlocker", "midwest_supplies", "monicaandandy", "mountain_hardware_us", "nofrills", "paulas_choice", "paulas_choice_au", "quest_nutrition", "sephora", "sorrel_us", "ssww", "strapworks", "terez", "uncommonsense", "vermont_country_store"]

for (let namespace of noJQuery) {
    let integrationCode = fs.readFileSync(`/src/integrations/src/${namespace}_integration.js`).toString('utf-8');
    let finalCode = 'triggermail.__doNotWaitForJQuery = true;\n' + integrationCode;

    fs.writeFileSync(`/src/integrations/src/${namespace}_integration.js`, finalCode, (error) => {
        if (error) {
            throw error;
        } else {
            console.log(namespace, '-----added variable')
        }

    });
}

