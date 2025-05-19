# -*- coding: utf-8 -*-
# Alchemical dictionary, v. 1.0.1
# Created and curated by Zdenko Vozar
# Based on secondary literature collections (Figala, Moreau, Colinet, ...) and primary literature analysis (some lemmas specific, because of typos in original sources, different transcriptions and NLP lemmatisation)
# Modifications:
# v. 1.0.1: 2025.05.19 Initial zenodo publication

def item_caps(lst):
    tmp=[]
    for item in lst:
        tmp.append(item.capitalize())
    return tmp

def item_decaps(lst):
    tmp=[]
    for item in lst:
        tmp.append(item.lower())
    return tmp

# To by imported by main.py
#pars, frater, mater, muliera, nutus, vulgus, fructus, foetus,uxor, infans.
elements       = ['aer', 'aqua', 'aque', 'ignis', 'terra', 'tellus']                                            
colors_white_luna  = ['albedus','albeda','albedum','albus', 'alba','album', 'argenteus', 
                'argentea', 'argenteum','blancus','blanca','blancum', 'candor', 'castus', 'casta', 'castum','candidus', 'candida', 'candidum', 
                'innocens', 'lacteus','lactea','lacteum','lacteolus', 'lacteola', 'lacteolum','limpidus','limpida','limpidum', 
                'purus','pura','purum']
colors_red_gold = ['aureus', 'aurea', 'aureum', 'martis', 'rubeus','rubea', 'rubeum', 
                'rubificus', 'rubor', 'sanguineus','sanguinea','sanguineum', 'purpureus', 'purpurea','purpureum']
colors_yellow  = ['alacra','citrinus', 'citrina', 'citrinum', 'citrinitas', 'flavus', 'flava', 'flavum',  'flavi']
colors_green   = ['viridis','viride']
colors_black   = ['ater', 'atra','atrum', 'bilis', 'caligo', 'conspurcatus','conspurcata',
                'conspurcatum', 'fuscus', 'fusca', 'fuscum', 'incestus', 'incesta', 'incestum',
                'niger','nigra','nigrum','obnoxius','obnoxia','obnoxium','polluto', 'polluta']
colors_varia   = ['glaucito','glaucitas','lividus', 'livida', 'lividum', 'pavo','pavonis', 
                'violaceus','violacea','violaceum']
main_stages    = ['albatio', 'albedio', 'albedo', 'flavedo', 'citrinatio', 'citrino', 
                'dealbo', 'dealbatio', 'nigredine', 'nigredo', 'rubedine', 'rubedo', 'rubeo', 'rubes', 'rubido','rubifico', 'rubificatio', 'rubefio', 'rubigo', 'splendeo', 'tinco', 'tingo', 'transmuto', 'virido']
colors         = ['aestas', 'aestus', 'color']  + colors_varia + colors_black + colors_yellow + colors_white_luna + colors_red_gold + colors_green     # cauda pavonis,
operations_transitive = ['cambio',   'compositio', 'confectio', 'coniunctio', 'conjunctio',
                'converto','corrumpo', 'dissiparo', 'incorporo', 'ingredior', 'minuo', 'multiplicatio','muto','permuto', 'proiectio','prohicio','projicio','proicio','sumo','recondo','vigoro']
operations     = ['abluo', 'absumo', 'accido', 'acquiro', 'administro', 'affligo', 
                'albefacio', 'alteratio', 'augmento', 'destillo', 'destillare', 'abicio', 'abluro', 'ablutio', 'ablutio', 'abscindo', 'accendo', 'accipio', 'aceo', 'accendo', 'addo', 'adfeo', 'adfero', 'adhereo', 'adhaereo', 'adhibeo','adicio','adipiscor', 'adiungo','adiuvo', 'adjuvo', 'adjungo', 'alo', 'admisceo', 'aduro', 'affero', 'aggrego', 'altero', 'amalgamatio', 'amalgare',
                'apiscor', 'applico', 'appono', 'approbo', 'ardeo', 'adscendo', 'ascendo','ascensio', 'accenso', 'assatio', 'assimulo', 'asso', 'assigno', 'assiduo', 'attingo', 'augeo', 'augmentatio', 'auri', 'aufero', 'balneo', 'bibo', 'caedo', 'callare', 'calcina', 'calcino', 'calcinatio', 'caltinatio', 'caldidiare',
                'calefacio', 'calfacio', 'calefacto', 'candeo', 'claudo',
                'carbo', 'cementatio', 'ceratio', 'cesso',  'ciba', 'cibo', 'cibatio', 'cineratio', 'cinero', 'clarifico', 'clarificatio', 'coagula', 'coagulatio', 'coagulo', 'coagulor', 'coapto', 'coctio', 'coepi', 'collecto', 'colloco', 'colligo', 'coloratio', 'coloro', 'confirmo', 'comburo', 'comburatio', 'combustio',
                'commisceo', 'commixtio', 'competo', 'compleo', 'completo', 'compono', 'concludo', 'condo', 'conscindo', 'confecto', 'conficio', 'confringo', 'conor','conpositio', 'congela', 'congelatio', 'congelo', 'conglutino', 'conservo', 'conspurco', 'consumptio', 'consumo', 'contingo', 'conversio', 'convertirem', 'cooperio', 'corrodo', 'coquo',  'cupelatio', 'cupelo',
                'coronatio', 'coque', 'coquendo', 'coquor', 'custodio', 'cribra', 'cribro', 'decapitatio', 'deco', 'decoctio', 'decoco', 'decoque','decoquo', 'decoro', 'deduco', 'deleo', 'deleteo', 'demeto', 'denudo', 'dequoquor', 'depono','depuro', 'dequoquor', 'descensio', 'desicco', 'desicceo', 'destruo', 'dimidio', 'diminuo', 'diminutio',
                'disolutio', 'dispono', 'dispositio', 'dissero', 'dissoluo', 'dissolvo', 'dissolutio', 'distilla', 'distillo', 'distillatio', 'distilatio','destilatio','destillatio', 'diverto', 'divido', 'duresco', 'duro', 'egredior',
                'effundo','emendare','emendo', 'emo', 'enceratio', 'erubesco', 'evanesco','evaporo', 'evinco', 'exalto', 'examinatio', 'excedo', 'exhalo', 'exhaurio', 'exigo', 'exicco', 'exime', 'eximo', 'expando', 'expedio', 'expello', 'experior', 'exsicatio', 'exsicco', 'extingo', 'extinguo','extractio', 'extraho', 'exuberatio', 'exubere', 'fermento', 'fermentatio', 'ferveo', 'fervo', 'filtro', 'filtrare', 'fingo', 'fixatio', 'fixio', 'fixo', 'fixor', 'flo', 'folio', 'foro', 'fractio', 'frango','frico', 'frigesco', 'frigido', 'fugo', 'fumigo', 'fumigeo',
                'fundo', 'fusco', 'fusio', 'fulgo', 'fundo', 'genero', 'haurio', 'humecto', 'humeo', 'ignesco','ignio', 'ignitio', 'illumino', 'imbibitio', 'imbibibo', 'incinero','imbibatio', 'imbuo', 'immineo', 'immitto',
                'impedio', 'impingo', 'impono', 'impregno', 'inbibitio', 'incendo', 'incero', 'incido', 'includo', 'incipio', 'induco', 'induratio', 'infero', 'inficio', 'infrigido', 'infundo', 'infusio', 'ingredio', 'inhumo', 'inspicio', 'inspiro', 'intensio', 'introeo', 'intromitto', 'inungo', 'inunguo', 'invenio', 'investigo', 'inquiro', 'itera', 'itero', 'iungo', 'quaero', 
                'lacto', 'laboro', 'lamo', 'lavo', 'limo', 'lino', 'liquefacer', 'liquefactio', 'liquefacio', 'liquefatio', 'liquefio', 'liquesco', 'liquescento', 'liquo', 'lotio', 'luero', 'luo', 'lutatio', 'magnifico', 'melioro', 'meto', 'metero', 'misceo', 'modero', 'mollifico', 'moror', 'mortifico', 'mortificatio',
                'multiplicatio', 'multiplico', 'mundo', 'mundificatio', 'mundifico', 'mutatio', 'nato', 'numerato', 'nutrio', 
                'obtineo', 'optineo', 'obturo',
                'pando', 'pasco', 'paeniteo', 'patefacio', 'penetro', 'penetratio',  'percutio', 'perficio', 'perimo', 'perscrutor', 'persevero', 'persequor', 'permisceo', 'permitto', 'perpendo', 'pingo', 'pondero', 'pono', 'portio','possideo', 'poto', 'praecaveo', 'preparo', 'praeparo', 'praeparatio', 'priuo', 'privo','probo', 'probatio', 'procreo', 'proficio', 'prohibeo', 'proiectio', 'projectio', 'prosequor', 'provenio', 'provideo',  'purgatio', 'purgo',  'purificatio',
                'putrefacio', 'putrefactio','putrescero', 'quero', 'rarifico', 'rarificatio', 'recedo', 'rectifico', 'redigo', 'reduco', 'reductio','reducanto', 'refrigero', 'reitero', 'reiteratio', 'remotio', 'remoueo', 'removeo', 'renoveo', 'repleo', 'repono',  'rescindo', 'resero', 'reservo', 'resolvo', 'resolutio', 'respiro', 'resto', 'retineo', 'revelo','revivo', 'revolvo', 'salio', 'sallo', 'scindo', 'secerno', 'segrego', 'servo', 'separatio', 'separo', 'sequor', 'sicco',
                'solido', 'solutio', 'solvo', 'specto', 'spisso', 'speculatio', 'stringo', 'subdo', 'subiaceo', 'subjaceo', 'subigo', 'subicio', 'subjcio', 'subjicio', 'subiungo', 'subjungo', 'sublevo', 'sublimo', 'sublimatio', 'subtilio', 'submergo', 'subtiliare',
                'subtiliatio', 'sudo', 'suffoco', 'superabundo', 'superemineo', 'superfluo', 'supero', 'superpono', 'suppono', 'suscito', 'suspendo', 'sustineo', 'tero', 'tereo', 'teneo', 'tollo', 'tracto', 'transfero', 'transformo', 'trituratio', 'trunco', 'valeo', 'verto', 'vivifico', 'violo', 'vinco', 'vito', 'viter'] + operations_transitive #+ main_stages
#reor, reperio, reverberatio, reveror, tango, tarto, vendo
# Instuments and terminus technicus
instruments    = ['accipientia', 'alcutia','alembicus', 'alambic', 'alembic', 'alumbic', 
                'allenbics', 'alembichum', 'amphora', 'ampullus', 'allembichum', 'allenbik', 'almazarat', 'aludel',
                'ampulla', 'ampullula', 'alutel', 'aluthel', 'alveolus', 'athanor', 'bacia', 'bachia', 'baculum', 'balneum', 'balneus', 'barbatum', 'botus', 'botum', 'calix',
                'calamus', 'caldariun', 'campanus', 'canna', 'capolla', 'capellos', 'capitelum', 'capitellum', 'caputium', 'catini', 'catinus', 'cazola','candela', 'carbon',
                'clavus','claves', 'cineritium', 'collum', 'colum', 'coecus', 'caecus', 'cooperculum', 'coopercullum', 'coopertorium', 'cornus', 'criseolon','criseolo','ciseolo','criseolus','ciseolus', 'crucibulum', 'cuculata',
                'cucurbitus', 'cucurbita', 'culter', 'culteus', 'cupella','cuza', 'cydaris', 'diadema', 'fiala', 'filter', 'filtrum', 'fiola', 'flamma', 'follis', 'fossor', 'foramen', 'forcipes','forceps', 'forma', 'fornax', 'fovea', 'furnax', 'furnum', 'furnus','furnellus','furnellos','furnellum',
                'garganta', 'gargaura', 'geranium',
                'incus', 'instrumentum','intestinum', 'limus', 'linea', 'lena', 'lutum', 'luto', 'matula', 'matulla', 'maleus', 'malleus', 'matratium', 'mortario', 'mortarium', 'mortarius', 'naphis', 'nodus', 'ola', 'olla', 'ollis', 'operculum', 'opercullum', 'patella','pastillum', 'pelicanus', 'pileus', 'pilleus',
                'pondus', 'phiala', 'phyala','phialam', 'phiola', 'phiolla', 'phyalam','pigne', 'pruna', 'pyxis', 'receptaculum', 'refrigerium', 'retorta', 'retortula', 'retortulla', 'rostratus','rostri', 'sartagine', 'scrinia', 'scutela', 'scutella', 'spatula', 'sublimatoria', 'syringa',
                'terraceus', 'testa','telus', 'tuba', 'turibula', 'vas', 'uas', 'urceus', 'vasa', 'uasa', 'vasus', 'uasus', 'vascula','uascula', 'ascensum', 'descensum',
                'ventosa', 'tabula', 'tenaculis','telon','telonus', 'tigilum','tigillum', 'tradentia', 'tripus','tripodis', 'tubulus', 'virga', 'virgula'] # ignis regimina
instruments    = instruments + item_caps(instruments)
symbols_uni    = ['amor','andros', 'apis', 'aquilo', 'aquila', 'argus', 'avis', 'basiliscus', 
                'canis', 'caput', 'capillus', 'caro', 'cauda', 'cervus', 'cervix', 'ciconia',
                'colubra', 'columba', 'conceptio','concipio', 'conjugium', 'coniugium', 'conjungo','copulo', 'cor', 'corvus', 'crocus', 'draco', 'equus', 'falco','falla','fella', 'feces', 'filius', 'femina', 
                'foemina', 'foemen', 'frater',  'fructus',  'flos', 'gallus', 'gallina', 'germen','germana', 'germanus', 'imperium','lac', 'leo','limatio', 'lupus', 'margarita', 'melissa', 'marito', 'mater', 'matrimonium', 'matrix',
                'menstruum', 'mulier', 'nuptialis', 'nuptale', 'os', 'orella', 'ovo', 'ovor', 'auricula', 'ovum', 'pater', 'pectus', 'puer', 'punica', 'rapio', 'sanguis', 'sangvio', 'sarx', 'semen', 'semino','sepultrum','serpens', 
                'servus', 'soror', 'sponsalitium', 'thalamus', 'turris', 'venter','violentia', 'vipera', 'vir'] # pelican, pes
symbols_uni     = symbols_uni + item_caps(symbols_uni)
## To deprecate
symbols_MWE_unl = ['albo_colore', 'alii_plures', 'albumen_ovi', 'aqua mercurii', 'aqua_Mercurii', 'aqua_permaneo', 'argentum_uiuus', 
                'argentum_vivus', 'clara_ovi', 'corpore magnesiae', 'dens_diaboli', 'dicitur_emendare', 'dictum_est',
                'facio_dico', 'facta_sunt', 'fortitudo_saeculi', 'herba_sana', 'homines_naturales', 'lapidis_operationem', 'lapis benedictus', 'lapis_noster', 'lapis_philosophorum','lapis preciosus', 'luce_filiorum', 'magnus_arcanum', 
                'natura_naturam', 'omnis_color', 'operari_volens', 'pannus_linneus', 'perire_facit', 
                'scilicet_quando', 'scilicet_usque', 'servi_rubei', 'spiritus_vini', 'sulfurus_aqua', 'tingente_accipit', 'terra_magisterii', 
                'turba_optimus', 'tyrius_color', 'virtutum_animae'] # Frequent symbolic collocations
## To deprecate
ops_turba = ['incido', 'calefacio', 'raresco', 'disiungo', 'coniungo', 'frigesco', 'comburo', 
                'constituo', 'separo', 'ascendo', 'suppono', 'vinco', 'frigesco', 'coaduno', 'congrego', 'spitto', 'quiesco'] #coniungo
#mat_subsatnces = ['mercurium','sulphur','sal']
mat_substances_food_ar     = ['almori', 'sirupum','syrupum', 'zucarum','zucara','zucari']
mat_substances_food_lt     = ['agaric','agaricum','alium','apium','casei', 'butyro','butyrum','botiro','butiro', 'farina', 'mel','pasta','vinum'] #lac
mat_substances_veg_ar = ['albelui', 'alcalcodre','alfolba', 'alginz', 'alchizaran', 'alchizaram', 'aloen', 'arroz', 'asfode','asfodel','asfodium','anefagga','borago', 'falle',
                'fu', 'galanga','galangar',
                'maulmbercum', 'mu', 'muscus', 'porcilaca','portulaca','portulacae', 'portulace', 'rigaricium', 'sandalum',
                'vitellus','xall','zaphaneria']
mat_substances_veg_lt = ['alumis', 'avellana', 'barabas', 'bdellion', 'bletes', 'capilli', 
                'castanella', 'cera', 'cero', 'collanderllum', 'dragagantum', 'frumentum', 'girgentis', 'girgontis', 'geldum', 'gergozos', 'chelidonia', 'mirtus', 'olea', 'oliva', 'parabas', 'pepo', 'pipinellus',
                'rafanos', 'sosa', 'spic', 'squinantum', 'sticados', 'stoechas', 'tragagantum', 'tribit', 'turbit'] #casta
mat_substances_ani_ar = ['achavo', 'algerid', 'anoca', 'gragras','hanoca']
mat_substances_ani_lt = ['abaxes', 'castoson', 'cocollata','belotta', 'fimus', 'kenkel', 
                'kenckel', 'perla', 'rana','ratus', 'rata', 'sapon', 'saponis', 'scoria', 'stentinum', 'tartuca','urina','vitulus','vitula','vitella'] #sanguis
mat_substances_ar     = ['acerabam', 'acavene', 'aceton', 'acochis', 'albenzar', 'alcofol',
                'algaceram','algarani', 'alalkoth', 'alanoch','alasphor','alasrob',
                'albac','alfirsen', 'algir','alkali','alkir', 'alkitan','alkofol', 'alleasol','alsurin','alum', 'alumen', 'almarkaside','armacassida',
                'annoxate','anoxate','anoxatir', 'attincar', 'attramusces',
                'azenzar', 'azer', 'azezi', 'alhanzar', 'azimar','baurac', 'baurax', 'boritis', 'calacant',
                'calcande', 'calcantum', 'calcantus', 'calcadi','calcandis','calcadis',  'calcadiz', 'calcaphanos', 'calcamenum', 'calcecumenon', 'calcatar', 'calcothar', 'calhi', 'coloti',
                'corsufle', 'cerob','cebal',
                'lachesir', 'espili', 'espini', 'gar','gariar',
                'hajar', 'latun','lato','alato','allato','allaton',
                'harsufle', 'kacabre', 'karesin', 'kartax', 'ixfili', 'lubrit', 'kibrit','kir', 'maganice', 'maganicea', 'magnesia', 'magnetia', 'Magnesia', 'magrani', 'magrane','almahagra',
                'magrane', 'marcasida','marcassida', 'marcasita', 'marchasita', 'marhasita', 'armacasida', 'morabetini','morabunt','martek', 'mugra', 'mucra',
                'racienti','realgar', 'sauen', 'samem', 'sericon', 'sericizar', 'servicizar', 'setariz', 'sumum', 'shaytan', 'tasrasim','teficin','tinga', 'tinchar', 'tinkar', 'tutia', 'uzifur', 'yle', 'ynoc',
                'uzifur','zanjar', 'zarnec','zegi','zenderich','zarunde','zimar','zunzar']
ms_AU_lt        = ['aurum', 'chrysos', 'sol', 'Sol', 'sole','solem']
ms_AU_ar        = ['coloti','exarchi','zafran', 'zafrani', 'zafri','zarchi']
ms_AG_lt        = ['argentum','luna', 'Luna', 'lune', 'luane','lunam']
ms_AG_ar        = []
ms_HG_lt        = ['hydrargyrum', 'mercurium', 'mercurius', 'Mercurius', 'mercurio','Mercurio', 'mercurialis','mercurii']
ms_HG_ar        = ['achavo', 'azoc', 'azoth', 'cambar','quinbar','sebic','zibaq']
ms_S_lt         = ['canonatum', 'venus','Venus','sulfur', 'sulphur']
ms_S_ar         = ['aranici','azenzar', 'safran','zafran']
ms_CU_lt        = ['cuprum','es','veneris','Veneris']
ms_CU_ar        = []
ms_ST_lt        = ['stagnum', 'stangnum', 'stannum', 'stannus','iupiter','iuppiter','Iupiter','Iuppiter','Iovis','iovis', 'Jovis','jovis']
ms_ST_ar        = ['talicon', 'taliconi']
ms_AS_lt        = ['auripigment', 'auripigmentum','auripimentum']
ms_AS_ar        = ['realgar','sandarakhi','zarnec']
ms_PB_lt        = ['blanchetum', 'litargium','litargirum', 'saturn', 'Saturn', 'saturnus', 'Saturnus', 'plumbum','plumbs']
ms_PB_ar        = ['acercon', 'asronj', 'gessuri', 'gozi','keion', 'isrengenz', 'martek', 'zoal','zuhal']
ms_FE_lt        = ['ferrum', 'mars', 'Mars','marte','marti', 'Marti', 'martius','Martius', 'calibe','calibs','chalyps']
ms_FE_ar        = []
mat_substances_elementa = ms_AU_lt + ms_AU_ar + ms_AG_lt + ms_AG_ar + ms_HG_lt  + ms_S_lt + ms_S_ar + ms_CU_lt + ms_CU_ar + ms_ST_lt + ms_ST_ar + ms_AS_lt + ms_AS_ar + ms_PB_lt + ms_PB_ar + ms_FE_lt + ms_FE_ar
mat_substances  = ['aceto', 'acetum', 'acutus','acuta','acutum', 'adusto','adustus','adusta', 'aes', 'ammoniac', 'armoniac', 'armoniacus', 'amostrari', 'andromanta', 'anthium',
                'arentium', 'arsenicum', 'asceni', 'attoronge','atorongis','attorongis', 'atramentum', 
                'auricalcum','borax','borico', 
                'cabunculus', 'calamina', 'cadmia', 'calx', 'calcis', 'calcus', 'calibe','calibs','chalyps',
                'cambar', 'camphora', 'carbunculus', 'carmini', 'catesin', 'cement', 'cementum', 'cenobrium', 'cerusa', 'ceruse', 'cinis', 'ciner','cinerum','cineres', 'cinus', 'cinabrium', 'cinnabar','compositiones',
                'dragantum','electrum', 'eramine', 'ethelie', 'ethelia', 'faex', 'favilla','folossus', 'fullosus', 'fex', 'flor', 'fuligo', 'fundus', 'fumus',
                'galbanum', 'gemma', 'glacies', 'guma', 'gumma', 'gummae', 'gypsum', 'hyrcum',
                'lamina', 'lapia','litargo', 'metallum',
                'minium','natron', 'niter', 'nitri', 'nitrum', 'nix', 'nummus', 'oleum', 'panis', 'pannum', 'plata', 'plumbum', 'plumbus', 'pulvis', 'sal','salis','salem','sale','scutum','scutus', 'smirrilus',
                'spinae','squama', 'stercus', 'stibi', 'stimmi', 'stimmium', 'substantia',
                'surianum', 'tartarus', 'terreum', 'vapor', 'verdigris', 'vermilio', 'vitreo', 'vitreolum', 'vitriol', 'vitriolo', 'vitriolum', 'vitrum' #'carbo',
                  ]
mat_stones_ar = ['alchahat','bazar','jacut','pirat','saphir','sapherum','zamrad']
mat_stones    = ['alectorius', 'ambra', 'anhomiomera', 'armenicus', 'azur', 'balagius', 
                'berilus', 'berillus', 'berylus', 'athichos', 'atitos', 'calcedonius', 'cristallus', 'cristalus', 'chrystallus',
                'cuchul', 'dehenegi', 'edaus', 'emathita', 'ferruzegi', 'filacterium', 'funcu', 'gagate', 'gegolitus', 
                'gir', 'gipsa', 'homiomera', 'iacintus', 'iaspis', 'ismaris', 'kuhul', 'lipparea', 'lunares', 'marmor', 'memphites', 'onix', 'onyx', 'orphanus',
                'petra','rubinus','quandros', 'sadda','saphirus', 'saphyrus', 'sedena', 'sedina', 'smaragdus', 'spehen', 'talca', 'terminati', 'thutia', 'topazius']  + mat_stones_ar # carbunculus
mat_substances  = mat_substances + mat_substances_ar + mat_substances_veg_lt + mat_substances_veg_ar + mat_substances_ani_lt + mat_substances_ani_ar + mat_substances_food_ar + mat_substances_food_lt + mat_substances_elementa + mat_stones #ADDED STONES #ars. sulfidy, odpad, vinny destilat, servus fugitivus -r., metal ores, squama aeris, flos aeirs, sal alkali
mat_substances = mat_substances + item_caps(mat_substances)

mat_stones = ['abcd','tuvx']
#medius #Medieval Latin produced specularis and on Greek roots filacterium and orphanus. Some stones were named for places: lippares (liparea, lypparea), found in the Lipari islands; memphites from Memphis; medius from Media; lapis armenicus from Armenia; and (Arabic­derived) balagius from Badakhshan. A magical gem found in the brain of a vulture was called a quandros, and the alectorius was said to come from the gizzard of a castrated cock.
titulations   = ['alkymista','alchymista','abba','abbas', 'baccalaureus', 'basilis', 
                'consulus', 'discipulus', 'doctor', 'dominus', 'domina', 'figulus', 'investigator','inuestigator', 'magister', 'magistrus', 'medicus', 'milites', 'philosophus', 'philosphus', 'philolophus', 'princeps', 'pietas', 'principium', 'princeps', 'regi', 'rex','sapiens','socius','sponsus','sponsae','turba']
titulations   = titulations + item_caps(titulations)
rel_concepts  = ['beatus','credo','occulto','magica','divinitas','spiritus', 'fatum', 'fides', 
                'anima', 'coelus','influxus','patiens', 'reverentia', 'salus', 'virtus', 'imago', 'praestigiatura', 'paradisus','spero', 'nativitas','natiuitas'] #'deus', 'nativitas','planeta','stella','signum'
concepts      = ['caliditas', 'decoctiones', 'demonstratio','calor', 'cave','caveo', 'colla', 'complexio',
                'corruptio', 'deceptor', 'elementum','emendatio','experientia', 'frigiditas', 'generatio', 'gradus', 'humiditas', 'infirmitas', 'insipientia', 'labor',
                'nervus', 'pecunia', 'pius', 'prolixitas','recepta', 
                'procreatio','rite','sicciditas','spissitudo', 'tenebrae', 'umbra', 'uterus', 'venenum', 'veneum', 
                'vita', 'virtus','via', 'vice', 'zandarich']
lit_references = ['aenigma','allegoria', 'carmina', 'exemplum', 'oratio', 'parabola', 
                'sententia', 'capitulum', 'descriptio', 'liber', 'libellus',  'libelus', 'rosarius', 'scriptum', 'scriptura', 'sermo', 'summus', 'testificor','testis', 'titulus', 'tractatus', 'versus']
lit_references = lit_references + item_caps(lit_references) # To add to some cat
scie1_concepts = ['accidens', 'agens','annus', 'anus', 'damno', 'doctrina', 'doceo', 'dubium', 
                'erro', 'firmamentum', 'intellegibilis','intellegibile','intelligibilis','intelligibile', 'magisterium', 'medicina','medicinae', 'medica', 'morbus', 'mors','natura', 'nebula', 'nubes', 'ignorantia','planeta','planetae', 'philosophia', 'philosophicus', 'philosophica','physica','phisica',  'proprietas', 'qualitas', 'rationalis',  'scientia', 'signo', 'signum','simulacrum', 'stella', 'studium']
scie1_concepts = scie1_concepts + item_caps(scie1_concepts)
met_concepts = ['aetas', 'alchemia', 'alchymia', 'alkymia', 'arcana', 'ars', 'artifex',   
                'artificialis', 'artificium', 'aequalitas', 'apparentia', 'attestor', 'attraho', 'caelum', 'chemica', 'certitudo', 'cibus','coelus', 'coelum', 'complementum', 'compositum', 'coquis', 'corono', 'corporeitas', 'cortex', 'croceo', 'corpus', 'corruptio', 'creatura',  'differentia', 'devoro', 'donum', 'essencia','essentia', 'essentialis', 'alixir', 'alexir', 'elexir', 'elixir', 'elyxir', 'elixire', 'exir','iccir','ixir','yxir','yccir','ycyr','yccyr', 'excogito', 
                'fel', 'fermentum', 'fides', 'fugitivus', 'fulgor', 'fundamentum', 'grossitia', 'humor', 'ignarus', 'imitor', 'impuritas', 'inspiratio', 'invideo','iudicium', 'iunctura', 'lapis', 'libido','lavacrum', 'levitas', 'ludus', 'lumen', 'maiestas',  'malum', 'mare', 'massa', 'materia', 'materies', 'mentior', 'minera', 'minerale', 'mixtura', 'mistura', 'modus', 'nutrimentum', 'occido', 'occulo', 'odor','operatio', 'opus', 'paupertas', 'peccatum', 'patiens', 'pretium',  'perfectio', 'pericula', 'pinguedo',  'praedico', 'predico', 'radix', 'radius', 'ratio', 'regimen', 'regnum', 'res', 'residuus','residua','residuum', 'resurgo', 'resurrectio', 'reverentia', 'ros','sanctus', 'salus', 'sanitas', 'sapor', 'sirupo', 'syrupis','spiritus', 'sordes', 'species', 'sperma', 'splendor', 'subtilitas', 'superficies', 'superfluitas',  'temperamentum', 'tempus', 'terreitas', 'terrestreitas', 'terminus', 'thesaurus', 'tinctura', 'transmutatio','transmutationis', 'tyriacus', 
                'utilitas', 'uicis', 'vicis','vinculum','vis','viscositas'] + concepts  + rel_concepts #  visus, vivo, vulgo 'deus',
#'patiens', 'sequens', 'finiuo, efludio, laetificio, revertuor, fumingo, cesso, concedo. copulato, imbibeo, iterato
met_concepts = met_concepts + item_caps(met_concepts)
scie_concepts = lit_references + scie1_concepts
geo_locs_ar     = ['adteegandi','albordali', 'albozam', 'alburchen','aledua','alhudava',
                'alhodua', 'alkalag', 'adteegandi','andarani', 'antachi',
                'armini', 'entachia','andeluz', 'arburium', 'bellengi', 'burchena', 'cichilii','corduba', 'ebrizum', 'elherachi', 'elebla', 'entachia',
                'forperia', 'goracini', 'hiameni','iameni','jameni', 'ibrizum', 'landeluz','neerim', 'obrizum', 'saracene', 'xeduna']
geo_locs_ar     = geo_locs_ar + item_caps(geo_locs_ar)
geo_locs_lt     = ['africa', 'alapia', 'halap', 'alexandria','armenia','barbaria', 'bononia', 
                'castillo', 'narbonem', 'castiglio', 'cartano',
                'corsica', 'cracovia', 'ciprus', 'cyprus', 'egyptius', 'evilat', 'florentia','gyon', 'hermineum','hermini','herminia', 'hispania','hispanicum', 
                'ierusalem','india', 'italia', 'maiorica', 'majorica', 'navarrae', 'phisan', 'sardinia', 'sicilia','tunisia','tunesia','tunixe', 'yspania','venetia','venetiis']
geo_locs_lt     = geo_locs_lt + item_caps(geo_locs_lt)
mesura = ['as','carica','centena','clavis','dram','drachma', 'dolium', 'grana','grano', 
                'granum', 'gutta','guttus','lagenae','libra','marca','marcha','pes','peysa','pisa', 'pond','pund','quartus',
                'potellum', 'quantitas', 'scrupulus', 'sextarius','telum','tela','ulna','uncia'] #pes, pondus
mesura = mesura + item_caps(mesura) 
mesura_temp = ['cotidie','cottidie','deinceps','demum','diuturnus','exinde', 'gradatim',
                'hora', 'mane','nondum','pluries','quando','quotiens','semel','simul','totiens']
# TO Deprecate
imp_style_verbs = ['dico','facio','coquo', 'scio','reducto','luto','tingo', 'misceo', 
                'emendo', 'exalto', # to deprecate
                'investigo', 'quaero', 'regio', 'appareo','video', 'noto', 'pervenio','tincto'] # for heating of metals (pepansis, epsesis, optesis) and underheating (molynsis)
adjectives = ['patientia','aureum','aurea','regis','regia','vitae' 'puerorum', 'mulierum', 
              'accerimus', 'limabilis', 'lunificus', 'transmutationis', 'prima', 'salvationis', 'spissitudo', 'pretiosus',  'magnificus', 'honorificus', 'verus','umidus','rubro', 'potabile','desideratum', 'philosophico', 'malleabilis', 'mulierum',
              'sublimatus', 'essencificatus','alcali', 'saturni','cuprum','vitriolatus', 'hispanicum','equinus','incorporeus','volatilis','arcanum'] 
adverbs   = ['abundanter','adeo','aequaliter', 'equaliter', 'alternatim','clare',
               'convenienter', 'desuper', 'frustra', 'huiusmodi', 'ibidem', 'intus', 'leniter', 'libenter', 'perfecte','protinus','saltem','saltim','similiter','sursum', 'plene','qualiter','recte', 'suaviter','totaliter','undique','vehementer','velociter','vere','vulgariter'] #modo, supra, utique                                 
# pecate lunatica, timorosa, malefica, infirma, suspiriosa, abortiva
#metrics = ['denario','dragma','libra', 'marca','obolus','uncia','dies']
# claus
quantifiers = ['abundans','aequalis', 'equalis', 'amplus','ampla','amplum' 'aliquot', 'bini',
               'binus', 'brevis', 'breuis', 'compar', 'comparis', 'copiosus','copiosa','copiosum', 'complures', 'continuo', 'continuus', 'continuatio', 'digitus', 'duplex', 'duplus','dupla','duplum', 'triduum', 'triplus', 'largior','largius','larga','largum','lenus', 'levis', 'magnus', 
               'maximus', 'medianus', 'mediana', 'medianum', 'medietas', 'minus', 'minimus', 'minima', 'minime', 'multi', 'multus', 'nimis','nonnuli', 'parvus', 'paruus', 'paucus', 'paululum', 'paullulum', 'plenus', 'plerique', 'unus','unam','duos','duas',
               'pars','partes',  'parvus','parva','parvo','parum', 'punctus', 'satis', 'quadruplex', 'triplex', 'quater', 'quinquies','quinquiens', 'sexies','sexiens', 'septies','septiens','decem','cento','mille','totidem','unicus','unio']  + mesura + mesura_temp # 'largus',
qualifiers  = ['acer','acris','acre', 'adipiscus', 'adustibilia', 'adustibilius', 'aereus',    
               'aerea', 'affirmatus','affirmata','affirmato', 'albe', 'alkalis', 'alcofolis', 'amarus','amara', 'amarum','amoenus', 'amoena','amoenum', 'ample', 'animabilis', 'animatum', 'animata', 'animatus', 
               'aranico','ardens', 'aquaticus', 'aqueitatis','aquea','aqueus', 'aquosus', 'assus', 'assa', 'assum','assatus', 'assata','assatum', 'assiduus', 'assidua', 'assiduum', 'attramus',  'beata', 'beatum', 'benedictus','benedicta','benedictum', 
               'bonus', 'bona', 'brutus', 'bruta', 'brutum', 'caelestis', 'caelesta', 'caelestum', 'coelestis', 'coelesta', 'coelestum', 'calidus', 'calida', 'calidum', 'callidus','callida','callidum', 'certus', 'certa', 'certum', 'circuitum', 'circuita', 'circuitum', 'clarus', 'clara','clarum',
               'claus', 'clausus','clausa', 'clausum', 'coagulatum', 'coagulata', 'coagulatum', 'combustus', 'combusta', 'communis', 'completus','completa', 'concavus', 'congruus', 'congrua', 'congruum', 'congrvus', 'congrva', 'congrvum', 'consimilis','consimile', 'continens', 'contratius', 'contraria','contrarium', 
               'corsuflus', 'corsufla', 'corsuflum', 'corruptus', 'corrupta', 'corruptum', 'cribellatus','cribellata','cribellatum', 'cristalinus','cristalina', 'cristalinum', 'cristallinus','cristallina', 'cristallinum', 'croceus','crocea','croceum', 'crudus', 'cruda', 'crudum', 'cunctus', 'cuncta', 'cunctum', 'dealbatus','dealbata', 'dealbatum', 'debilis', 'debile', 
               'decoctus' 'decocta', 'decoctum', 'difficilis', 'difficile', 'dignus', 'digna','dignum', 'divinus', 'divina', 'divinum', 'dulcis', 'dulce', 'elevatus', 'elevata','elevatum', 'equinus', 'excelsus', 'excelsa', 'excelsum', 'extraneus', 'extranea','extraneum', 'facilis','facile',
               'fatuus', 'fatua', 'fatuum', 'fessus', 'fessa', 'fessum', 'ferreus', 'ferreas', 'ferreum', 'fidelis', 'flammans', 'foetidus',  'fetidus', 'foetida', 'fetida', 'foetidum','fetidum', 
               'faetidus', 'faetida', 'faetidum', 'foetus', 'foeta', 'foetum', 'foliatus', 'foliata', 'foliatum', 'fortis', 'forte', 'frangibilis','frangibile', 'fulgidus', 'fulgida', 'fulgidum', 'frigidus', 'frigida', 'frigidum', 'fructuosus', 'fructuosa','fructuosum', 'fusibilis',
               'grossus','grossities', 'humidus', 'humida', 'humidum', 'immeritus', 'immerita', 'immeritum', 'immundus',	'immunda',	'immundum', 'impalpabilis', 'impalpabile', 'impossibilis','impossibile', 'innumerabilis','innumerabile', 'integer', 'integra','integrum',
               'igneus', 'ignea', 'igneum', 'inalterabilis', 'incombustibilis', 'indelibilis', 'indelibile', 'indigestus','indigesta','indigestum',
               'indivisibilis', 'inferius','inferia', 'inferium', 'infinitus', 'infinita', 'infinitum', 'insipiens', 'intensus', 'intensus', 'intensa','intensum',
               'intimus', 'intrinsecus', 'intrinseca', 'intrinsecum', 'invariabilis', 'invicem', 'inuicem', 'invidus', 'invisibilis', 'irrigatus', 'irrigata', 'lapideus', 'lapidum', 'laudabilis', 'laudabile', 'lenis', 'lene', 'lentus','lenta','lentum', 'limaturus','limatura','limaturum', 'liquidus', 'liquida','liquidum', 'longus', 'longa','longum', 'lucida','lucidum','lucidus', 'madefactus', 'madefacta','madefactum', 'magnificus', 'manifestus','marium', 'masculus', 
               'masculum', 'masculinus','masculina','masculinum','materialis', 'marinus', 'marina', 'marinum', 'medius', 'media', 'medium', 'merum', 'mera', 'mero', 'metallicus', 'mineralis', 'mistus', 'mista', 'mistum',  'mixtus', 'mixta', 'mixtum', 'mirabilis', 'mirabilis', 'modicus', 'modica', 'modicum', 'molle', 'mollis', 'mortuus', 'mortua', 'munda','mundum', 'naturalis', 
               'necessarius', 'noster', 'noxius', 'obscuro','obscura','obscurum', 'occultus', 'occulta','occultum', 'odoriferus', 'oleaginitas', 'penitus','penita', 'penitum', 'perfectus', 'perfecta', 'perfectum', 'permaneo', 'perpetuus', 'planus', 'plana', 'planum', 'plumosus', 'plumosa', 'plumosum', 'potentus', 'practicus', 'practica', 'practicum', 'praeciosus', 'praedicatus', 'praedicata', 'praedicatum', 'praesens', 'predicatus', 'predicata', 'predicatum', 'precedo', 'preciosus', 'pretiosa', 'pretiosis',
               'pretiosus', 'pretiosa','pretiosum', 'profundus','profunda','profundum', 'propinquus','propinqua','propinquum', 'prorsus', 'prorsa', 'prorsum', 'prudens', 'pustulatum', 'radicalis', 'radicale', 'radiosa', 'radiosus','radiosum', 'rectus', 'recta','rectum', 'regalis','regale', 'roridus', 'rorida', 'roridum',
               'salsum', 'salsa', 'salsus', 'sazonata', 'secretus', 'secreta', 'secretum', 'semicoctus', 'semicocta', 'semicoctum','seorsus', 'seorsa', 'seorsum', 'siccus', 'sicca', 'siccum', 'sigillatim', 'siggilata', 'similis', 'singularis',
               'solis', 'solus', 'sola','solum', 'solidus', 'solida','solidum', 'solificus', 'solubilis', 'sordidus', 'sordida','sordidum', 'spiritualis', 'spissus','spissa','spissum', 'stultus', 'stulta','stultum', 'suavis', 'suave', 'sublimus', 'sublima', 'sublimum', 'sublimis', 'sublimatis', 'sublimata', 'sublimatum', 'subtilis', 'sulfureus', 'sulfurea','sulfureum', 'sulfurus', 'sulphureus','sulphurum', 'superficialis', 'superficiale', 'superfluus', 'superflua', 'superfluum', 'superius','superia', 'superbus', 'superba','superbum', 'susceptivus', 'susceptiva', 'susceptivum', 'tenebrosus', 'tenebrosa', 'tenebrosum', 'tener', 'tenera','tenerum', 'tenuis', 'tenue', 'tenuissimus','tenuissima', 'tenuissimum', 'teres',
               'terreus', 'toxicus', 'toxica', 'toxicum', 'transmutatis', 'turpis', 'turpe', 'ultimus', 'unctuositas', 'urinalis', 'urinale', 'ustus', 'usta', 'ustum', 'utilis', 'vacuus', 'vacua', 'vacuum', 'vanus', 'vegetabilis', 'velox', 'venenosus', 'vera', 'verax', 'veris', 'veridicus', 'verum', 'verùm', 'verus', 'vitreatus', 'vitreata', 'vitriolata', 'vitriolatus', 'vitriolus', 'vivus', 'uiuus', 'viva', 'uiva', 'vivum', 'uiuum', 'volatilis'] + geo_locs_lt + geo_locs_ar
               # 'beatus', 'mundus', 'tyrius',
               # multi, aliquot, nonnulli, complures, and plerique can be called mid-scalar, vs cardinal, maximal and minimal
qualifiers = qualifiers + adverbs + ['mundus', 'tyrius']
# Authorities
authorities_Turba = ['Arislee','Acratos', 'Acratus', 'Adimon', 'Admion', 'Afllontus',       
                'Agadimon', 'Agadmon', 'Aiadmurus', 'Amacaras', 'Anaxagoras', 'Anaxagorus', 'Anaximandros', 'Anaximenes', 'Anaximenes', 'Andaranus',
                'Apollonios', 'Archelaos', 'Archimedes', 'Arcioflus', 'Arisleus', 'Aristenes', 'Aristeus', 'Arras', 'Aros', 'Arros',  'Arsuberes','Arsubres', 'Arsulere','Arsulerem', 'Artanius', 'Arzoch', 'Ascanus', 'Ascanius', 'Aseanius',
                'Assotes', 'Assuberes', 'Astamus', 'Astanius', 'Atamus', 'Atos', 'Ayen','Avicenna', 'Aziratus', 'Baacsem', 'Bachimedi', 'Bachimedis', 'Bacoscus','Bacostus', 'Bacsem', 'Bacsen', 'Bacses',
                'Balgus', 'Balgus', 'Balinus', 'Balis', 'Bandafilus', 'Barfeus', 'Barmanidas', 'Barmanides', 'Barseus', 'Belinus', 'Belus', 'Bellus', 'Berberis', 'Bodillus', 'Bonellus', 'Bonitis',
                'Bovilis', 'Buxen', 'Cadmon', 'Cerus', 'Cinon', 'Constans', 'Costans', 'Costos', 'Costus', 'Custos', 
                'Dardani', 'Dardari', 'Dardaris','Dardius', 'Dardus', 'Democrites', 'Democritos', 'Diamedis', 'Diamedis', 'Dimocras', 'Discanius',
                'Effistus', 'Efistes', 'Efistus', 'Ekmisius', 'Ekximenus', 'Empedokles', 'Epistenus','Ersoltus',  'Ethel', 'Ethelis','Ethelius','Ethenus', 'Eximandrus', 'Eximedrus', 'Eximefus', 'Eximegorus','Eximenus', 'Eximidrius', 'Eximius', 'Exiniganus', 'Exymenus','Exumdrus', 'Euthesius',
                'Faltis', 'Fiorus', 'Fitaguras', 'Flontos', 'Florus', 'Florus', 'Foncus', 'Frictes', 'Flritius', 'Gregorios', 'Gregorius', 
                'Hefaistos', 'Heracleios','Herfolius', 'Horfachol', 'Horfolcus', 'Horfoleus', 'Horfolcis', 'Horfoltus', 'Orsolcus', 'Hyargus', 'Iargos', 'Iksimidrus', 'Iksimidrius', 'Iximindrus', 'Ixistius', 'Jargus', 'Largus', 'Leukippos', 'Locastes', 'Locustor', 'Lucas', 
                'Medritantillus','Menabdus', 'Menabdurs', 'Mesulus', 'Morfoleus', 'Mosius', 'Nephitus', 'Nabastus', 'Nicaris', 'Nictimerus', 'Nitagoras', 'Nitimerus', 'Noficus', 'Nofil', 'Obsemeganus', 'Orfultus','Orsoltus', 'Pandolfus',
                'Padolphus', 'Pandoflius', 'Pandolphis', 'Pandoflus', 'Pandophilis', 'Pandophis', 'Pandulfus',  'Pantophilus', 'Parmanides', 'Parmenides', 'Paxamos', 'Pelagios', 'Permanides', 'Phiorus', 
                'Pion', 'Pictagora', 'Pitagoraus', 'Pitaguras', 'Pithem', 'Pithen', 'Platon', 
                'Qusta', 'Rimas', 'Rinas', 'Ruius', 'Scrites', 'Sergios', 'Simon', 'Socrates', 
                'Talis', 'Tawfil', 'Thales', 'Thelus', 'Thelesinus', 'Thelisinus', 'Theofilus', 'Theophilus', 'Vitarus', 'Uitarus', 'Vitimerus', 'Uitimerus', 'Zenon', 'Zenon', 'Zeumon', 'Zimon','Zino','Zinon'] #Turba 'Calidus', 'Mundus',
authorities_mytho   = ['Apollo','Achilesve', 'Beja', 'Beia', 'Bejas','Beiia','Beiius', 
                'Cabrita', 'Cabritis', 'Cabritus', 'Gabricus', 'Hermes', 'Kabritus','Haclis', 'Hadus', 'Hermes','Hermet','Merlinus', 'Paris', 'Phoebus', 'Zoroaster']
authorities_christ  = ['Aggeus','Daniel','Habacuc','Ieremias', 'Iesus','Ievus','Ihs','Isaias',
                'Ionas','Job','Jonas','Johel','Luca','Lucas','Malachias','Maria', 'Mosius','Moises','Mosy', 'Salamon',
                'Christus','Cristus','Lucifer','Daniel','Deus','Deum','Deo','Diabolus','Diaboli','Dyaboly','Dyabolus','Dyaboli', 'Pylatus', 'Virgo', 'Yesse','Ysaias','Ysaius','Zacharias']
authorities_presoc  = ['Alchus', 'Archelaus', 'Archilaus', 'Arsuber', 'Democritus', 
                'Diomedes', 'Diamedus', 'Eximideus', 'Eximidrus', 'Hermogenes', 'Hermogeres', 'Parmenides','Heracleitus']
authorities_grec    = ['Aristoteles','Hermes', 'Socrates', 'Aristoteles', 'Phistus', 
                'Pictagoras', 'Pigtagora', 'Pitagora', 'Pythagoras', 'Pythagus', 'Pithagoras', 'Pitagoras', 'Philetes','Plato'] #'Tyrius' 'Philosophus','Philosphus',
authorities_lantic  = ['Diomedes','Dioscoridus', 'Galenus', 'Hippocratus', 'Hippocratum', 
                'Horatius', 'Macer', 'Plinius','Tulius']
authorities_byz     = ['Theophilus']
authorities_arab    = ['Aboalus', 'Abuali', 'Abincine','Abincenus','Acicenna',  'Alboiali', 
                'Albouialus', 'Alcolcotar', 'Almizadir', 'Alphidius', 'Alphydius', 'Alsurinus','Amazaras', 'Amilius','Aven', 'Avicen', 'Auicennus','Avicena',  'Avicenna','Avicenne',
                'Avicennae', 'Abuzelmi', 'Abimazer','Abumazer','Abunazer','Amizadir', 'Assen', 'Asses', 'Assenus','Azaradetus', 'Azoc','Azoch', 'Aziracus', 'Azratus', 'Bubacar', 'Bubacarda', 'Calid', 'Calith', 'Dardanus', 'Gebe',
                'Geber','Jeber', 'Ieber','Yeber','Yabar','Yaber','Yebri', 'Gebrus',  'Yebrus',
                'Habohalus','Habohaly', 'Kalid', 'Kalit','Marienus','Morianus','Morienus', 'Morienes','Rases', 'Rasis','Rasius', 'Rhases', 'Rosinus','Rosius', 'Solemi','Sahid', 'Ysidus', 'Zadith','Zahid','Zoilus','Zoilum','yeber'] #'Alasphor'
authorities_med     = ['Alemanus', 'Alamannus', 'Albertus', 'Antonius','Arnaldus',
                'Artusus', 'Aquinus','Bonifatius','Dastinus', 'Georgijus', 'Ticinensis','Helya', 'Helia','Michalis', 'Hortulanus','Hortulano',
                'Scottus', 'Johanes','Johannes', 'Johannis', 'Molendinus', 'Paulus','Phillypus','Phillipus','Philipus', 'Philypus', 'Petrus', 'Proculus',
                'Raynaldus','Rogerius', 'Roggerius','Rosinus','Robertus', 'Clementus',
                'Theodorus', 'Thibaldus', 'Thomasus','Ticinensis','Tecenensis','Ursetus', 'Compillator']
authorities_earlymodern = ['Rheticus', 'Szepsius']
authorities_unknown = ['Acteus', 'Alkien','Belthiocus', 'Bratus', 'Bulcarus','Cordus', 'Diofus', 'Diochus', 'Dracon', 'Gigil', 'Iamenes', 'Ioachimus', 'Madius', 'Marcus', 'Mergeris', 'Micedius', 'Mierdis', 'Miscus', 'Priscus','Pheyrer','Prothea','Urad'] # 'Alasrob','Keion',
auth_LiliumDeSpinis = ['hermis','geber', 'avicenna', 'arisleus', 'arsuleres', 
                'ascanius', 'atos', 'aziratus', 'balgus', 'barfeus', 
                'bonellus', 'buxen', 'calid', 'costus', 'ethel', 'eximandrus', 'eximideus', 'galenus', 'hippocratus', 
                'geber', 'gregorius', 'hermes', 'ievus','iesus', 'lucas', 'maria', 'mosius', 'morienes', 'orsolcus', 
                'pandolphus', 'phistus', 'pythagoras', 'rasius', 'robertus', 'theodorus', 'theophilus', 'diomedes','parmenides','alchus','arsuber','hermogenes','democritus','morienese','dardani'] #mercurius 'philosphus',
auth_gen            = ['Adam','Alexander',]
authorities         =   ['Gregorius', 'Pandolphus',  
                        'Theophanus'] + authorities_Turba + authorities_mytho + authorities_christ + authorities_presoc + authorities_grec + authorities_lantic + authorities_byz + authorities_arab + authorities_med + authorities_earlymodern +auth_LiliumDeSpinis + auth_gen + authorities_unknown  #Mercurius
authorities         = authorities + item_decaps(authorities) + ['Calidus', 'Mundus','Tyrius']
alch_core = elements + colors + main_stages + operations + instruments  + symbols_uni + mat_substances + mat_stones + concepts
# omnis, sermo, consilium, quatuor

not_ner_trad =['submerge', 'ab', 'ad', 'accipe','accepi', 'accepit','ait','aid','alius', 
                'amalgamatur','adaugmentandas','atendre','bene', 'cola', 'conficem', 'cum', 'de', 'dico','dicit','dies', 'donec','excusare', 'et', 'foramen','habeo','hic','haec','in','illa','ille','inde','inueo','item', 'noster','laborioso','laboriosa','loquo','loguo', 'manus', 'mane', 'melius','noster','nostra', 'nuda', 'occasus','postea','prior', 'quia','que', 'qui','quod', 'quis', 'quicumque', 'quisquis','quera','recipe','repone', 'sicut', 'sieut','subtilis','suus','sua','depone','pars','possum','primo','secundo','secundus','secundum', 'ter', 'sublimo', 'super', 'superponus', 'sum', 'tertio', 'quarto','quinque','sexto','septo', 'superponus','octavo','nono','decimo','decimouno', 'decimoduo','decimotertio','decimoquarto','cuncta','uel', 'vel', 'unus', 'una', 'ut', 'tamquam','time','tere', 'tunc', 'velut','visio',':',',']

## Summary of Vocab
colsumtext_POSAlch = ['ELE','COL','MST','OPS','INS','SYU','MAS','STO','TIT','MEC','QAN','QAL', 'AUT']
alch_vocab = [elements, colors, main_stages, operations, instruments, symbols_uni, mat_substances, scie_concepts, titulations, met_concepts, quantifiers, qualifiers, authorities] #mat_stones -> scie_concepts
alch_vocab_tit = ['elements', 'colors', 'main_stages', 'operations', 'instruments', 
                'symbols_uni', 'mat_substances', 'mat_stones', 'titulations', 'met_concepts','quantifiers', 'quantifiers','authorities']
alch_vocab_broad = [elements, colors, main_stages, operations, instruments, symbols_uni, ops_turba, mat_substances, mat_stones, titulations, concepts, met_concepts, imp_style_verbs, adjectives, adverbs, quantifiers, qualifiers, auth_LiliumDeSpinis, alch_core]
alch_vocab_tit_broad = ['elements', 'colors', 'main_stages', 'operations', 'instruments', 
                'symbols_uni', 'ops_turba', 'mat_substances', 'mat_stones', 'titulations', 'concepts', 'met_concepts', 'imp_style_verbs','adjectives', 'adverbs', 'quantifiers', 'quantifiers', 'auth_LiliumDeSpinis', 'a_core']

## Check size

#c=0
#for pos, item in enumerate(alch_vocab):
#  print(alch_vocab_tit[pos]," (",len(item),')')
#  c = c + len(item)
#print('Total',c)