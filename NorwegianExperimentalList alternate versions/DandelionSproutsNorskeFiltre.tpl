msFilterList
# Title: 🏔️ Dandelion Sprouts nordiske filtre for ryddigere nettsider
# Title 🇬🇧: Dandelion Sprout's Nordic filters for tidier websites
# Version: 11July2024v1-Deprecated
: expires = 18 hours
# Lisens   Licence: https://github.com/DandelionSprout/adfilt/blob/master/LICENSE.md
# Homepage: https://github.com/DandelionSprout/adfilt/blob/master/Wiki/General-info.md
# 🇳🇴: Denne listen dekker nettsteder for Norge, Danmark, Island, Færøyene, Grønland, Schleswig-Holsteins danske minoritet, og samebefolkningen. For mere informasjon, detaljer, hjelpemidler, og andre lister jeg har laget, gå til https://github.com/DandelionSprout/adfilt/blob/master/Wiki/General-info.md#norsk
# 🇩🇰: Denne liste dækker websider for Danmark, Norge, Island, Færøerne, Grønland, Sydslesvig, og den samiske befolkning. For mere information-, detaljer-, nyttige værktøjer- og andre lister, jeg har lavet, besøg https://github.com/DandelionSprout/adfilt/blob/master/Wiki/General-info.md#dansk
# 🇳🇴🏞: Denne lista dekkar nettstader for Noreg, Danmark, Island, Færøyane, Grønland, Schleswig-Holsteins danske minoritet, og samefolkesetnadene. For meire informasjon, detaljar, hjelpemiddel, og anna listar eg har laga, gå til https://github.com/DandelionSprout/adfilt/blob/master/Wiki/General-info.md#norsk-nynorsk
# Description: 🇬🇧: This list covers websites for Norway, Denmark, Iceland, Danish territories, Schleswig-Holstein's Danish minority, and the Sami indigenous population. For more information, details, helpful tools, and other lists that I've made, visit https://github.com/DandelionSprout/adfilt/blob/master/Wiki/General-info.md#-english
# Pretty important note: Documentation for TPL lists is atrociously bad, and often contradict themselves and omit important details. It wasn't until March 2020 that I discovered that TPL lists refuse to block first-party files, making more than half of this list useless, although it may have a slight effect on some newssites. If you just need a browser to play Flash games on, please switch to Waterfox Classic. If you have to use IE at work, you should either install AdGuard for Windows, or quit the job on the spot in protest against ancient technology.
# If you wish to remove cookie banners from Nordic websites, check out https://filters.adtidy.org/windows/filters/18.txt
# Starting 13 May 2024, reports about non-blocked banners on digi.no and tu.no must instead be sent to https://reports.adguard.com/new_issue.html/and/or/https://github.com/uBlockOrigin/uAssets/issues./No/exceptions/under/any circumstances. They're simply far, far better at them than me. They must either fix it on their own, or have written all needed entries on their own in advance before they forward such reports to me. If they ever say otherwise, show them this line of text.
# 🇳🇴: Fjerning av reklamebokser og tomme overskuddsbokser
# 🇩🇰: Fjernelse af annonceboxer og tomme overskudsrammer
# 🇬🇧: Ads and leftovers removal entries   Hiding-type rules
# — — — — — — — — —
# 🇳🇴: Oppføringer for minst 3 nettsteder
# 🇬🇧: Entries for at least 3 websites
- images banners
-d widgets.sprinklecontent.com
# — — — — — — —
# 🇳🇴: Brede eller heldomenebaserte blokkeringsoppføringer
# 🇬🇧: Broad or whole-domain blocking rules
-d dk ad
-d dk ads
-d is ad
-d is augl
-d is netbordar
-d is augl
-d no ad
- annonsar
- annonse_
- auglysing
- auglysingar
- vefauglysingar
-d ad.no.doubleclick.net
-d ad.shareholders.dk
-d adext.inkclub.com
-d adnordics.com
-d adserver.xh.no
-d adservice.com
-d adservicemedia.dk
-d banner.3loops.com
-d betterbanners.org
-d bilborsen.webannonse.no
-d boligkanalen-maestro-new.azurewebsites.net
-d cluster.chart.dk
-d delivered-by-madington.com
-d dotbanner.dk
-d easy-ad.no
-d easy-ads.dk
-d heartbeat.airserve.net
-d images.passendo.com
-d isweb.no
-d kunde.apt.no
-d kynning.olis.is
-d matriell.dm-storage.no
-d ndstage.wpengine.com
-d openad.visir.is
-d samfilm.codelab.is
-d sannsyn.com
-d static.airserve.net
-d tankeogteknikk.no
-d tracking-genesisaffiliates.com
-d vefbordi.is
-d vevlysingar.fo
-d videotool.fbg.dk
-d svindel.info
-d annoncer.nichehuset.dk
-d pliing.com
-d admob.no
-d admob.dk
-d print2web.sn.dk
-d lib.idg.no
# Adressa.no
-d drbrand.herokuapp.com
# bobilverden.no
- annonse-
# https://www.ballade.no/
- wp-content uploads *_Annonse_
- _toppbanner_
# https://www.osterud.name/FF57W10/norwegian-filters.txt
- bannerannonser
# byggenytt.no
- _annonser
# frende.no
-d api.frende.no log
# https://malviknytt.no/2020/07/31/skyting-pa-hjemmebande/ (16 08 2020)
- Nettbanner-
# sexpiger.dk
-d lh3.googleusercontent.com *=w468-h60-
-d lh3.googleusercontent.com *=w970-h250-
# salangen-nyheter.com, hytteavisen.no, strafferunden.no, langrenn.com (12 10 2020)
- getbanner.php
# biff.no (26 10 2020)
- _nettannonse.
- BINARY *-BANNER-*.gif
- BINARY *%20200x300.jpg
# nett.no (30 11 2020)
- byteads
# adressa.no (02 12 2020)
- polarnexus.js
# reavisa.no (06 12 2020)
- _nettbanner_
- _visittkortannonse_
- -visittkortannonse-
# ytresogn.no (16 12 2020)
- hnuannonse
# heilsutorg.is (17 04 2021)
-d is strevda
# fugleognatur.dk (14 05 2021)
- images bannere
# https://norges.online/produkt/nestle-viking-melk-410-g
-d fr135.net
-d static-dscn.net
# skagensavis.dk
- wp-content uploads i123_ads *.gif
- wp-content uploads i123_ads *_460x196.jpg
- wp-content uploads i123_ads 930x180_
# tv-kalundborg.dk
- system_files banner ckfinder
# keldan.is (05 01 2021)
- images augl
-d tac.is kunnar
# isolor.no (16 01 2021)
- -skyskraper-annonse.
# norskemagasinet.com (24 01 2021)
-d img.norrbom.com *-300x60.png
# vg.no (14 04 2021)
- gfx fishfingers
# xpresstryk.dk
-d images.staticjw.com casino24.jpg
# https://www.diabetes.no/mer/nyheter-om-diabetes/nyheter-2021/sporsmal-og-svar-om-koronavaksinen-og-diabetes/ (16 11 2021)
- globalassets banner_
# https://github.com/AdguardTeam/AdguardFilters/issues/114245#issuecomment-1085683154
-d no apx
# https://viivilla.no/hage/terrasse/slik-gjor-du-terrassen-festklar-til-17-mai-pa-1-2-3//(18/05/2023)
-d gcp.passendo.com
-d psscdn.com
# samferdselinfra.no (18 05 2023)
- wp-content uploads ad-html
# https://spurt.no/zyrtec-mot-myggstikk/ (01 06 2023)
- convertpro cp-popup.min.css
# https://www.version2.dk/artikel/medie-yngre-er-til-nemid-aeldre-til-mitid/(02/11/2023)
-d service.tekhus.dk *.jpg
# vilgernelevel.dk (25 12 2023)
-d skisverige.dk *banner_*.gif
# skessuhorn.is (29 12 2023)
-d app.pulsmedia.is
# https://bygge-anlaegsavisen.dk/historisk-vejprojekt-mellem-sisimiut-og-kangerlussuaq-undervejs/(30/12/2023)
-d s3.eu-west-1.amazonaws.com ads.
# https://www.minmote.no/interioer/gjoer-det-selv/a/EQBava/slik-faar-du-den-perfekte-uteplassen-til-vaarsesongen
# https://github.com/DandelionSprout/adfilt/discussions/932#discussioncomment-8408727
-d tize.no
# — — — — —
# 🇳🇴: Domenefokuserte blokkeringsoppføringer
# 🇳🇴🏞: Domenefokuserande bloknadsoppføringar
# 🇳🇴: Domænefokuserede blokeringsindførsler
# 🇩🇰: Domain-speficic blocking-entries
- gifs *emty.gif
- -banner_
- -bazaar-
- -l%C3%BDsing-
- 930x180_*.gif
- _bm abd
- Bannere
- banners
- bazaar
- bilder erotikk1.jpg
- entag.js
- js smartbanner
- liveodds-button_nordicbet
- mediaxpress ad
- nordicbet_logo
- partners *_ad_icon
- resources dfp
- tv2ads.js
- wp-content banners
- wp-content uploads *.gif
- wp-content uploads *bruktbilann*.jpg
- wp-content uploads *casino
- _300x250px-*.gif
- _300x500pix
- _930x180pix
- contentMarketing
- blob:https://www.veier24.no/
-d 1819.is infosmall
-d 730.no sonymusic
-d aa-cdn.mytaste.org ad.js
-d acdn.adnxs.com ast.js
-d acdn.adnxs.com ast.js
-d akamai.net
-d akamaihd.net
-d amino.dk 240x140-forside-hardcoded*.jpg
-d annoncelight.dk banner
-d appetitt.no *_1150x350*.jpg
-d appetitt.no *_Bannere_
-d appetitt.no *_widescreen_1920x1080_*.jpg
-d appetitt.no 1150*
-d appetitt.no 320x640-*.png
-d appetitt.no Annis.jpg
-d appetitt.no Topp-banner-*.jpg
-d arendalstidende.no *_490px.jpg
-d austevollforlag.no yachtmarine2014.
-d austurfrett.is *augl.jpg
-d ballade.no *Uke*_Sky
-d banner.landbrugsavisen.dk reklame.aspx
-d biip.no *320x250.jpg
-d bilbasen.dk GetVipFinanceBanner
-d bobilverden.no Banner-1200x300px.jpg
-d bornholm.nu banner
-d canariposten.no 300x1500*
-d cdn.rikstoto.no GameShop
-d check-in.dk *_930x180.gif
-d cms.sona.fo ads
-d danishfamilysearch.dk xp2
-d deals.innocode.no api
-d detailersclub.no *_banner.
-d dnitv.com
-d dust2.dk banners
-d erotikmix.dk mixads300.html
-d escort46.dk bg_images
-d export.prisguide.no
-d export.prisguiden.no
-d eyjar.net ads
-d fcbarcelona.dk footerbg.jpg
-d fcbarcelona.dk bcn_*.gif
-d feltet.dk topbanner_*.jpg
-d feltet.dk wallpaper_1.jpg
-d feltet.dk *_300x60.gif
-d footy.dk Sk%C3%A6rmbillede-*.png
-d forum.flyprat.no Header
-d frilansinfo.no *-annonse.jpg
-d gamer.no ?module=Tumedia\DFProxy\Modules
-d gaysir.no rek
-d gulindex.no spring.js
-d healthtalkweb.s3.amazonaws.com *_560x210.
-d hnytt.no Fluffy.jpg
-d i0.wp.com 180x500.png
-d img.sofabold.dk banner
-d indblik.net angwp
-d isolor.no *-toppbanner-
-d isolor.no *_480x150px.jpg
-d karfan.is *-470x130*.jpg
-d karfan.is *300x250.jpg
-d karfan.is *-vefbor%C3%B0i-
-d ksu247.no *-300x64.jpg
-d ksu247.no banner-*.jpg
-d ksu247.no BP-logo-*.png
-d ksu247.no Bunnpris2.jpg
-d leikjaland.is bannerstopright
-d leikjaland.is *logo.png
-d levmeddiabetes.no Accu-
-d magasinetreiselyst.no *_annonse*promo
-d malviknytt.no ani*-*.gif
-d malviknytt.no *-998x1024.jpeg
-d malviknytt.no *-firkant-*e1*.
-d mc-avisa.no Banner-*.jpg
-d media.sonymusic.no *.html
-d melkoghonning.no *_980x300px.jpg
-d melkoghonning.no *_Banner_
-d mmm.dk safeframe
-d n247.no salg
-d ni.dk *banner
-d nocc.no System_Promoteringssaker
-d nordlysid.fo lysing
-d norskenettsider.no ageras-banner.jpg
-d norskenettsider.no remember-banner-2016.jpg
-d nvnytt.no *annonse-
-d nyteknikk.no 180x
-d nyteknikk.no x150
-d oppdrettstorget.no cms
-d oyggjatidindi.com *L%C3%BDsing
-d r7.fo lysing
-d radiohallingdal.no abanners
-d radiorana.no *-300x300.jpg
-d radiorana.no Meyership.jpg
-d radiorana.no Telemix2.jpg
-d reavisa.blob.core.windows.net *-annonse-
-d reavisa.blob.core.windows.net *-NET.jpg
-d reavisa.blob.core.windows.net *-NETT.jpg
-d reavisa.blob.core.windows.net *_300x100
-d reavisa.blob.core.windows.net *_annonse_
-d reavisa.blob.core.windows.net *_NETT.jpg
-d reavisa.blob.core.windows.net *visittkort
-d reiseliv.no *-Annons%C3%B8rinnhold-*-Aksjer-*.
-d rett24.no inline
-d rett24.no*bannerizor.js
-d ridr.dk partners
-d s3-eu-west-1.amazonaws.com *-980x500-
-d s3-eu-west-1.amazonaws.com *-annonse-*.gif
-d s3-eu-west-1.amazonaws.com *-toppannonse-
-d s3-eu-west-1.amazonaws.com *.-jpg.jpg
-d s3-eu-west-1.amazonaws.com *.jpeg.jpg
-d s3-eu-west-1.amazonaws.com *nettannonse-
-d s3-eu-west-1.amazonaws.com nordbohus.gif
-d saernieh.no j%C3%B8rn-jensen.jpg
-d seksualitet24.no sinful_
-d semegleren.com video
-d skagensavis.dk annonceblok_baggrund.jpg
-d skagensavis.dk skagennet
-d smakmagasinet.no 170x500-
-d smakmagasinet.no 970x250-
-d spaniaidag.no Alltihus.jpg
-d spaniaidag.no Ceru-Design-Web-*.jpg
-d spaniaidag.no Kolstad-Gif-SI.gif
-d spanienidag.es patrocinadores
-d ssl.p.jwpcdn.com freewheel.js
-d ssl.p.jwpcdn.com jwpsrv.js
-d ssl.p.jwpcdn.com sharing.js
-d ssl.p.jwpcdn.com vast.js
-d static.finncdn.no FINNExternalDistribution.js
-d storfjordnytt.no *.jpg
-d storfjordnytt.no 26_hh.png
-d storfjordnytt.no *_bilsenter.jpg
-d storfjordnytt.no *_hovleriet.jpg
-d storfjordnytt.no *_muri.jpg
-d stream.fo *-300x111.jpg
-d teknologiskmatforum.no ViewImage.aspx?*width=343
-d thaiguiden.no tg-980.html
-d thainytt.no *-160.jpg
-d thainytt.no 160_*
-d track.adform.net Banners
-d track.adform.net
-d travservice.dk wp-content
-d trolli.is banner
-d trolli.is benecta.png
-d trolli.is Hollin_olafsfirdi
-d trolli.is syngjum-kubbur
-d trolli.is vefsmarinn
-d trolli.is videoval_logo
-d trolli.is *logo-*.png
-d trolli.is Untitled-1-1.jpg
-d tunnelsyn1.files.wordpress.com sotra-trelast-isolasjon
-d tv-kalundborg.dk banner
-d tv2.no sponsor
-d tvkampen.com banner*
-d tvkampen.com unibet-lo
-d utrop.no Banner_utrop
-d utrop.no utrop.no_-1.jpg
-d utvarpsaga.is *-bordi.jpg
-d utvarpsaga.is *_banner.png
-d vaktin.is grkuk
-d veitingageirinn.is haus20g.jpg
-d verktoy24.no Banner-*px.jpg
-d verktoy24.no *_300px-scaled.jpg
-d vf.is *2000x616.jpg
-d vf.is geysir-dekkjaskipti.jpg
-d elton.app widget
-d viasport-assets.mtg-api.com comScore-*.js
-d vikari.is frjalsi-lif*.png
-d viralefilmer.no *slot-
-d webforumet.no AD-*.jpg
-d webforumet.no *-250x250.jpg
-d www-presse-fotos-dk.filesusr.com
-d xklub.dk bannercache
-d xklub.dk banner
-d xn--bredbnd-ixa.dk velkommen_banner
-d youtube.com *&origin=https%3A%2F%2Fwww.feltet.dk&widgetid=1
-d yrkesbil.no 1pix.gif
-d ytresogn.no index.html
-d ytresogn.no *-copy.jpg
-d ytresogn.no *-Topbanner-
-d ytresogn.no *-1.jpg
-d ytresogn.no *-nett.jpg
-d ytresogn.no 128829765_1713260288837784_946999945581640675_n.jpg
-d ytresogn.no default_file-1607345037.png
-d ytresogn.no Fj.-Varmepumpe.png
-d ytresogn.no Fureli-nett-mobil.jpg
-d ytresogn.no image007.jpg
-d ytresogn.no Ytre_718_360_2.jpg
-d datamaskin.biz ad
# — — — — — — —
# 🇳🇴: Filtjener- eller nettstedsspesifikke oppføringer med kilder
# 🇳🇴🏞: Filtenar- eller nettstadsspesifikke oppføringar med kildar
# 🇩🇰: Filserver- eller webstedsspecifikke indførsler med kilder
# 🇬🇧: Fileserver or site-specific blocking rules with sources
# bilasolur•is (03 05 2020)
- lykill_banner
# bt•no
# https://newsbreak.dk/a01-problemer-hos-tdc-maaske-kan-du-ikke-ringe-01072020/
-d images.sprinklecontent.com *.amazonaws.com%2Fimages%
# https://github.com/AdguardTeam/AdguardFilters/issues/67358#issuecomment-724888304
-d gfx.no refererPromo
# buildingsupply•no, maskinregisteret•no, metalsupply•no, plastforum•no
-d f.nordiskemedier.dk *.gif
# building-supply•dk
-d f.nordiskemedier.dk banner
# metalsupply•no, licitationen•dk
# viivilla•no (10 11 2020)
-d bcm.interactives.dk script
# adressa•no (10 11 2020)
-d static.polarismedia.no cxense.js
# https://github.com/uBlockOrigin/uAssets/issues/13661/(11/06/2022)
-d freewheel-mtgx-tv.akamaized.net
# https://github.com/DandelionSprout/adfilt/issues/968
# https://github.com/DandelionSprout/adfilt/issues/983
# arto•dk
-d artodata.net ads
# — — — — —
# 🇳🇴: Generelle oppføringer med kilder
# 🇬🇧: Generic entries that have sources
# framtia.no, sovesten.no, arendalstidende.no, bil24.no, 730.no, frettatiminn.is, opp.no, melkoghonning.no
# Exceptions: ballade.no
# https://www.totensblad.no/2019/nyheter/forsynte-seg-gradig-av-medaljene-i-nm/
# arendalstidende.no
# https://www.langrenn.com/cppage.6250314-1743.html
# bobilverden.no
# norskenettsider.no, sva.no
# https://www.diskusjon.no/topic/1760306-ogs%C3%A5-onecall-lanserer-rollover-av-data/
# tv2.no
# https://kulturplot.no/synspunkt/2020/hva-er-malet-for-kultur-i-regionreformen
# https://www.dagbladet.no/mat/spaghetti--la-capri-italienerne-liker-sausen-men-n-ting-far-slakt---dette-er-ikke-pasta/67659821
# portal.fo (09 05 2020)
# jyllands-posten.dk
# buildingsupply.no, maskinregisteret.no, metalsupply.no, plastforum.no, retailnews.dk
# retailnews.dk (11 09 2020)
# n247.no
# healthtalk.no
# appetitt.no
# ekstrabladet.dk
# nab.no (Only shown if cookies are accepted; 18 08 2020)
# Bet365 widget triggered for Norwegian audiences only
# borsen.no (08 10 2020)
# https://www.nettavisen.no/3424050834.html/(24/11/2020)
# reavisa.no (06 12 2020)
# ytresogn.no (16 12 2020)
# nettavisen.no (25 12 2020)
# ao.no (28 12 2020)
# keldan.is (05 01 2021)
# madridista.dk (21 04 2021)
- banners casinotop
# gnavergalleri.dk (along with ~60 affiliates sites)
# https://github.com/DandelionSprout/adfilt/issues/233
# sol.dk (25 04 2021)
# bilgalleri.dk (25 04 2021)
# forum.ipmsnorge.org (24 05 2021)
# tipsbladet.dk (15 06 2021)
# sol.no (22 09 2021)
# vesterbroliv.dk, vafo.dk, amagerliv.dk
# https://github.com/uBlockOrigin/uAssets/issues/13224
# rett24.no (13 06 2022)
# metalsupply.no, licitationen.dk (08 03 2023)
# https://www.licitationen.dk/article/view/900259/efter_entreprenors_konkurs_river_106_ufaerdige_huse_ned_i_hojetaastrup/(08/03/2023)
# maskinregisteret.no (08 03 2023)
# eikernytt.no (18 05 2023)
# Various now-dead Frettabladid subdomains
# migogkbh.dk (22 06 2023)
# digitalt.tv (08 09 2023)
# h-avis.no (11 12 2023)
# skessuhorn.is (29 12 2023)
# sol.no
# www.qxl.no
# www.vtb.no
# vafo.dk
# reelligestilling.dk
# www.rbnett.no
# www.op.no
# journalisten.dk
# www.altomfotball.no
# dv.is
# bt.no
# latterkula.no se-streamerne-som-vinner-store-gevinster-mens-de-streamer-live
# www.latterkula.no artikler
# www.mbl.is frettir
# adressa.no
# https://nyheder.tv2.dk/2021-02-04-soennerne-saa-frem-til-en-arv-fra-deres-far-efter-mange-aars-lidelser-indtil-han-giftede/(04/02/2021)
# kk.no, sol.no
# (Exception: https://github.com/AdguardTeam/AdguardFilters/issues/58527)
# historienet.no, natgeo.no, komputer.no
# qxl.no
# gamer.no, veier24.no, at.no, porten.no, insidetelecom.no, elektronikkbransjen.no, tu.no, digi.no
# demokraten.no, avisa-hordaland.no, blv.no, gat.no, lp.no, osogfusa.no, raumnes.no, setesdolen.no, sunnhordland.no, vaksdalposten.no, vtb.no
# ba.no
# https://github.com/DandelionSprout/adfilt/pull/53
-d services.api.no bazaar
# aftenbladet.no
# avisalofoten.no
# blv.no nyheter kan-bruke-23-millioner-pa-the-whale-undersokelsene
# https://www.aftenposten.no/sport/sjakk/i/4qKxMg/carlsen-overbeviste-verdensmestertakter
# https://www.aftenposten.no/sport/sjakk/i/0nyKLG/sjakkstjernen-mistet-kona
# aftenposten.no (Mobile useragent)
# https://www.brannmannen.no/brann/store-utfordringer-ved-togulykken-pa-asta/
-d 85.17.76.181
# krs247.no
# lsk.no
# https://www.budstikka.no/
# e24.no, aftenbladet.no, sysla.no
# https://www.austurfrett.is/frettir/lagt-smithlutfall-a-austurlandi/(15/04/2020)
# https://fiskur.fo/gitte-henning-1-landar-i-maloy/(09/05/2020)
-d fo banner2x1.png
# https://www.dagsavisen.no/nyheter/verden/1.1731911/(18/06/2020)
# https://www.nordlys.no/egon-i-tromso-evakuert-tok-fyr-i-en-ovn/s/5-34-1326807/(10/07/2020)
# advokatbladet.no; https://gardsdrift.no/maskiner-potet-fagdag/folksomt-under-potato-scandinavia/185668/(16/08/2020)
# kimbino.no, kimbino.dk (13 09 2020)
# fasteignir.frettabladid.is (Exception: https://github.com/AdguardTeam/AdguardFilters/issues/111644)
-d via.placeholder.com
# lokal-avisa.no, ringsakern.no (19 09 2020)
# gjoviksblad.no (19 09 2020)
# midtjyllandsavis.dk, herningfolkeblad.dk, ikast-brandenyt.dk (30 09 2020)
# godstart.dk, sol.dk (30 09 2020)
-d ni.dk *-bottom.html
# fyens.dk, stiften.dk, jv.dk, dagbladet-holstebro-struer.dk, hsfo.dk (30 09 2020)
# https://www.nutiminn.is/menn-is/spilagaldur-ruglar-i-hausnum-thinum-varud-gaeti-fengid-thig-til-ad-trua-a-galdra-myndband/
# dagsavisen.no (30 05 2021)
# aftenposten.no, hockeymagasinet.dk, l-a.no, aftenbladet.no (30 10 2020)
# bt.no, byas.no, aftenbladet.no (30 10 2020)
# costume.no, costume.dk (09 11 2020)
# boligpluss.no (09 11 2020), women.dk
# ytresogn.no (16 12 2020)
- _980banner_
# ambulanseforum.no (26 12 2020)
# fyens.dk, faa.dk, stiften.dk, jv.dk, amtsavisen.dk, vafo.dk, viborg-folkeblad.dk, hsfo.dk, frdb.dk, folkebladetlemvig.dk, dbrs.dk, dagbladet-holstebro-stuer.dk, helsingordagblad.dk (02 01 2021)
# forum.doktoronline.no (06 01 2021), forum.klikk.no, forum.kvinneguiden.no
# nettavisen.no (20 01 2021)
# https://www.helsenett.no/spor-oss/har-du-smabarn/50657-svstadig-tilbakevendende-forkjolelsehostefeber.html/(10/02/2021)
# https://www.tronderdebatt.no/vet-regjeringen-at-det-bor-folk-langs-grensen-nord-i-trondelag/o/5-122-18453/(20/03/2021),/ba.no
# https://viralefilmer.no/norske-henry-78-kjopte-superbil-med-700-hestekrefter-til-43-millioner/ (25 03 2021), eavisa.no
# https://www.terrengsykkelforumet.no/ubbthreads.php?ubb=showflat&Number=2453543/(31/03/2021),/terrengsykkel.no
# nettavisen.no (04 04 2021)
# gnavergalleri.dk (along with ~60 affiliates sites; 21 04 2021)
# nidaros.no
# dagsavisen.no
# elbil24.no, vi.no (21 06 2021)
# farmatid.no (16 11 2021)
# https://radioh.no/norsk-opphenting-mot-nederland-sikret-vm-kvartfinale-storm-i-kastene/ (14 12 2021)
# nordlys.no, an.no (19 06 2022)
# nidaros.no (22 02 2023)
# jyllands-posten.dk (22 03 2023)
# forum.kvinneguiden.no (Mobile user agent; 05 04 2023)
# Various now-dead Frettabladid subdomains from 2020
# https://www.aftenposten.no/sport/fotball/i/QoP7KA/spansk-fotballstreik-fortsetter/(26/12 2023)
# e24.no (Mid-December 2023)
# — — — — — — —
# 🇳🇴: Oppføringer med spesielle omstendigheter
# 🇬🇧: Entries with special circumstances
+d vgtv.no
-d adnxs.com
-d samimag.no Screenshot-2020-03-21-at-12.40.32.png
# https://www.aftenposten.no/sport/i/kR20OL/uno-x-soeker-om-worldtour-lisens-en-droem-som-har-modnet-over-tid/(03/09/2022)
# Should not have ":not" + ":empty" added to it due to costume.no
# — — — — — — — — —
# 🇳🇴: Hovedsaklig for AdGuard
# 🇳🇴🏞: Huvudsakleg for AdGuard
# 🇮🇸: Aðallega fyrir AdGuard
# 🇬🇧: Mostly for AdGuard
-d 3.248.18.175
-d 35.227.231.163
-d 45.58.146.154
-d 82.196.13.38
-d 82.221.81.9
-d 178.79.136.45
# 🇳🇴 🇩🇰: ——— Sporingsfiler ———
# 🇳🇴🏞: ——— Sporingsfilar ———
# ❄: ——— Guorrafiilaid ———
# 🇬🇧: ——— Tracker files ———
# https://github.com/DandelionSprout/adfilt/pull/699
-d s.api.no *.gif
# https://github.com/uBlockOrigin/uAssets/issues/18880
# 🇳🇴: ——— Tomme skillebokser ———
# 🇩🇰: ——— Tomme adskillerbokser ———
# 🇳🇴🏞: ——— Tomme skiljeboksar ———
# 🇮🇸: ——— Tóma skilirammar ———
# 🇬🇧: ——— Empty divider spaces ———
# Was supposed to be synced often with https://raw.githubusercontent.com/DandelionSprout/adfilt/master/EmptyPaddingRemover.txt,/which/has/not been the case.
# 🇳🇴: ——— Distraherende bakgrunnsbilder ———
# 🇩🇰: ——— Distraherende baggrundsbilleder ———
# 🇮🇸: ——— Truflanda baksýnsmyndir ———
# 🇬🇧: ——— Distracting background images ———
-d images.media.xxlsports.com bg.jpg
-d platekompaniet.no background.png
-d pepcall.no bakgrunn-forside.jpg
-d tv2.no tv2-background.svg
# 🇳🇴: ——— Fiksing av knekte sider ———
# 🇩🇰: ——— Fiksing af knækte websider ———
# 🇮🇸: ——— Óbrot ———
# 🇬🇧: ——— Unbreakage ———
# Posten's new parcel tracker, fixes the form for giving them delivery information (doorbell name number)
# Makes articles that would be counted as ads anywhere else on SeHer, show up on that page.
# folkebladet.no; Makes job position lists show up correctly
+d stillingledig.*.no
# https://github.com/DandelionSprout/adfilt/issues/63#issuecomment-683430537
+d isdownorblocked.com
# https://github.com/DandelionSprout/adfilt/issues/63#issuecomment-689373261
-d prod-adops-proxy.dnitv.net
# Caused primarily by the site's tech incompetence, and merely secondarily by «uBlock Filters»
# ★★★ Caused by «EasyPrivacy» ★★★
# Attempting to fix a problem with voting online on Idol Norway
# Attempts to resolve how some frontpage articles are hard to open
# 🇳🇴: Får Discovery+ sin påloggingsside til å vises riktig
# 🇬🇧: Makes Discovery+'s login page show up properly
# https://github.com/easylist/easylist/issues/18542/(These/entries/are here to stay, regardless of the report's outcome.)
+d medlemskap.*.no
-d medlemskap.fagforbundet.no
# ★★★ Caused by «Fanboy's Social Blocking List», if I recall correctly ★★★
+d api.instagram.com
# https://github.com/ryanbr/fanboy-adblock/issues/1261
# https://github.com/easylist/easylist/issues/7805/(05/05/2021)
+d cookieinformation.com
# ★★★ Caused by «Fanboy's Annoyances List» and «EasyList Cookie List» ★★★
# https://github.com/ryanbr/fanboy-adblock/issues/1243
-d ktg-content.cdn.prismic.io *(my.newsletter_popup.uid
# https://github.com/ryanbr/fanboy-adblock/issues/1339
# https://github.com/ryanbr/fanboy-adblock/issues/1468
# https://github.com/easylist/easylist/issues/12067#issuecomment-1132797711
# https://github.com/easylist/easylist/issues/15519
# ★★★ Caused by «Fanboy's Enhanced Blocking List» ★★★
# https://github.com/DandelionSprout/adfilt/discussions/779#discussioncomment-5962141
+d vg.no
# ★★★ Caused by «EasyList» ★★★
+d _prebid_
@@://billink*.blob.core.windows.net/*/annonser
# https://raw.githubusercontent.com/hkarn/scandinavianlist/master/scandinavianlist/scandinavianlist_whitelist.txt
# Forum feeds in the upper right of articles
# Makes 1p info banners show up correctly
+d _980x100.
# Makes most links show up correctly (Fixed in AdGuard Base)
# https://github.com/uBlockOrigin/uAssets/issues/11546/(Not/yet/forwarded to EasyList)
# https://github.com/uBlockOrigin/uAssets/issues/13907
@@://imasdk.googleapis.com/js/sdkloader/ima3.js
# http://sosialurin.fo/news-detail/steypafinala-vilhelm-og-rogvi-a-ruv1-fra-klokkan-1630
# ★★★ Caused by «I Don't Care About Cookies» (Its maintainer couldn't reproduce it) ★★★
# Fullpage uncloseable overlay when browsing around on Telenor Norway's TV section
# ★★★ Caused by «AdGuard Annoyances Filter» and «AdGuard Tracking Protection Filter» ★★★
# (Currently empty.)
# ★★★ Caused by «AdGuard Popups Filter» ★★★
# ★★★ Caused by «Schacks Adblock Plus liste» ★★★
# https://github.com/ryanbr/fanboy-adblock/issues/1410
# ★★★ Unknown cause ★★★
# https://github.com/DandelionSprout/adfilt/issues/67
# https://new.reddit.com/r/uBlockOrigin/comments/gye2f2/cant_watch_videos_on_a_specific_website_with/ft9zlse/
+d notice.sp-prod.net
+d sp-prod.net
!
# 🇳🇴: Anti-'CPU-massakrering'
# 🇮🇸: And-örgjörvislatrun
# 🇬🇧: Anti-'CPU slaughtering'
# 🇳🇴: ——— Norsk Tipping, inkl. tvilsomt motiverte lottoreklamer (Noen ikke-påtrengende tippereklamer er greit nok i mine øyne) ———
# 🇩🇰: ——— Norsk Tipping, inkl. nogle tvivlsomt motiverede lottoreklamer (Nogle ikke-påtrængende sportstipsreklamer er akseptabelt i mine øjne) ———
# 🇳🇴🏞: ——— Norsk Tipping, inkl. tvilsamt motiverte lottoreklamar (Ein håndfull ikkje-påtrengande tippereklamar er i orden for meg) ———
# 🇬🇧: ——— Norsk Tipping, incl. poorly motivated lotto ads (A few non-pushy football pool ads are fine in my book) ———
-d widget.tippebannere.no
-d tipster.no embed
# https://www.nettavisen.no/
# https://www.ba.no/s/5-8-1221171
- pustehullet betting-header.png
-d norsktippingpartner.no
+d oddstips.norsktippingpartner.no
-d cloudfront.net Liveoddsen.aspx
- cloudfront.net oddsen
# nidaros.no (02 12 2021)
# h-avis.no (11 12 2023)
# https://github.com/DandelionSprout/adfilt/discussions/932#discussioncomment-7794535
# https://github.com/DandelionSprout/adfilt/discussions/932#discussioncomment-7865350
# https://www.nettavisen.no/sportspill/her-er-tallene-som-vil-fa-liverpool-fansen-i-godt-humor/s/5-95-1529066
# 🇳🇴: Oppføringer for ytre-høyre-nettsteder. Støtte for disse nettstedene er begrenset, og de fleste nye oppføringer som blir foreslått for dem vil bli ordrett godkjent.
# 🇮🇸: Skráningar fyrir ytrihægri-vefsiður. Stuðningur við þessar síður er takmarkaður, og flestar nýjar skráningar sem mælt er með fyrir þær verða innifalin orðrétt.
# 🇬🇧: Entries for far-right websites. Support for these sites is limited, and most new entries that are suggested for them will be accepted verbatim.
# https://github.com/uBlockOrigin/uAssets/issues/16138
# https://github.com/ryanbr/fanboy-adblock/issues/1405
# 🇳🇴: Falske innlastinger som sløser bort tid
# 🇩🇰: Falske indlastinger, der søler bort tid
# 🇬🇧: Fake loading screens that waste time
# adressa.no (02 12 2020)
-d collector.schibsted.io
# "Generic Hide"
+d bondebladet.screen9.tv
+d eurosport.no
+d eurosport.dk
# Fixed in better ways in AdGuard Base and uBlock Filters, but is needed for ABP
+d inputmag.dk
# 🇳🇴: Hvitelisteoppføringer for å unngå å trigge anti-reklameblokkeringstiltak (Slike hvitelistinger er fullt tillatt av Adblock Plus som det er meg bekjent)
# 🇬🇧: Allowlist entries to avoid triggering anti-adblock measures (Such allowlistings are fully allowed by Adblock Plus from what I'm aware of)
+d sixscissors.com
# https://github.com/AdguardTeam/AdguardFilters/issues/121422
# 🇳🇴: Oppføringer som også er tilstede i «AdGuards hovedfilter   AdGuard Base Filter», for de som bruker ABP og AdBlock, eller som ikke har tatt seg bryet å bruke 8 sekunder på å skru den på i uBlock Origin.
# 🇩🇰: Opføringer som også er tilstede i «AdGuard Basisfilter   AdGuard Base Filter», for de der bruger ABP og AdBlock, eller der ikke har tatt seg bryd at bruge 8 sekunder på at abonnere på den i uBlock Origin.
# 🇬🇧: Entries that are also present in AdGuard Base Filter, for those who use ABP and AdBlock, or who haven't felt a need to spend 8 seconds to subscribe to it in uBlock Origin.
# Starting with 10May2024v4, only entries from newer than #50000 in AdGuard Filters' issue section will be included in this section, to avoid very outdated entries.
-d freewheel-mtgx-tv.akamaized.net *.mp4
-d freewheel-mtgx-tv.akamaized.net
-d googletagservices.com gpt.js
-d img.sofabold.dk banner
-d v.fwmrm.net g
-d widget.tippebannere.no
-d widgets.sprinklecontent.com
# • Not to be removed during upstream syncs •
# https://www.avvir.no/samegiella-ja-mearkagiella-vuosttasgiellan/
# jyllands-posten.dk (09 07 2020)
# specificTXT
# 🇬🇧: Entries that are also present in «uBlock Filters», for those who use ABP and AdGuard
# ——————————————————————————————————————————————————————————————————————————————————————————
# 🇳🇴: Svindelnettsteder og virusnettsteder (Ikke besøk dem hvis du har dine datamaskiner og lommebøker kjært)
# Rask leksjon: Mange svindelnettsteder bruker adresser som ligner på adressene til store nettsteder, men som inneholder tilfeldige ekstra smådetaljer som gjør dem til en helt annen adresse. "||vg.no." vil blokkere vg.no.iphone-svindel-eksempel.xyz, men ikke vg.no eller vg.no sport
# 🇩🇰: Fupsider og virussider (Besøg dem ikke, hvis du sætter pris på dine computere og tegnebøger)
# 🇮🇸: Svindlsidur og vírussidur (Ekki heimsæk þeim ef þér líkar þinni tölvur og peningaveskur)
# 🇬🇧: Scam sites and virus sites (Do not visit them if you value your computers and wallets)
# Quick 101: Many scam sites use addresses that resemble those of major sites, but which contain random extra tidbits that make them a whole different address. "||vg.no." will block vg.no.iphone-scam-example.xyz, but not vg.no or vg.no sport
- begrensede-tilbudet
- bli-avbrutt-bor-du-oppdater
- dnb11111
- KiwiErbjudanden1
- Norgesecure
- pakkerlevering
- finn.no finno.htm
- gratis-reisebilletter.
-d 102.112.2o7.net
-d 52.216.146.90
-d 92.42.104.146
-d djurs.com-*.
-d itunesconnect-*.no
-d jimmychoostore.top
-d look-like-star.myshopify.com
-d marked.no
-d mrcal365.com
-d pensjonistferie.no
-d postuksus.com
-d replicapatekphilippe.com
-d replicarolexyachtmaster.com
-d secureriches.com
-d trackvoluum.com
-d tromselementbygg.no
-d ultimate-tech-products.myshopify.com
-d vipps-sikkerhet.
-d norskposten.com
-d oslo-tannlegene.no
-d y6.no
-d havfruen4220.dk
-d bankid-sperret.
-d srilanka.no
-d innboks.info
-d skaatteenok.com
-d pearlandcarpetcleaner.com
-d logg-inn.online
- ?finn.no login
# 🇬🇧: Copied over from «Dandelion Sprout's Anti-Malware List»
-d fredfiber.no
-d gogle.net
# 🇬🇧: Scam domains as reported in https://github.com/DandelionSprout/adfilt/issues/63#issuecomment-988127908
# https://www.tek.no/i/lVeQAe/
# https://www.nkom.no/aktuelt/ikke-trykk-pa-lenker-i-sms--for-du-er-helt-sikker/
-d eccolabgroup.com
-d galerijajava.ba
-d p-stn.net
# Fake Gymshark webshops
-d altrasgshoes.com
-d altrask.com
-d brunateskonorge.com
-d g-ymsharknorge.com
-d gantdanmark.com
-d gantnorge.com
-d gymshark-danmarkudsalg.com
-d gymshark-no.com
-d gymsharkbutikdanmark.com
-d gymsharkbutikkoslo.com
-d gymsharkdanmark.com
-d gymsharkidanmark.com
-d gymsharkiesale.com
-d xn--gymsharkklrnorge-3ob.com
-d gymsharkldanmark.com
-d gymsharklnorge.com
-d gymsharkno.com
-d gymsharknorge.com
-d gymsharkoutletsnorge.com
-d gymsharksalg.com
-d gymsharktightsnorge.com
-d gymsharnorge.com
-d hilfigerdenmark.com
-d hilfigernorge.com
-d hugobossbutikk.com
-d hunterstovlerbutikk.com
-d josefseibeloutletnorge.com
-d joyaskobutikk.com
-d kybunskodanmark.com
-d louboutinnorge.com
-d montec-danmark.com
-d montecnorge.com
-d montecsalg.com
-d nauticadanmark.com
-d nauticanorge.com
-d salgvejanorge.com
-d sanukdk.com
-d sanuksandaler.com
-d umbrodk.com
-d umbrono.com
-d underarmourdk.com
-d underarmourdks.com
-d vejadanmarkudsalg.com
-d xeroshoes-danmark.com
-d xeroshoesdanmark.com
- -norgesalg.com
# E-mail tips
-d s.free.fr
-d trmff.wpengine.com
-d 212.27.60.108
# Overly dedicated E-mail spambots
-d wirexapp.africa.com
-d tachyoniums.eu.com
# https://github.com/DandelionSprout/adfilt/discussions/932#discussioncomment-9075749
# 🇳🇴: Som nevnt i diverse nyhetsartikler om svindelsider
# 🇩🇰: Som nævnt i diverse nyhedsartikler om fupwebsider
# 🇬🇧: As mentioned in various news articles about fraud sites
# https://www.tv2.no/nyheter/10493336/
-d rnbinance.com
-d brightertrade.com
# https://www.nrk.no/norge/1.14511067
# https://www.datahjelperne.no/verifiser-get-konto-falsk-mail/
# https://www.datahjelperne.no/gratulerer-du-har-vunnet-en-gave-mail-svindel/
-d liveshopdealz.com
# https://www.nrk.no/livsstil/1.14732503
-d elkjop*.club
# https://www.datahjelperne.no/sparebank1-kortet-ditt-er-blokkert-mail-phishing/
- css *sparebank1.no
# https://www.facebook.com/viralspiralen/posts/2494251397311027
-d addmoviesnow.com
# https://www.mm.dk/tjekdet/artikel/faarup-sommerland-advarer-mod-gratis-billetter-det-er-spam-og-fup
-d faarup.com-*.
-d com-dk.com
# https://www.mm.dk/tjekdet/artikel/det-er-fup-heller-ikke-denne-gang-giver-legoland-5-gratis-billetter-vaek
-d legoland.com-*.
# https://www.mm.dk/tjekdet/artikel/ogsaa-chili-klaus-maa-staa-model-til-falske-annoncer
-d hcliips.com
# https://www.nrk.no/troms/1.14788086
-d geometra-bologna.it
# https://www.nrk.no/nyheter/1.14793929
-d sky.gs
# https://www.online.no/sikkerhet/falsk-online-nettside
-d is-a-personaltrainer.com
# https://nyheder.tv2.dk/krimi/2020-02-11-politiet-advarer-mod-svindler-smser-forsoger-at-fa-billede-af-nemid
-d rigspolitiet.com
# https://www.faktisk.no/faktasjekker/vw8/erik-gikk-fra-arbeidsledig-til-millionaer-pa-8-uker
-d ocgadgets.com
-d ocgadgetss.myshopify.com
# https://www.mm.dk/tjekdet/artikel/fup-artikel-hun-er-tiltalt-for-millionsvindel-men-nu-pludselig-loesladt
-d ekstrabiadet.
# https://www.tv2.no/nyheter/11516670/
-d fintechnow*.buzz
-d wealthnews*.xyz
# https://www.datahjelperne.no/posten-informerer-deg-om-forsendelsen-din-mail-svindel/
-d newzeninfotech.com
# https://www.datahjelperne.no/skatteberegning-mail-svindel/
-d probenefit.net
-d ssbeveragedistribution.com
# https://www.datahjelperne.no/olav-thon-facebook-svindel/
-d euronews*.buzz
-d softwaredaily*.monster
-d stalknews*.buzz
-d goldupdates*.xyz
# https://www.datahjelperne.no/vipps-sms-svindel/
# https://www.datahjelperne.no/hvit-bjorn-river-kvinne-i-stykker-facebook-spam-oppdatert/
-d vidcopa.me
# https://www.adressa.no/pluss/nyheter/2020/08/26/Kristofer-Hivju-V%C3%A6r-s%C3%A5-snill-og-slutt-22527944.ece
-d smallrise.com
# https://www.datahjelperne.no/coop-du-har-fatt-nye-kuponger-mail-svindel/
-d offerleads.club
- cop-no index.htm
# https://www.datahjelperne.no/elkjop-kontaktforsok-mail-svindel/
-d bamboobotanica.com
- survey heldige
# https://www.datahjelperne.no/sparebank-1-din-tilganger-er-blokkert-svindel/
-d cionialessio.it
# https://www.dinside.no/okonomi/advarer-mot-falsk-facebook/72891041
# https://www.datahjelperne.no/norske-facebook-profiler-misbrukes-i-svindel/
-d sites.google.com truls-svendsen
-d signup-*vpns.com
# https://www.datahjelperne.no/telenor-din-faktura-mislyktes-svindel/
# https://www.datahjelperne.no/eurocard-falsk-epost-faktura/
-d valspe.com.br
# https://www.datahjelperne.no/eika-falsk-epost-svindel/
-d tekuon.com
# https://www.nrk.no/norge/1.15235615
- -sparebank1.*.net
# https://www.datahjelperne.no/er-det-deg-facebook-video-spam/
-d cinefique.com
# https://www.datahjelperne.no/posten-sms-svindel/
-d niupaiba.com
# https://www.adressa.no/pluss/nyheter/2021/03/30/Ser-du-hvilken-profil-som-er-ekte-23739076.ece
-d nordeninterior.weebly.com
# Googling Aksel Hennie (Results for prior week) in late July 2021
-d com vg.no
# Various Google results for 'jesper buch bitcoin'
-d fartuelt.dk
-d fancywoman.dk
-d privatedagplejere.dk
-d mxdesign.dk
-d bitcoinevolutionaustraliareview.com
-d irb.dk
-d ditsunde.dk
-d economywatch.com
-d superbinvest.com
-d marvelouskaunas.club
-d aktienboard.com
-d minklubshop.dk dk
# https://www.nrk.no/vestfoldogtelemark/1.15750360
-d dundeehills.group
# https://www.adressa.no/pluss/nyheter/2021/12/04/Posten-advarer-Vi-sender-ikke-slike-tekstmeldinger-24894483.ece
-d ozarkvillage.net
-d channawars.com
# https://www.vi.no/forbruker/ikke-trykk-pa-lenka-fra-skatteetaten/75666026
-d melding.link
# https://github.com/DandelionSprout/adfilt/issues/63#issuecomment-1114669106
-d cx nordea
-d cx sparebank
-d cx sbanken
# https://www.kode24.no/artikkel/75980495
-d campbell-living.com
# https://www.telia.no/kundeservice/mobil/malware-flubot-android/
-d wxqgx123.com
# https://dinside.dagbladet.no/mobil/ikke-la-deg-friste/76730599
-d k-yw.com
# https://dinside.dagbladet.no/okonomi/tusenvis-forsokt-lurt/76921148
-d a2ics.eu
-d smsb.co
# https://www.tv2.no/nyheter/innenriks/advarer-om-svindel-sms-sender-aldri-slike-henvendelser/16284207//(15/12 2023)
-d minklarna.
# https://github.com/DandelionSprout/adfilt/issues/747
- -norge.co.no
-d skechersskosalg-norge.com
-d dkgaborsneakers.com
-d haglofstilbud.com
-d fjallraventilbud.com
-d hitecskonorge.com
-d off-whitenorge.com
-d gaborskonorge.com
-d oofosnorgeoutlet.com
-d camperskonorge.com
-d eccoskonorge.com
-d clarksskonorge.com
-d off-whitedanmark.com
-d underarmourdanmarkdk.com
-d eccodanmarkwebbutik.com
-d clarks-dk.com
-d salomonoutletnorge.com
-d speedcrossnettbutikk.com
# https://github.com/DandelionSprout/adfilt/issues/748
-d salomomnorgeoutlet.com
-d jakkeshopdanmark.com
-d jakkeshopnorge.com
-d norge-adidas.com
-d tevanorgeshop.com
-d wolverineskonorge.com
-d hunternorge.co
-d hunternorgeno.com
-d norgeskotilbud.com
-d hokasnorgeno.com
-d vanssnorge.com
-d asoloskonorge.com
-d hokaonenorge.com
-d jordannorge.top
-d quiksilvernorge.com
-d hokanorgeno.com
-d drmdanmark.com
-d tevadanmarkshop.com
-d hunter-danmark.com
-d salomonbutikdanmark.com
-d jordantilbud.com
-d jordantilbuddanmark.com
-d quiksilverdanmark.com
-d salomon-danmark.net
-d salomonidanmark.com
-d saucony-dk.com
-d palladiumskodk.com
-d keensandalertilbud.com
-d quiksilvertilbud.com
-d palladiumskobutikk.com
-d hunterstovlersalg.com
-d martenssalg.com
-d hokaskooutlet.co.no
-d hoka-sko.com
-d hoka-one-one.cc
-d hokaoneone*
# https://www.adressa.no/nyheter/trondheim/i/Moq2wR/svindlere-kaarer-vinnere-i-konkurranser-gir-en-daarlig-foelelse-aa-forklare-at-dette-bare-er-tull
# https://www.adressa.no/nyheter/trondheim/i/69d3lL/spisesteder-rammet-det-er-forferdelig-jeg-fikk-panikk
-d sitey.me
# https://www.tv2.no/nyheter/innenriks/olav-thon-misbrukes-i-svindelannonser-ble-feilaktig-meldt-dod/15818647/
-d 24-news.online
# https://www.tv2.no/nyheter/innenriks/advarer-ikke-klikk-pa-lenken/16040614/
-d brugerverificering.com
-d dhl-trackng.com
-d dnb-oppdater.
-d linkednordersalenavigate.com
-d mobilidentitet.com
-d mobiltrygheden.com
-d mobilunderskriv.com
-d no-aut.co
-d no-bekreft.com
-d no-confir.com
-d no-erne.com
-d no-erne.live
-d no-nye.live
-d no-renovere.com
-d no-sikkerhet.com
-d no-update.live
-d no-updater.live
-d start-myaltinn.com
-d no-forny*
-d my-altinn*
-d no-oppdatere.
-d no-oppdatert.
-d 179.43.189.62
# https://github.com/DandelionSprout/adfilt/discussions/932#discussioncomment-7694946
-d easypark-
-d 74.119.239.234
-d 162.241.194.206
# IP addresses of servers notorious for hosting many of the sites above
-d 51.195.133.131
-d 66.206.3.34
-d 82.118.242.69
-d 136.243.73.30
-d 138.201.126.227
-d 156.236.126.173
-d 196.196.230.76
-d 167.71.49.177
-d 134.209.82.119
-d 154.213.16.136
-d 158.247.212.220
-d 165.227.168.212
-d 132.148.220.142
-d 104.160.10.
-d 165.231.154.
-d 167.99.196.225
# https://github.com/DandelionSprout/adfilt/discussions/932#discussioncomment-7872103
-d betzykrisesenter.no
-d citra2010oslo.no
-d digiter.no
-d easydisplay.no
-d kjaerra.no
-d kontrast1.no
-d norskmatkultur.no
-d norskoffroadteknikk.no
-d nyematoghelse.no
-d securmarksykkel.no
-d thecoolgirl.no
-d topshineauto.no
-d vossblues.no
-d yttersiden.no
# https://github.com/DandelionSprout/adfilt/discussions/932#discussioncomment-7873648
-d monetrizer*.
-d 38.180.96.244
# 🇳🇴: Falske nett-"butikker" som er så dårlige, at de står oppført på Forbrukertilsynet egen svarteliste.
# 🇩🇰: Forbrukertilsynets black-list over falske netbutikker (Norges svar på Forbrugerombudsmanden).
# 🇬🇧: Fake and fraudulent web-"stores" that are so bad, that they're listed on the blacklist of the Norwegian state-sponsored Consumer Authority.
# Source: https://www.forbrukertilsynet.no/netthandel/falske-nettbutikker.
-d adidasko.com
-d airmaxskobillige.com
-d assassinfitness.com
-d coralls.com
-d daradis.com
-d drakternorge.com
-d drcarolyngroff.com
-d dunjakke-no.com
-d fotballsko-salg.com
-d gsport.com
-d hernoclothing.com
-d jakkesalgs.com
-d jakkesnorge.com
-d linkshe.com
-d mbtnorge.com
-d moteshoes.com
-d mycraftypad.com
-d norfotball.com
-d norgefotball.com
-d norgeshoes.com
-d oflike.com
-d parajumperssalg.com
-d pjs.outlet.com
-d popeurope.com
-d um-bs.com
# 🇬🇧: Pirate-product-selling stores registered by the serial scammers who go by the name of "xiang dao xin xi ji shu you xiang gong si".
-d nofotballshop.com
-d nofotballstore.com
-d nodrakts.com
-d dkfodboldstore.com
-d vmfodboldtoj.com
-d 5.39.217.206
-d 5.39.221.180
-d 193.148.70.153
# 🇳🇴: Falske nettapoteker
# 🇬🇧: Fake online pharmacies
- -med.footeo.com
-d *medisin*.over-blog.com
-d godtdsamaritansk.com
-d helsehjelp.over-blog.com
-d jensapoteker.com
-d marson.footeo.com
-d sikkertapotek.com
-d sobrilleverandoridanmark.wordpress.com
-d xanax*.over-blog.com
# 🇬🇧: Old domains stolen by casino sites
-d kohlershop.dk
-d fredensborg-orredfiskeri.dk
-d informationer.nu
-d cphspaogwellness.dk
-d webavisen.gl
# 🇬🇧: Copied over from DNS-BH Malware Domains and verified to actually be malicious (as that list has a whole lot of false positives)
-d desidert.no
-d brigitteheilmann.dk
-d storustovu.dk
-d campingnews.dk
# 🇬🇧: Copied over from URLHaus and verified
-d hagebakken.no
-d mdb.nu
-d idj.no
-d 1.14.61.188
-d smarthouseforum.ru
-d trafikkskoleapp.no
# Last updated: 20June2024v2-Extension
# 🇳🇴: ——— Vindusviskere for betalte artikler (sånn at de nederste linjene i en forhåndsvisning ikke toner ut) ———
# Takk til THEtomaso (https://github.com/THEtomaso)/for/de/fleste/av/disse/oppføringene.
# 🇩🇰: ——— Vinduesviskere for betalte artikler (så de sidste par linjer i en forhåndsvisning ikke falder ud) ———
# Tak til THEtomaso (https://github.com/THEtomaso)/for/de/fleste/af/disse/regler.
# 🇬🇧: ——— De-blurrers for paid articles (so that the last few lines of a preview doesn't fade out) ———
# Thanks to THEtomaso (https://github.com/THEtomaso)/for/most/of/these/entries.
-d dagligvarehandelen.no veil.png
# 10 02 2024
# https://github.com/DandelionSprout/adfilt/discussions/932#discussioncomment-8603702
# dagbladet.no,elbil24.no
# digi.no, tu.no, medier24.no, porten.no
# https://www.klikk.no/side3/vimenn/viggo-bloffet-hele-norge-6857944
# https://www.vg.no/nyheter/i/y3Mka2//(08/04/2020)
# https://www.vg.no/nyheter/innenriks/i/3JbRzv/ (09 04 2020)
# 🇳🇴 🇩🇰: ——— Anti-anti-reklameblokkering ———
# 🇮🇸: ——— And-and-auglýsingshindrun ———
# 🇬🇧: ——— Anti-anti-adblocking ———
-d elderlyscissors.com
# Also fixed in "uBlock Filters - Privacy", but is added to this list as well, because it serves to remove AAAB notices on various pages (especially when "uBlock Filters" is turned on).
-d googletagmanager.com gtm.js
# aftenposten.no, abcnyheter.no, recordere.dk, gastrofun.dk, fyens.dk, tilbudsuken.no, viborg-folkeblad.dk, gaffa.dk, jv.dk
# https://github.com/uBlockOrigin/uAssets/issues/8648
# https://github.com/finnish-easylist-addition/finnish-easylist-addition/issues/305
# https://www.findroommate.dk/vaerelser/302142/stort-lyst-vaerelse-taet-paa-aarhus-i-viby-centrum/(17/12/2021)
# https://github.com/uBlockOrigin/uAssets/issues/13495
# The green "Abonner" button in the upper right appears to work perfectly even with this entry, and the entry does not cause the Plus article bodies to appear either, so I feel I'm on safe enough grounds on this one.
-d piano.io execute
# 🇬🇧: ——— Not actually AAB, but would've caused fatal breakage in ABP ———
!¤=☆=¤=☆=¤=☆=¤=☆=¤=☆=¤=☆=¤=☆=¤=☆=¤=☆=¤=☆=¤=☆=¤=☆=¤!
# 🇳🇴 🇩🇰: ——— Ikke for Brave Browser ———
# 🇬🇧: ——— Not for Brave Browser ———
# Last updated: 09February2022v1-Extension
# https://github.com/brave/adblock-lists/issues/768/(Remove/when/Shield Standard Mode adds support for cosmetic filtering in default lists)
