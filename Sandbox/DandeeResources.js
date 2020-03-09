/// ghhbd.js
// ==UserScript==
// @name        Google Hit Hider by Domain (Search Filter / Block Sites)
// @author      Jefferson "jscher2000" Scher
// @namespace   JeffersonScher
// @version     2.1.2
// @copyright   Copyright 2020 Jefferson Scher
// @license     BSD-3-Clause
// @description Block unwanted sites from your Google, DuckDuckGo, Startpage.com, Bing and Yahoo search results. v2.1.2 2020-01-26
// @include     http*://www.google.*/*
// @exclude http*://www.google.com/recaptcha/*
// @include     http*://www.google.co*.*/*
// @include     http*://news.google.*/*
// @include     http*://encrypted.google.*/*
// @include     http*://startpage.com/*
// @include     http*://*.startpage.com/*
// @exclude https://www.startpage.com/*/ads?*
// @include     http*://duckduckgo.com/*
// @include     http*://start.duckduckgo.com/*
// @include     http*://safe.duckduckgo.com/*
// @include     http*://3g2upl4pq6kufc4m.onion/*
// @include     http*://www.bing.com/*
// @include     http*://*search.yahoo.com/*
// @include     http*://search.yahoo.co.jp/*
// @include     http*://www.yandex.com/*
// @include     http*://yandex.com/*
// @include     http*://searx.*/*
// @include     http*://www.qwant.com/*
// @include     http*://www.qwantjunior.com/*
// @include     http*://www.baidu.com/*
// @include     https://www.ecosia.org/search*
// @grant       GM_getValue
// @grant       GM.getValue
// @grant       GM_setValue
// @grant       GM.setValue
// @grant       GM_registerMenuCommand
// @grant       GM_deleteValue
// @grant       GM.deleteValue
// @grant       GM_getResourceURL
// @grant       GM.getResourceUrl
// @resource    mycon https://www.jeffersonscher.com/gm/src/gfrk-GHHbD-ver212.png
// ==/UserScript==
var script_about = "https://greasyfork.org/scripts/1682-google-hit-hider-by-domain-search-filter-block-sites";
/*
Copyright (c) 2020 Jefferson Scher. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met and subject to the following restriction:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

var GM4 = (typeof GM_getValue === "undefined") ? true : false;
function GHHbD_addStyle(txt){
  var s=document.createElement('style');
  s.className = 'GHHbDcss';
  s.appendChild(document.createTextNode(txt));
  document.body.appendChild(s);
}
var isch = false;
function injectBaseCSS(){
  // == == == To override the style of the script's buttons and panes, use the custom style feature == == ==
  GHHbD_addStyle("div.ghhider{color:#888;} div.ghhider:hover{background-color:#eee;} " +
            "button.ghhider{color:#555;background-color:#fcfcfc;font-family:sans-serif;font-size:0.85em;margin:auto 2px;border:1px solid #ccc;border-radius:4px;padding:2px 3px;} h3>button.ghhider{font-size:0.75em;} " +
            "button.ghhider:hover{color:#000;background:#ff8;} .ghh1time{background:#eee !important;} .ghhdnone{display:none !important;} " +
            ".ghhpane{position:absolute;color:#333;background-color:#fcfcfc;border:1px solid #ccc;border-radius:4px;padding:0.25em 1.5em;font-size:13px;display:none} " +
            "#ghhsitelist, #ghhpbanlist{background:#fff;list-style-type:none;padding:0;margin:0;} " +
            "#ghhsitelist li,#ghhpbanlist li{width:100%;line-height:1.5em;padding:0;position:relative} " +
            "#ghhsitelist li:nth-of-type(odd),#ghhpbanlist li:nth-of-type(odd){background-color:#fcfcaa} " +
            ".ghhhost{display:block;padding:0 0.25em;cursor:pointer;} #ghhutil{text-align:center;margin:0.5em 0 1em 0;border:1px solid #ccc;border-radius:4px;padding:3px 0;} " +
            ".ghhinfo{font-size:12px;line-height:9px;position:absolute;top:0;right:0;z-index:1001;border:4px solid transparent;border-radius:4px;border-bottom-left-radius:8px;border-top-left-radius:8px;margin-top:1px;padding-left:1px} " +
            ".ghhdel{text-decoration:line-through;color:#333;} .ghhpb{text-decoration:none;color:#f00;} " +
            ".ghhblk{text-decoration:none;color:#333;} .ghhd{position:relative;line-height:1.2em;cursor:pointer;} " +
            ".ghhindent{position:absolute;left:350px;top:-3px;} #btnedit p{margin:2px 4px 4px 4px;} #ghhblockform input[type='radio'], #ghhmngform input[type='radio']{vertical-align:bottom;margin-top:5px;margin-bottom:1px} " +
            "#ghhblockform label, #ghhmngform label{display:inline;font-weight:normal} .ghhtbl{border:1px solid black;border-collapse:collapse} .ghhtbl td, .ghhtbl th{border:1px solid black;padding:2px 4px;} " +
            "#ghhtsdiv{margin:0 -1.5em;padding:0 3px 0 8px;border-bottom:1px solid #ccc;} #ghhtstrip{padding-bottom:0;} " +
            "#ghhtstrip button{color:#555;background-color:#f5f5f5;margin:0 2px 0 0;border:1px solid #ccc;padding:1px 2px;height:22px;border-radius:2px;} " +
            "#ghhtstrip .ghhCurTab{background-color:#fcfcfc;border-bottom-color:#fcfcfc;} .ghhtab {margin-top:1em;height:17em;overflow-y:scroll;border:1px solid #333;} " +
            "#mflists>div>p{margin:1em 0;} #ghhmngform{position:fixed;top:65px;right:0;z-index:9001;text-align:left;line-height:1.2em} #ghhblockform{text-align:left;z-index:3005} " +
            'h3[wotdonut="true"]{overflow:visible!important}');
  GHHbD_addStyle("@media print {button.ghhider{display:none;}}");
  // Standard image results style block
  if (location.search.indexOf("tbm=isch") > -1){
    var ghhbd_imgsty = document.createElement("style");
    ghhbd_imgsty.id = "ghhStyleImgResults";
    ghhbd_imgsty.setAttribute("type", "text/css");
    ghhbd_imgsty.appendChild(document.createTextNode('div[imgblock="regular"] img{opacity:0.1 !important} div[imgblock="regular"] a div{display:block !important;opacity:0.6 !important} div[imgblock="regular"] img:hover{opacity:0.5 !important} div[imgblock="pban"]{background-color:#aaa !important;border-radius:6px !important} div[imgblock="pban"] a{display:none !important}'));
    document.body.appendChild(ghhbd_imgsty);
    isch=true;
  }
}
injectBaseCSS();

var currentG = location.hostname; var engine = 'misc';
function doSiteSpecific(){
    if (currentG.indexOf("google") > -1){
        engine = 'Google';
        // Google: div#res > div#search > div > div#ires > div.srg | ol#rso | div._NId | div.bkWMgd > div.g > div.rc > h3.r > a
        // Google in-depth articles: div#res > div#search > div#ires > ol#rso > div > li.g.card-section or li.g.ct-cs > div.rc > div > h3.r > a
        // Google Images (default): div#res > div#search > div > div#ires > div#rso > div#isr_mc > div > div#rg > div#rg_s > div.rg_di.rg_el.ivg-ig > a > img
    }
    if (currentG.indexOf("bing.com") > -1){
        engine = 'Bing';
        // Bing: div#b_content > main > ol#b-results > li.b_algo > h2 > a
        GHHbD_addStyle("li[ghhresult] h2 button.ghhider{font-size:0.7em !important;} li > h2 {white-space:nowrap !important;}");
    }
    if (currentG.indexOf("duckduckgo") > -1 || currentG.indexOf("3g2upl4pq6kufc4m") > -1){
        engine = 'DDG';
        // DuckDuckGo: div#links > div.results_links_deep > div.links_main > h2 > a
        GHHbD_addStyle(".links_main,.result__title{overflow:visible !important;} .result__title{white-space:nowrap !important;} .ghhb{font-size:12px!important;margin-left:4px!important;}");
    }
    if (currentG.indexOf("startpage") > -1){
        // Startpage: div#results > ol > li > div.result > h3 > a
        // 11/21/2018: [data-view="results"] div.columns article.column.column--main > div.column.column--main__content > ol.list-flat > li.search-result.search-item > h3.search-item__title > a
        //  7/03/2019: div.mainline-results__web section.w-gl > div.w-gl__result > a.w-gl__result-title
        GHHbD_addStyle('.w-gl__result{overflow:visible !important;} .ghhd{padding:0 10px 8px 12px}button.ghhider{font-weight:normal}#ghhblockform input[type="checkbox"], #ghhmngform input[type="checkbox"]{width:unset;height:unset;position:static;margin:unset;border:unset;padding:unset;clip:unset;}' +
                      '#ghhblockform button, #ghhmngform button{font-size:1em;font-weight:normal;border:1px solid #e3e3e3;border-radius:3px;padding:2px 8px;box-shadow:none}');
    }
    if (currentG.indexOf("yahoo.com") > -1){
        // Yahoo (Firefox): div#results > div#cols > div#left > div > div#main > div > div#web > ol > li > div > div > h3 > a
        GHHbD_addStyle("div#web > ol.reg, li div.compTitle {overflow:visible !important;} .ghhd{margin: 1em 0px -1em 10px} #ghhmngform{top:80px} li div div h3{white-space:nowrap !important;}");
    }
    if (currentG.indexOf("yahoo.co.jp") > -1){
        // Yahoo Japan: div#contents > div > div > div > div#WS2m > div.w > div.hd > h3 > a
        GHHbD_addStyle("#WS2m .w{overflow:visible !important;} #ghhmngform{z-index:3001}");
    }
    if (currentG.indexOf("baidu") > -1){
        engine = 'Baidu';
        // Baidu: (title) #content_left > div.result.c-container > h3 > a; (domain) #content_left > div.result.c-container > div > a.c-showurl
        // Baidu rich result: (title) #content_left > div.result-op.c-container > h3 > a (or p.op_site_domain_title, div.op_generalqa_main.c-row); (domain) #content_left > div.result-op.c-container[mu]
    }
    if (currentG.indexOf("yandex.com") > -1){
        // Yandex: div.serp-list | ul.serp-list > div.serp-item | li.serp-item > h2 > a
        GHHbD_addStyle("h2.serp-item__title{white-space:nowrap;}.ghhb{font-size:0.75em!important;margin-left:4px!important;}");
    }
    if (currentG.indexOf("qwant") > -1){
        // Qwant: div.results-column > div.result_fragment > div.result--web | div.result--news > h3 > a
        GHHbD_addStyle("div[blocknotice]:not(.ghh1time){min-height:1em;padding-left:0;}");
    }
    if (currentG.indexOf("searx") > -1){
        // Searx.me: div#main_results > div.result > h4.result_header > a
        GHHbD_addStyle("h2.serp-item__title{white-space:nowrap;}.ghhb{font-size:0.75em!important;margin-left:4px!important;}");
    }
    if (currentG.indexOf("ecosia") > -1){
        engine = 'Ecosia';
        // Ecosia: div.results-wrapper > div.container.results ... div.card-web ... div.result-firstline-title > a.result-title
    }
}
doSiteSpecific()
//console.log('engine=' + engine);

function injectCustom(){
  if (custSty.length === 0) return;
  var ghhbd_custsty = document.createElement("style");
  ghhbd_custsty.setAttribute("type", "text/css");
  ghhbd_custsty.id = "ghhbdcuststy";
  ghhbd_custsty.appendChild(document.createTextNode(custSty));
  document.body.appendChild(ghhbd_custsty);
}

var custSty;
if (!GM4){
  custSty = GM_getValue("hiderStyles", "");
  injectCustom();
} else {
  GM.getValue("hiderStyles", "").then(function(value){custSty = value; injectCustom();});
}

// == == == Globals for preferences == == ==
var blist, defaultTxts, txtsPref, txts, defaultPrefs, ghhPrefs, ghhPrefO, showYN, mpopen, mbstyle, bbstyle, bbpos, addAt, listchgs, bLUopen, bAggress, bAJAX, bMutOb, pref1click, betatest, MutOb, chgMon, opts, kids, needupdate = true, doms = [];
var patIPv4 = /\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b/;

function checkblist(){
  if (blist.length === 0) blist = "|example.com:t|";
  if (blist.substr(0,1) != "|") blist = "|" + blist;
  if (blist.indexOf(":") < 0) convertFormat();
}

if (!GM4){
  blist = GM_getValue("hideyhosts", "");
  checkblist();
} else {
  GM.getValue("hideyhosts", "").then(function(value){blist = value; checkblist();});
}

defaultTxts = {
  "block":["block","Button next to the result title to call up the block dialog"],
  "unblock":["Unblock","Green button in results to remove a site from the block list"],
  "onetime":["Show Hit","Yellow button in results to show a result temporarily"],
  "pban":["Perma-ban","Red button to move a site to the perma-ban list"],
  "shownotc":["Show Notices","Button to set the preference for notices to show them"],
  "hidenotc":["Hide Notices","Button to set the preference for notices to hide them"],
  "okbtn":["Block Site","Button in the block dialog to block the selected domain"],
  "cancelbtn":["Cancel","Button in the block dialog to cancel out with making changes"],
  "savebtn":["Save Lists","Button in the management pane to update the block and perma-ban lists"],
  "closebtn":["Close","Button in the management pane to close the pane"],
  "okPbtn":["Perma-ban","Button in the block dialog to perma-ban the selected domain"],
  "cancelMbtn":["Manage Hiding","Button in the block dialog to open the management pane"],
  "mngbtn":["Manage Hiding","Button on the right side to open the management pane"],
  "eximbtn":["Export","Button in the management pane to export the block list"],
  "utilbtn":["List Util","Button in the management pane to open the utility panel"],
  "sortbtn":["Sort","Button in the management pane to sort the block list"],
  "unwwwbtn":["Un-www","Button in the management pane to strip www from blocked domains"],
  "dedupbtn":["De-Dup","Button in the management pane to de-duplicate the block list"],
  "impobtn":["Import","Button in the management pane to import domains into the block list"],
  "sharebtn":["Share","Button in the management pane to post block list to the web"],
  "addallbtn":["Add All","Button in the management pane to bulk add all unblocked domains to current list"]
};

function checktxts(){
  if (txtsPref.indexOf(":[") == -1 || txtsPref.indexOf("mngbtn") == -1 || 
      txtsPref.indexOf("eximbtn") == -1 || txtsPref.indexOf("utilbtn") == -1 || 
      txtsPref.indexOf("impobtn") == -1 || txtsPref.indexOf("addallbtn") == -1) {
    convertTxts(txtsPref);
  } else {
    txts = JSON.parse(txtsPref);
  }
}

if (!GM4){
  txtsPref = GM_getValue("textstrings", JSON.stringify(defaultTxts));
  checktxts();
} else {
  GM.getValue("textstrings", JSON.stringify(defaultTxts)).then(function(value){txtsPref = value; checktxts();});
}

defaultPrefs = {
  "shownotc":["Y","Show hit notices(Y|N)"],
  "mngpaneopen":["Y-N","Persistence enabled(Y|N),Pane was open(Y|N),Last tab number(1-4)"],
  "mngbtnstyle":["both-ifrN-R-P-Y-H","Display Manage Hiding button and Block buttons(mng|blk|both),In iframes(ifrN|ifrY),Position(R,T,B),Block button display(P,M),Block button tooltips(Y|N), Block button position(H|C)"],
  "addtolistpos":["end","Where to add new hits to block lists(end|top|sort)"],
  "aggressiveblock":["none","Which domains to default to shorter form(none|all|www)"],
  "usemutation":["on-Y","Listen for mutation events(on|off),Use DOM4 Mutation Observer(Y|N)"],
  "oneclick":["N-N","One-click blocking(Y|N),Goes to Perma-ban(Y|N)"],
  "runbeta":["N","Enable incompletely tested features (Y|N)"],
  "reserved2":["X","Y"]
};

function checkprefs(){
  if (ghhPrefs.length == 0){
    convertPrefs(defaultPrefs, "true");
  } else {
    if (ghhPrefs.indexOf("reserved1")>-1){
      convertPrefs(defaultPrefs, "false");
    } else {
      ghhPrefO = JSON.parse(ghhPrefs);
    }
  }
}

if (!GM4){
  ghhPrefs = GM_getValue("ghhprefs", "");
  checkprefs();
  GHHbDinit();
} else {
  GM.getValue("ghhprefs", "").then(function(value){ghhPrefs = value; checkprefs(); GHHbDinit();});
}

function GHHbDinit(){
  showYN = ghhPrefO.shownotc[0];
  mpopen = ghhPrefO.mngpaneopen[0];
  mbstyle = ghhPrefO.mngbtnstyle[0];
  if (mbstyle.split("-")[0] == "mng") toggleBlockHiders("H");
  if (mbstyle.split("-").length < 3){
    GHHbD_addStyle("#ghhMngBtn {position:fixed;top:150px;right:-2.8em;-moz-transform:rotate(-90deg);-webkit-transform:rotate(-90deg);"+
      "border-bottom:0;border-bottom-left-radius:0;border-bottom-right-radius:0;padding:6px 1px;z-index:1000;}");
  } else {
    switch (mbstyle.split("-")[2]){
      case "B":
        GHHbD_addStyle("#ghhMngBtn {position:fixed;bottom:0;right:2px;"+
          "border-bottom:0;border-bottom-left-radius:0;border-bottom-right-radius:0;padding:6px 1px;z-index:1000;}");
        break;
      case "T":
        GHHbD_addStyle("#ghhMngBtn {margin:0;padding:4px 6px;z-index:3000;}");
        if (document.querySelector("#appbar ol")){
          window.setTimeout(function(){document.querySelector("#appbar ol#ab_ctls").appendChild(document.getElementById("ghhMngBtn"))}, 1000);
          window.setTimeout(function(){var liNew = document.createElement("li");liNew.className="ab_ctl";liNew.appendChild(document.getElementById("ghhMngBtn"));document.querySelector("ol#ab_ctls").appendChild(liNew);}, 1500);
        } else {
          window.setTimeout(function(){if (document.querySelector("#appbar ol")){var liNew = document.createElement("li");liNew.className="ab_ctl";liNew.appendChild(document.getElementById("ghhMngBtn"));document.querySelector("ol#ab_ctls").appendChild(liNew);}else{document.getElementById("ghhMngBtn").setAttribute("style","position:absolute;top:8em;right:0")}}, 1500);
        }
        break;
      default:
        GHHbD_addStyle("#ghhMngBtn {position:fixed;top:150px;right:-2.8em;-moz-transform:rotate(-90deg);-webkit-transform:rotate(-90deg);"+
          "border-bottom:0;border-bottom-left-radius:0;border-bottom-right-radius:0;padding:6px 1px;z-index:1000;}");
    }
  }
  if (mbstyle.split("-").length > 3) bbstyle = mbstyle.split("-")[3];
  else bbstyle = "P";
  if (mbstyle.split("-").length > 5) bbpos = mbstyle.split("-")[5];
  else bbpos = "H";
  // toggleciteline(bbpos); called by fixuistyle()
  addAt = ghhPrefO.addtolistpos[0];
  listchgs = 0;
  bLUopen = "N";
  bAggress = ghhPrefO.aggressiveblock[0];
  bAJAX = ghhPrefO.usemutation[0].split("-")[0];
  if (ghhPrefO.usemutation[0].split("-").length > 1) bMutOb = ghhPrefO.usemutation[0].split("-")[1];
  else bMutOb = "Y";
  pref1click = ghhPrefO.oneclick[0];
  betatest = ghhPrefO.runbeta[0];
  if (document.body){
    // Add buttons, hide unwanted domains
    hidehits(null,false);
    var t_pb;
    if (document.getElementById("GTR")) removePBs();
    // Special results layout
    if (betatest == "Y"){
      var itbl = document.querySelector("#res .images_table");
      if (itbl) hidebasic(itbl);
    }
    // Create skeleton of manage form
    if (!document.getElementById("ghhmngform")) addManageForm();
    // Add manage button
    if (!document.getElementById("ghhMngBtn") && mbstyle.split("-")[0] != "blk"){
      if (engine == 'Google'){if(document.getElementById("res")) addMngBtn();}
      else addMngBtn();
    }
    // Show pane if last open
    if (mpopen.substr(0,3) == "Y-Y") showManageForm("mngform");
    // Add menu item - Legacy Only
    if (!GM4) GM_registerMenuCommand("Manage Hiding", showManageForm);
    // Create block form
    if (!document.getElementById("ghhblockform")) addBlockForm();
    // Watch for changes that could be new instant or AJAX search results
    if (bAJAX == "on") setMutationWatch();
  }
}

function setMutationWatch(){
  // Prefer MutationObserver (Firefox 14+) over Mutation Events
  MutOb = (window.MutationObserver) ? window.MutationObserver : window.WebKitMutationObserver;
  if (MutOb && bMutOb == "Y"){
    chgMon = new MutOb(function(mutationSet){
      mutationSet.forEach(function(mutation){
        if (mutation.type == "childList"){
          for (var i=0; i<mutation.addedNodes.length; i++){
            if (mutation.addedNodes[i].nodeType == 1){
              checkNode(mutation.addedNodes[i]);
            }
          }
        } else { // attribute mutation on Google Images
          if(mutation.target.className == "rg_l") checkNode(mutation.target.parentNode);
        }
      });
    });
    // attach chgMon to document.body
    if (isch == true) opts = {childList: true, subtree: true, attributes: true, attributeFilter: ["href"], characterData: false};
    else opts = {childList: true, subtree: true, attributes: false, characterData: false};
    chgMon.observe(document.body, opts);
  } else if (bMutOb == "Y") { // Legacy browser support and Baidu
    document.body.addEventListener("DOMSubtreeModified", checkOlist, false);
  }
}
// == == == Main Event Loops == == ==
var ignoreNodeNames = "|BODY|#text|#comment|INPUT|BUTTON|SCRIPT|LI|A|FORM|";
var ignoreIds = "|leftnav|leftnavc|foot|ghhtemp|ghhblockform|ghhmanageform|ghhsitelist|ghhpbanlist|rhs|rhscol|";
var ignoreClass = "|ghhider|ghhdbuttons|ghh1time|";
var t_ap, t_gimg;

function checkOlist(e){ // Check for new results // Needed for Baidu
  var el = e.target;
  // Ignore events on some elements
  if (ignoreNodeNames.indexOf("|"+el.nodeName+"|") > -1) return;
  if (el.hasAttribute("id")){if (ignoreIds.indexOf("|"+el.id+"|") > -1) return;}
  if (el.hasAttribute("class")){
    if (ignoreClass.indexOf("|"+el.className+"|") > -1) return;
    if (el.classList.contains("goog-date")) return;
  }
  if (!document.getElementById("ghhmngform")){
    addManageForm();
    injectBaseCSS();
    injectCustom();
    if (!document.getElementById("ghhMngBtn") && mbstyle.split("-")[0] != "blk"){
      if (engine == 'Google'){if(document.getElementById("res")) addMngBtn();}
      else addMngBtn();
    }
    // Use default button style for now (1.9.3)
    GHHbD_addStyle("#ghhMngBtn {position:fixed;top:150px;right:-2.8em;-moz-transform:rotate(-90deg);-webkit-transform:rotate(-90deg);"+
                   "border-bottom:0;border-bottom-left-radius:0;border-bottom-right-radius:0;padding:6px 1px;z-index:1000;}");
  }
  checkNode(el);
}
function checkNode(el){
  if (el.parentNode && (el.parentNode.id == 'ghhsitelist' || el.parentNode.id == 'ghhpbanlist')) return; // 2.0.6 duh!
  // AutoPager extension
  if (document.querySelector("#navcnt")){
    if (t_ap) window.clearTimeout(t_ap);
    t_ap = window.setTimeout(refreshListeners, 500);
  }
  if (el.nodeName == "LI" || (el.nodeName == "DIV" && (el.className == "g" || el.classList.contains("rg_di") || el.className == "rgsh")) || 
      el.nodeName == 'G-INNER-CARD' || el.nodeName == 'G-CARD') var nlist = [el];
  else var nlist = el.querySelectorAll('li.g, div.g, div.rg_di');
  if (engine != 'Google' && el.nodeName != "LI"){
    if (el.nodeName == "DIV" && (el.classList.contains("result--web") || el.classList.contains("result--news") || el.className == "card-mobile")) var nlist = [el]; // Qwant, Ecosia
    else var nlist = el.querySelectorAll('div.result, div.result-op, div.links_main, div.serp-item, div.hd, li.b_algo, ol.list-flat > li, div.card-web div.card-mobile');
  }
  if (nlist.length > 0){
    if (isch) hidehits(nlist,true);
    else hidehits(nlist,false);
    if (document.getElementById("GTR")) removePBs();
  } else {
    if (el.nodeName == "DIV" && ( (el.classList.contains("irc_c") || el.classList.contains("irc_bg")) || el.id == 'irc_bg') ) {
      var buttondivs = el.querySelectorAll('.irc_butc:not([ghhresult]), .irc_but_r:not([ghhresult]), .irc_ab:not([ghhresult]), .irc_but_pdfr:not([ghhresult])');
      for (var k=0; k<buttondivs.length; k++){
        buttondivs[k].setAttribute("ghhresult", "image-unset");
        buttondivs[k].style.position = "relative";
        if (buttondivs[k].nodeName == 'TABLE'){
          var tdnew = document.createElement("td");
          tdnew.innerHTML = '<button type="button" title="Block/Unblock" class="irc_but"><span class="irc_but_t">GHHbD</span></button>';
          buttondivs[k].querySelector('tr').appendChild(tdnew);
          tdnew.firstChild.addEventListener("click", imgblockdialog, false);
        } else {
          var spannew = document.createElement("span");
          spannew.style.marginLeft = '10px';
          spannew.innerHTML = '<button type="button" title="Block/Unblock" class="irc_but"><span class="irc_but_t">GHHbD</span></button>';
          buttondivs[k].appendChild(spannew);
          spannew.firstChild.addEventListener("click", imgblockdialog, false);
        }
      }
    }
  }
  if (document.querySelectorAll('style.GHHbDcss').length === 0){ // Bing losing styles... 2018-10-01
    injectBaseCSS();
    doSiteSpecific();
    GHHbD_addStyle("#ghhMngBtn {position:fixed;top:150px;right:-2.8em;-moz-transform:rotate(-90deg);-webkit-transform:rotate(-90deg);"+
      "border-bottom:0;border-bottom-left-radius:0;border-bottom-right-radius:0;padding:6px 1px;z-index:1000;}");
  }
}
var parentcard;
function hidehits(liels,ovrd){
  if (!liels){
    if (engine == 'Google'){
      liels = document.querySelectorAll("#res li.g, #res div.srg div.g, #res div._NId div.g, #res div._bkWMgd div.g, #res #rso div.g, #res #GTR div.g, #res #isr_mc, g-section-with-header g-scrolling-carousel g-inner-card, g-card div.dbsr, g-card");
    } else {
      liels = document.querySelectorAll('div#results li, div#results > div.result, div#links > div.results_links_deep > div.links_main, div#b_content ol > li.b_algo, div#results div#web > ol > li, div#WS2m > div.w, div.serp-list > div.serp-item, ul.serp-list > li.serp-item, div#main_results > div.result, div.results-column div.result--web, div.results-column div.result--news, #content_left > div.result.c-container, #content_left > div.result-op.c-container, ol.list-flat > li, div.w-gl__result, div.card-web div.card-mobile');
    }
    if (!liels) return;
  }
  if (liels.length==0){
    if (engine == 'Google'){
      liels = document.querySelectorAll("#res li.g, #res div.srg div.g, #res div._NId div.g, #res div._bkWMgd div.g, #res #rso div.g, #res #GTR div.g, #res #isr_mc, g-section-with-header g-scrolling-carousel g-inner-card, g-card div.dbsr, g-card");
    } else {
      liels = document.querySelectorAll('div#results li, div#results > div.result, div#links > div.results_links_deep > div.links_main, div#b_content ol > li.b_algo, div#results div#web > ol > li, div#WS2m > div.w, div.serp-list > div.serp-item, ul.serp-list > li.serp-item, div#main_results > div.result, div.results-column div.result--web, div.results-column div.result--news, #content_left > div.result.c-container, #content_left > div.result-op.c-container, ol.list-flat > li, div.w-gl__result, div.card-web div.card-mobile');
    }
  }
  //console.log(liels);
  if (liels.length == 0) return;
  if (liels.length == 1){if(liels[0].id == "isr_mc") liels = liels[0].querySelectorAll(".rg_di");} // Google Standard Image Results
  var hosts, hiders, nhider, i, j, k, hid, ael, ahref, dom, dompart, btn, apar, dgone, pban, linkwidth;
  hosts = blist;
  for (i=0; i<liels.length; i++){
    if ((liels[i].parentNode.nodeName == "OL" || liels[i].parentNode.nodeName == "TD" ||
         liels[i].classList.contains("card-section") || liels[i].classList.contains("ct-cs") || liels[i].classList.contains("w-gl__result") ||
         (liels[i].parentNode.nodeName == "DIV" && (liels[i].parentNode.classList.contains("srg") ||
                                                    liels[i].parentNode.classList.contains("_NId") || liels[i].parentNode.parentNode.classList.contains("_NId") ||
                                                    liels[i].parentNode.classList.contains("bkWMgd") || liels[i].parentNode.parentNode.classList.contains("bkWMgd") ||
                                                    liels[i].nodeName === 'G-INNER-CARD' || liels[i].nodeName === 'G-CARD')) ||
         (liels[i].parentNode.nodeName == "DIV" && liels[i].parentNode.id == "rso") ||
         (engine != 'Google' && liels[i].parentNode.nodeName == "DIV") ||
         liels[i].classList.contains('serp-item')) &&
        liels[i].className.indexOf("gbt")!=0 &&
        liels[i].classList.contains("gplusgrid") === false &&
        liels[i].classList.contains("mitem") === false &&
        liels[i].classList.contains("kno-kp") === false) {
      liels[i].setAttribute("ghhresult","unset");
      hiders = liels[i].getElementsByClassName("ghhider");
      nhider = hiders.length;
      if (nhider == 0 || ovrd == true){ // skip if a button is there
        hid = false;
        ael = liels[i].querySelector("div.r > a, h3 a"); // first link (not useful for video or book blocks), <h3> preferred
        if (!ael || ael.parentNode.className=='deeplink_title') ael = liels[i].querySelector("h2 a, h4 a");
        if (!ael) ael = liels[i].querySelector("a");
        if (liels[i].classList.contains("videobox")) ael = liels[i].querySelectorAll("td")[1].querySelector("a"); //video page
        if (engine == 'Google' && location.search.indexOf('adtest=on') > -1){
          ael = liels[i].querySelector('cite');
          if(ael) if(!ael.hasAttribute('href')){
            if (ael.textContent.indexOf('http://')===-1 && ael.textContent.indexOf('https://')===-1) ael.setAttribute('href', 'http://'+ael.textContent);
            else ael.setAttribute('href', ael.textContent);
          }
        }
        if (currentG.indexOf("baidu") > -1){
          if(liels[i].hasAttribute('mu')) liels[i].insertAdjacentHTML('beforeend', '<span style="display:none"><a class="c-showurl" href="' +
             liels[i].getAttribute('mu') +'">' + liels[i].getAttribute('mu') + '</a></span>');
          ael = liels[i].querySelector("a.c-showurl");
          if(ael) if(!ael.hasAttribute('href')){
            if (ael.textContent.indexOf('http://')===-1 && ael.textContent.indexOf('https://')===-1) ael.setAttribute('href', 'http://'+ael.textContent);
            else ael.setAttribute('href', ael.textContent);
          }
        }
        if (ael){ahref=ael.getAttribute("href"); if(ahref){if (ahref.search(/http|ftp/i)==0 || ahref.indexOf("/interstitial")==0 ||
                                                               ahref.indexOf("/url?q=")==0 || ahref.indexOf(currentG+"/url?q=")>-1 || ahref.indexOf("/url?sa=")==0 ||
                                                               (ahref.indexOf("/aclk?")==0 && liels[i].classList.contains("psli"))
                                                               || ahref.indexOf("//r.search.yahoo")==0 || ahref.indexOf(currentG+"/link?url=")>-1){
          dom = ahref.substr(ahref.search(/http|ftp/i));
          if (ael.hasAttribute("data-href")) dom = ael.getAttribute("data-href").substr(ael.getAttribute("data-href").indexOf("http"));
          if (dom.indexOf(currentG+"/aclk?")>-1) dom = ahref.substr(ahref.indexOf("http", 10));
          if (ahref.indexOf("/url?sa=")>-1) dom = decodeURIComponent(ahref.substr(ahref.indexOf("&url=")+5));
          if (ahref.indexOf("r.search.yahoo.com/_ylt=")>-1) dom = decodeURIComponent(ahref.substr(ahref.indexOf("RU=http")+3));
          if (dom.indexOf("search.yahoo.co.jp/r/FOR=")>-1) dom = decodeURIComponent(ahref.substr(ahref.indexOf("/**http")+3));
          if (dom.indexOf("https://ixquick-proxy.com/do/spg/highlight.pl")>-1) dom = decodeURIComponent(ahref.substr(ahref.indexOf("&u=http")+3));
          if (currentG.indexOf("baidu") > -1) dom = '//' + ael.textContent.replace('https://', '').replace('http://', '').replace('....', '');
          // if (dom.indexOf("imgrefurl")>-1) dom = dom.match(/imgrefurl=([^&]+)/)[1];
          dom = dom.split("/")[2];
          if (dom.indexOf(":")> -1) dom = dom.substr(0,dom.indexOf(":")); // Strip port number
          dompart = dom;
          liels[i].setAttribute("ghhhost",dompart);
          while (dompart.indexOf(".")> -1) {
            if (hosts.indexOf("|"+dompart+":")>-1) { // These domains suck
              if (nhider > 0){  // Remove old buttons, notices, etc.
                for (k=hiders.length-1; k>=0; k--){
                  hiders[k].parentNode.removeChild(hiders[k]);
                  nhider = liels[i].getElementsByClassName("ghhider").length;
                }
              }
              if (liels[i].classList.contains("ghh1time") === false){
                if (hosts.indexOf("|"+dompart+":p")<0) {  // Regular block
                  if (showYN=="Y"){
                    if (liels[i].classList.contains("results_links_deep")){ // DDG
                      replaceHit(dompart,ael,liels[i].querySelector(".links_main"),"");
                    }
                    else replaceHit(dompart,ael,liels[i],"");
                  }
                  else replaceHit(dompart,ael,liels[i],"none");
                } else { // Perma-ban
                  liels[i].setAttribute("blockhidden",dompart);
                  if (engine != 'Google' && liels[i].classList.contains("ghhdnone") === false){
                    liels[i].classList.add('ghhdnone');
                    if (liels[i].classList.contains("links_main")) liels[i].parentNode.classList.add('ghhdnone');
                  }
                }
                if (engine == 'DDG' && liels[i].classList.contains("results_links_deep")) kids = liels[i].lastElementChild.children; //DDG
                else kids = liels[i].children;
                for (j=0; j<kids.length; j++){ // Hide Google result
                  if (kids[j].classList.contains("ghhider") === false && kids[j].classList.contains("ghhdnone") === false){
                    kids[j].classList.add('ghhdnone');
                  }
                }
              }
              if (liels[i].classList.contains("psli")) liels[i].style.padding = "0"; // Shopping results
              hid = true;
              break;
            }
            else {
              dompart = dompart.slice(dompart.indexOf(".")+1);
              if (dompart.indexOf(".") === -1 && dompart != "tld") dompart += '.tld';
            }
          }
          if (hid == false && nhider > 1) { // Remove previous block & reset nhider
            liels[i].removeChild(liels[i].children[0]);
            // Clean up unblocked one-times
            if (liels[i].classList.contains("ghh1time")){
              liels[i].classList.remove('ghh1time');
              dgone = liels[i].getElementsByClassName("ghhd")[0];
              if (dgone) dgone.parentNode.removeChild(dgone);
              dgone = liels[i].getElementsByClassName("ghhdbuttons")[0];
              if (dgone) dgone.parentNode.removeChild(dgone);
            }
            nhider = liels[i].getElementsByClassName("ghhider").length;
          }
          if (hid == false && nhider == 0) { // Not blocked, insert block button
            // First, remove hiding for unblocked domains
            if (engine == 'DDG' && liels[i].classList.contains("results_links_deep")) kids = liels[i].lastElementChild.children; //DDG
            else kids = liels[i].children;
            for (j=0; j<kids.length; j++){
              if (kids[j].classList.contains("ghhdnone")){
                kids[j].classList.remove('ghhdnone');
              }
            }
            if (liels[i].hasAttribute("blockhidden")){
              liels[i].removeAttribute("blockhidden");
              liels[i].classList.remove('ghhdnone');
              if (engine == 'DDG' && liels[i].classList.contains("links_main")) liels[i].parentNode.classList.remove('ghhdnone');
            }
            if (liels[i].hasAttribute("blocknotice")) liels[i].removeAttribute("blocknotice");
            // Insert block button
            apar = ael;
            if (engine == 'Google'){
              if (location.search.indexOf('adtest=on') > -1){
                apar = liels[i].querySelector("h3 a, a");
                if (!apar.hasAttribute('hreforiginal')) apar.setAttribute('hreforiginal', ael.getAttribute('href'));
              } else {
                if (!apar.hasAttribute('hreforiginal')) apar.setAttribute('hreforiginal', apar.href);
              }
            }
            if (engine == 'Baidu'){
              apar = liels[i].querySelector("h3 a");
              if (!apar) apar = liels[i].querySelector("p.op_site_domain_title, div.op_generalqa_main.c-row").firstChild;
            }
            if (!apar.nextElementSibling){
              if (apar.parentNode.nodeName != "LI" &&
                  apar.parentNode.nodeName != "TD" &&
                  apar.parentNode.nodeName != "H2") apar = apar.parentNode;
            }
            if (apar != undefined) { if (dom.indexOf(currentG)<0 &&
                                         (liels[i].parentNode != document.querySelector("#tads ol")) &&
                                         (liels[i].parentNode != document.querySelector("#bottomads ol")) &&
                                         (liels[i].parentNode != document.querySelector("#ads div")) &&
                                         (liels[i].parentNode != document.querySelector("#rhs ol"))){
              btn = document.createElement("button");
              btn.appendChild(document.createTextNode(txts.block[0]));
              btn.className="ghhider ghhb";
              btn.setAttribute("meta",dom);
              if (pref1click.substr(0,1) == "Y" && mbstyle.split("-")[4] == "Y"){ //BUG: for 1-click with aggressive (subdomain) settings, dom will be incorrect
                if (engine == 'Google') btn.setAttribute("title","Block "+dom+" / SHIFT+click to display block form / ALT+click to omit");
                else btn.setAttribute("title","Block "+dom+" / SHIFT+click to display block form");
              } else if (mbstyle.split("-")[4] == "Y"){
                if (engine == 'Google') btn.setAttribute("title","Block "+dom+" / Show block form / ALT+click to omit");
                else btn.setAttribute("title","Block "+dom+" / Show block form");
              }
              btn.addEventListener("click",showbfd,true);
              //console.log(apar.parentNode.outerHTML);
              // Position button inside the H2 or H3 or H4
              if (apar.nodeName == "H3" || apar.nodeName == "H2" || apar.nodeName == "H4"){
                apar.style.overflow = "visible";
                apar.appendChild(btn);
                apar.querySelector('a').setAttribute("title",apar.querySelector('a').textContent); // full link text tooltip
              } else if (apar.parentNode.parentNode.nodeName == 'G-CARD'){
                apar.parentNode.appendChild(btn);
                apar.parentNode.parentNode.style.overflowY = 'visible';
                apar.parentNode.parentNode.style.height = 'unset';
                apar.parentNode.parentNode.style.position = 'relative';
              } else if (apar.parentNode.className == 'dbsr') {
                apar.parentNode.appendChild(btn);
                parentcard = apar.closest('g-card');
                if (parentcard){
                  parentcard.style.overflowY = 'visible';
                  parentcard.style.position = 'relative';
                }
              } else {
                if (apar.nextSibling) apar.parentNode.insertBefore(btn,apar.nextSibling);
                else apar.parentNode.appendChild(btn);
              }
              // Move button to citeline 6/10/2013
              if (bbpos == "C") {
                var citelines = liels[i].querySelectorAll("cite");
                for (var citenum=0; citenum<citelines.length; citenum++){
                  if (window.getComputedStyle(citelines[citenum]).visibility != "hidden"){
                    citelines[citenum].parentNode.appendChild(btn);
                    btn.removeAttribute("style"); 
                  } else { // add to visibility:hidden element for spacing
                    citelines[citenum].parentNode.appendChild(btn.cloneNode(true));
                  }
                }
                // Startpage.com
                citelines = liels[i].querySelectorAll('.w-gl__result-url-container');
                if (citelines.length > 0){ 
                  citelines[0].appendChild(btn);
                  btn.removeAttribute("style");
                }
              }
              // Implement Mouseover Option 6/22/2012
              if (bbstyle == "M") {
                btn.style.visibility = "hidden";
                liels[i].addEventListener("mouseover",togglebbtn,false);
                liels[i].addEventListener("mouseout",togglebbtn,false);
              }
              // Avoid unhiding garbage span 5/25/2012
              for (j=0; j<liels[i].children.length; j++){
                if (liels[i].children[j].classList.contains("ghhider") === false){
                  if (liels[i].children[j].style.display=="none") liels[i].children[j].setAttribute("wasdisplaynone","wasdisplaynone");
                }
              }
            }}
          }
        }}}
      }
    } else { // Check for and handle Google standard image results - doesn't yet support BASIC image results
      if (liels[i].classList.contains("rg_di")){
        if (!liels[i].hasAttribute("imgblock") || ovrd == true){ // skip if previously processed
          liels[i].setAttribute("imgblock", "normal");
          ael = liels[i].getElementsByTagName("a")[0];
          if (ael){if(ael.hasAttribute("href")){
            if (ael.getAttribute("href").indexOf("imgrefurl")>-1){ // Site showing the image ("visit page")
              dom = decodeURIComponent(ael.href).match(/imgrefurl=([^&]+)/)[1].split("/")[2];
              if (dom.indexOf(":")> -1) dom = dom.substr(0,dom.indexOf(":")); // Strip port number
              dompart = dom;
              while (dompart.indexOf(".")> -1) {
                if (hosts.indexOf("|"+dompart+":")>-1) { // These domains suck
                  if (hosts.indexOf("|"+dompart+":p")<0) { // Regular block
                    liels[i].setAttribute("imgblock", "regular");
                  } else { // Perma-ban
                    liels[i].setAttribute("imgblock", "pban");
                  }
                  break;
                } else {
                  dompart = dompart.slice(dompart.indexOf(".")+1);
                  if (dompart.indexOf(".") === -1 && dompart != "tld") dompart += '.tld';
                }
              }
            }
            if (ael.getAttribute("href").indexOf("imgurl")>-1){ // Site hosting the image ("view image")
              dom = decodeURIComponent(ael.href).match(/imgurl=([^&]+)/)[1].split("/")[2];
              if (dom.indexOf(":")> -1) dom = dom.substr(0,dom.indexOf(":")); // Strip port number
              dompart = dom;
              while (dompart.indexOf(".")> -1) {
                if (hosts.indexOf("|"+dompart+":")>-1) { // These domains suck
                  if (hosts.indexOf("|"+dompart+":p")<0) { // Regular block
                    liels[i].setAttribute("imgblock", "regular");
                  } else { // Perma-ban
                    liels[i].setAttribute("imgblock", "pban");
                  }
                  break;
                } else {
                  dompart = dompart.slice(dompart.indexOf(".")+1);
                }
              }
            }
          }}
        }
        var imgshuffle = false;  // CHANGE TO TRUE TO TURN ON SHUFFLING (CURRENTLY BROKEN)
        if (imgshuffle){
          // Standard image results: move p-banned nodes to the end to maintain overall page length (otherwise, autoloading stops)
          if (t_gimg) window.clearTimeout(t_gimg);
          t_gimg = window.setTimeout(fixImagesLayout, 500);
        }
      }
    }
  }
  if (!document.getElementById("ghhMngBtn") && mbstyle.split("-")[0] != "blk" && document.getElementById("res")) addMngBtn();
  if (document.getElementsByClassName("unbtn").length > 1) undupMngBtn();
  if (betatest == "Y" && engine == 'Google'){ // BETA - NEW - v1.5.2
    // If there are more than two completely invisible results, modify the query to exclude the first hidden site
    var invis = document.querySelectorAll("li[blockhidden]");
    if (invis.length >= 3) reQry("+-site:"+invis[0].getAttribute("blockhidden"));
  }
}
function fixImagesLayout(){
  // BUGGY: REPLACEMENT IMAGES DO NOT LOAD UNTIL YOU TRIGGER A REPAINT (e.g., open/close Find bar, resize window, zoom in then zoom out)
  var madeamove = false;
  var rgshes = document.querySelectorAll(".rgsh");
  var lastdatapg = rgshes[rgshes.length-1].getAttribute("data-pg");
  var badimg = document.querySelectorAll('div[imgblock="pban"]');
  // TODO: Create setting to let user choose to remove regular blocks, too; temporary workaround: uncomment the following line:
  // var badimg = document.querySelectorAll('div[imgblock="pban"],div[imgblock="regular"]');
  if (badimg.length > 0){
    for (bi=0; bi<badimg.length; bi++){
      if (badimg[bi].hasAttribute("newdatapg")){ // already moved
        if (badimg[bi].getAttribute("newdatapg") != lastdatapg){
          document.getElementById("rg_s").appendChild(badimg[bi]);
          badimg[bi].setAttribute("newdatapg", lastdatapg);
          madeamove = true;
        }
      } else {  // first move
        document.getElementById("rg_s").appendChild(badimg[bi]);
        badimg[bi].setAttribute("newdatapg", lastdatapg);
        madeamove = true;
      }
    }
    // Trigger Google's function to re-layout the results neatly
    if (madeamove){
      var sctag = document.createElement("script");
      sctag.setAttribute("type", "text/javascript");
      sctag.appendChild(document.createTextNode("google.isr.layoutInit();"));
      document.body.appendChild(sctag);
    }
  }
}
function replaceHit(sdomain,oa,oli,ddis){
  var fc, dnew, dset, btn;
  fc = oli.querySelector('h3, h2');
  if (!fc) fc = oli.firstChild;
  if (fc.nodeName=="DIV" && fc.classList.contains("ghhider")) return;
  dnew = document.createElement("div");
  if (oa.querySelector('h3')) dnew.appendChild(document.createTextNode(oa.querySelector('h3').textContent+" on "+sdomain));
  else {
    if (oli.nodeName === 'G-INNER-CARD' || oli.nodeName === 'G-CARD' || oli.className === 'dbsr'){
      if (oa.children[1]) dnew.appendChild(document.createTextNode(oa.children[1].textContent+" on "+sdomain));
      else dnew.appendChild(document.createTextNode(oa.children[0].children[1].children[1].textContent+" on "+sdomain));
      dnew.style.whiteSpace = 'normal';
    }
    else dnew.appendChild(document.createTextNode(oa.textContent+" on "+sdomain));
  }
  dnew.className="ghhider ghhd";
  dnew.setAttribute("title","Click to view, unblock or Perma-ban");
  dnew.style.display = ddis;
  if (ddis == "none"){
    oli.setAttribute("blockhidden",sdomain);
    if (oli.hasAttribute("blocknotice")) oli.removeAttribute("blocknotice");
  } else {
    oli.setAttribute("blocknotice",sdomain);
    if (oli.hasAttribute("blockhidden")) oli.removeAttribute("blockhidden");
    oli.classList.remove('ghhdnone');
    if (oli.parentNode.classList.contains("results_links_deep")){
      oli.parentNode.setAttribute("blocknotice",sdomain);
      if (oli.parentNode.hasAttribute("blockhidden")) oli.parentNode.removeAttribute("blockhidden");
      oli.parentNode.classList.remove('ghhdnone');
    }
  }
  dnew.addEventListener("click",reshow,false);
  // dnew is disappearing on Bing in Chrome TODO: FIXIT
  if (oli.className === 'dbsr'){
      parentcard = apar.closest('g-card');
      if (parentcard){
        parentcard.insertBefore(dnew, parentcard.firstChild);
      }
  } else {
    oli.insertBefore(dnew,oli.firstChild);
  }
  dset = document.createElement("div");
  dset.className = "ghhider ghhindent";
  dset.setAttribute("dom",sdomain);
  dset.style.display = "none";
  btn = document.createElement("button");
  btn.appendChild(document.createTextNode(txts.unblock[0]));
  btn.className="ghhider";
  btn.setAttribute("title","Unblock this site");
  btn.style.backgroundColor="#9f6";
  btn.addEventListener("click",unblock,false);
  dset.appendChild(btn);
  btn = document.createElement("button");
  btn.appendChild(document.createTextNode(txts.pban[0]));
  btn.className="ghhider";
  btn.setAttribute("title","Permanently hide this site");
  btn.style.backgroundColor="#f66";
  btn.addEventListener("click",permban,false);
  dset.appendChild(btn);
  btn = document.createElement("button");
  btn.appendChild(document.createTextNode("close"));
  btn.className="ghhider";
  btn.setAttribute("title","Re-hide this hit");
  btn.style.backgroundColor="#eee";
  btn.addEventListener("click",rehide,false);
  dset.appendChild(btn);
  dnew.appendChild(dset);
  if (dnew.parentNode.style.overflow == "hidden" || dnew.parentNode.style.overflowX == "hidden"){
    dnew.insertBefore(document.createElement("br"), dnew.firstChild);
  }
  dset.addEventListener("click",ghhkillevent,false);
  if (oli.classList.contains("psli")) dnew.style.margin = "1em 0"; // Shopping results
}
function hidebasic(tbl){ // BASIC IMAGE RESULTS, BETA ONLY, NON-AJAX
  var hosts, tds, i, j, k, hid, ael, dom, dompart, btn, apar, dgone;
  hosts = blist;
  tds = tbl.querySelectorAll("td");
  for (i=0; i<tds.length; i++){
    ael = tds[i].querySelector("a");
    if (ael){if(ael.hasAttribute("href")){if (ael.getAttribute("href").indexOf("imgrefurl=")>-1){
      dom = ael.getAttribute("href").substr(ael.getAttribute("href").indexOf("imgrefurl=")+7).split("/")[2];
      if (dom.indexOf(":")> -1) dom = dom.substr(0,dom.indexOf(":")); // Strip port number
      dompart = dom;
      while (dompart.indexOf(".")> -1) {
        if (hosts.indexOf("|"+dompart+":")>-1) { // These domains suck; mark the cell for now
          if (hosts.indexOf("|"+dompart+":p")>-1 || showYN=="N") tds[i].setAttribute("ghhaction","delete");
          else tds[i].setAttribute("ghhaction","notice");
          break;
        } else {
          dompart = dompart.slice(dompart.indexOf(".")+1);
          if (dompart.indexOf(".") === -1 && dompart != "tld") dompart += '.tld';
        }
      }
    }}}
  }
  for (i=0; i<tds.length; i++){
    switch (tds[i].getAttribute("ghhaction")){
      case "delete":
        // TODO implement deletion
        tds[i].innerHTML = "delete cell";
        break;
      case "notice":
        // TODO implement clickable notices
        tds[i].style.textDecoration = "line-through";
        tds[i].style.opacity = "0.3";
        break;
      default:
        // TODO add block button
    }
  }
}
// == == == Other Functions == == ==
function reshow(e){   // Show hit without unblocking
  var liel, ael, dabs, k;
  liel = e.target.parentNode;
  while (!liel.hasAttribute("ghhresult")){
    liel=liel.parentNode;
    if (liel.nodeName == "BODY") return;
  }
  liel.classList.add('ghh1time');
  // Hide notice, move action buttons, then show hit
  e.target.style.display="none";
  ael = liel.querySelector("div.r > a, h3 a");
  if (!ael && engine == 'Baidu' && liel.hasAttribute('mu')) ael = liel.querySelector("p.op_site_domain_title, div.op_generalqa_main.c-row").firstChild;
  if (!ael) ael = liel.querySelector("span.tl a"); // summarized news result
  if (!ael) ael = liel.querySelector("a"); // other
  if (liel.classList.contains("videobox")) ael = liel.querySelectorAll("td")[1].querySelector("a"); //video page
  dabs = e.target.firstElementChild;
  if (engine != 'Bing'){
    if (ael.parentNode.classList.contains('ghh1time')){
      ael.parentNode.insertBefore(dabs,ael.nextSibling);
    } else {
      if (ael.parentNode.parentNode.nodeName === 'G-INNER-CARD' || ael.parentNode.parentNode.nodeName === 'G-CARD') ael.parentNode.parentNode.insertBefore(dabs,ael.parentNode);
      else {
        if (ael.parentNode.nextSibling) ael.parentNode.parentNode.insertBefore(dabs,ael.parentNode.nextSibling);
        else ael.parentNode.parentNode.appendChild(dabs);
      }
    }
    dabs.className = "ghhdbuttons";
    dabs.removeAttribute("style");
    if (dabs.nextElementSibling) if (dabs.nextElementSibling.className.indexOf("ghhider") == 0 || dabs.nextElementSibling.innerHTML == "block") dabs.parentNode.removeChild(dabs.nextElementSibling);
  } else {
    // TODO dabs is disappearing on Bing when moved -- temporarily, don't move it
    e.target.style.display='';
    dabs.className = "ghhdbuttons";
    dabs.removeAttribute("style");
  }
  for (k=1; k<liel.children.length; k++){
    liel.children[k].classList.remove('ghhdnone');
  }
  e.stopPropagation();
}
// Hide or Show hit notices
async function updtpref(e){
  var btns, j, hds, s;
  if (showYN == "Y"){
    if (confirm("No longer show titles or buttons for suppressed results?")){
      ghhPrefO.shownotc[0] = "N";
      if (!GM4){
        GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
      } else {
        await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
      }
      showYN = ghhPrefO.shownotc[0];
      togHiderDivs("no");
    }
  } else {
    hds = document.getElementsByClassName("ghhd");
    if (hds.length > 0) s = (hds.length == 1) ? "is 1 blocked hit" : "are "+hds.length+" blocked hits";
    else s = "are no blocked hits";
    if (confirm("Show titles and buttons for suppressed results? (There "+s+" on this page.)")){
      ghhPrefO.shownotc[0] = "Y";
      if (!GM4){
        GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
      } else {
        await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
      }
      showYN = ghhPrefO.shownotc[0];
      togHiderDivs("yes");
    }
  }
  fixShowHideBtn();
  e.target.blur();
}
function fixShowHideBtn(){
  var chkMP = document.getElementById("chkshownotc");
  var chkBF = document.getElementById("chkshownotcbf");
  if (showYN == "Y"){
    chkMP.setAttribute("checked","checked");
    chkMP.checked = true;
    if (chkBF){
      chkBF.setAttribute("checked","checked");
      chkBF.checked = true;
    }
  } else {
    chkMP.removeAttribute("checked");
    chkMP.checked = false;
    if (chkBF){
      chkBF.removeAttribute("checked");
      chkBF.checked = false;
    }
  }
}
function togHiderDivs(sShow){
  var dh, i;
  dh = document.getElementsByClassName("ghhider");
  for(i=0;i<dh.length;i++) {
    if (dh[i].nodeName == "DIV" && dh[i].classList.contains("ghhindent") === false) {
      if (sShow == "yes") dh[i].style.display = "";
      else dh[i].style.display = "none";
    }
  }
}
// Remove domain from the block list
async function unblock(e){
  var elPar, sdom, slist, liel, tgt;
  elPar = e.target.parentNode;
  sdom = elPar.getAttribute("dom");
  if (!sdom || sdom.length<4){
    alert("Problem with domain to unblock");
    return;
  }
  if (!GM4){
    slist = GM_getValue("hideyhosts");
  } else {
    slist = await GM.getValue("hideyhosts");
  }
  if (slist.substr(0,1) != "|") slist = "|" + slist;
  slist = slist.replace("|"+sdom+":t","");
  if (!GM4){
    GM_setValue("hideyhosts", slist);
  } else {
    await GM.setValue("hideyhosts", slist);
  }
  blist = slist;
  needupdate = true;
  liel = elPar.parentNode;
  while (!liel.hasAttribute("ghhresult")){
    liel=liel.parentNode;
    if (liel.nodeName == "BODY") break;
  }
  //console.log(liel.outerHTML);
  if ((liel.nodeName =="LI" || liel.nodeName == "DIV") && liel.classList.contains("ghh1time")){
    liel.classList.remove('ghh1time');
    liel.removeChild(liel.getElementsByClassName("ghhd")[0]);
    elPar.parentNode.removeChild(elPar);
  }
  hidehits(null,true);
  if (document.getElementById("ghhmngform")){
    if(document.getElementById("ghhmngform").style.display=="block") refreshSiteList();
  }
}
// Add domain to the Perma-ban list
async function permban(e){
  if (!confirm("Never see hits for this domain again?")) return;
  var dpar, sdom, slist, liel;
  dpar = e.target.parentNode;
  sdom = dpar.getAttribute("dom");
  if (!GM4){
    slist = GM_getValue("hideyhosts");
  } else {
    slist = await GM.getValue("hideyhosts");
  }
  if (slist.substr(0,1) != "|") slist = "|" + slist;
  slist = slist.replace("|"+sdom+":t","|"+sdom+":p");
  if (!GM4){
    GM_setValue("hideyhosts", slist);
  } else {
    await GM.setValue("hideyhosts", slist);
  }
  blist = slist;
  needupdate = true;
  liel = dpar.parentNode;
  while (!liel.hasAttribute("ghhresult")){
    liel=liel.parentNode;
    if (liel.nodeName == "BODY") break;
  }
  if ((liel.nodeName =="LI" || liel.nodeName == "DIV" || liel.nodeName == 'G-INNER-CARD' || liel.nodeName == 'G-CARD') && liel.classList.contains("ghh1time")){
    liel.classList.remove('ghh1time');
  }
  if(dpar.classList.contains("ghhindent")) dpar = dpar.parentNode;
  dpar.parentNode.removeChild(dpar);
  hidehits(null,true);
  if (document.getElementById("GTR")) removePBs();
  if (document.getElementById("ghhmngform")){
    if(document.getElementById("ghhmngform").style.display=="block") refreshSiteList();
  }
}
// Close this bad result and rehide (to allow indendent open/close, do not run through hidehits)
function rehide(e){
  var dpar, liel, dompart, ael, j;
  dpar = e.target.parentNode;
  liel = dpar.parentNode;
  while (!liel.hasAttribute("ghhresult")){
    liel=liel.parentNode;
    if (liel.nodeName == "BODY") break;
  }
  dompart = dpar.getAttribute("dom");
  if (engine != 'Bing'){
    dpar.parentNode.removeChild(dpar);
    liel.removeChild(liel.querySelector("div.ghhd"));
  } else {
    // TODO notice is disappearing on Bing -- temporarily, do not move/remove the buttons div
    liel.querySelector('div.ghhd > div.ghhdbuttons').style.display = 'none';
  }
  ael = liel.querySelector("h3 a, h2 a");
  if (!ael) ael = liel.querySelector("a");
  liel.classList.remove('ghh1time');
  replaceHit(dompart,ael,liel,"");
  for (j=0; j<liel.children.length; j++){ // Hide Google result
    if (liel.children[j].classList.contains("ghhider") === false && liel.children[j].classList.contains("ghhdnone") === false){
      liel.children[j].classList.add('ghhdnone');
    }
  }
}
// Functions relating to the Block form
function addBlockForm(){
  var bfd = document.createElement("div");
  bfd.id = "ghhblockform";
  bfd.className = "ghhpane";
  var bfdcode = '<form onsubmit="return false;"><p style="margin:0.75em 0;"><strong>Add to blocklist:</strong></p><p><label ' +
      'style="white-space:pre"><input type="radio" name="ghhdom" value="f"> <span id="ghhfulldom"></span></label><br>' +
      '<label><input type="radio" name="ghhdom" value="p"> <span id="ghhpartdom"></span>  <button type="button" id="ghhdomadj" ' +
	  'title="Adjust partial domain" style="position: absolute; right: 1em; padding: 0 1px;">~</button></label></p>' +
      '<p style="text-align:center;white-space:pre;line-height:2em;margin:0.75em 0"><button type="button" id="ghhbf1" bt="t"> ' +
	  txts.okbtn[0] + ' </button> <button type="button" id="ghhbf3" bt="p"> ' + txts.okPbtn[0] + ' </button><br>' +
      '<button type="button" id="ghhbf2" mng="N"> ' + txts.cancelbtn[0] + ' </button> ' +
      '<button type="button" id="ghhbf4" mng="Y">' + txts.cancelMbtn[0] + '</button></p>';
  if (engine == 'Google'){
    bfdcode += "<p style=\"border-top:1px solid #aaa;text-align:center;white-space:pre;line-height:2em;margin:0.75em 0;padding-top:0.5em;\">Edit query: <button type=\"button\" id=\"ghhbf5\" title=\"This site only\"> +site: </button> " +
      "<button type=\"button\" id=\"ghhbf6\" title=\"Exclude this site\"> -site: </button></p>"
  }
  bfdcode += "<p style=\"margin:0.75em 0;\"><label title=\"Switch between showing and hiding result titles for regular blocked hits\"><input " +
    "type=\"checkbox\" name=\"chkshownotcbf\" id=\"chkshownotcbf\"> Show hidden hit notices</label><br>" +
    "<label title=\"Switch between block dialog and one-click blocking\"><input type=\"checkbox\" name=\"chk1clickbf\" " +
    "id=\"chk1clickbf\"> Enable 1-click blocking</label></p></form>";
  bfd.innerHTML = bfdcode;
  document.body.appendChild(bfd);
  document.getElementById("ghhbf1").addEventListener("click",addblock,false);
  document.getElementById("ghhbf2").addEventListener("click",ghhcloseform,false);
  document.getElementById("ghhbf3").addEventListener("click",addblock,false);
  document.getElementById("ghhbf4").addEventListener("click",ghhcloseform,false);
  if (engine == 'Google'){
    document.getElementById("ghhbf5").addEventListener("click",reQuery,false);
    document.getElementById("ghhbf6").addEventListener("click",reQuery,false);
  }
  document.getElementById("ghhblockform").addEventListener("click",ghhkillevent,false);
  document.getElementById("chkshownotcbf").addEventListener("change",updtpref,false);
  document.getElementById("chk1clickbf").addEventListener("change",updt1click,false);
  document.getElementById("ghhdomadj").addEventListener("click",adjpartdom,false);
}
function showbfd(e) {
  var bbtn, bfdiv, fdom, pdom, fspan, pspan, tdiv, lt;
  bbtn = e.target;
  fdom = bbtn.getAttribute("meta");
  if (!document.getElementById("ghhblockform")) addBlockForm();
  fspan = document.getElementById("ghhfulldom");
  fspan.textContent = fdom;
  fspan.previousElementSibling.checked = true;
  pdom = fdom.substr(fdom.indexOf(".")+1);
  pspan = document.getElementById("ghhpartdom");
  if (pdom.indexOf(".") > -1 && patIPv4.test(fdom) != true) {
    pspan.textContent = pdom;
    pspan.parentNode.style.display = "";
    switch (bAggress){
      case "all":
        pspan.previousElementSibling.checked = true;
      case "www":
        if (fdom.substr(0,3) == "www") pspan.previousElementSibling.checked = true;
      default:
        // default to full domain
    }
    document.getElementById("ghhdomadj").style.display = '';
  } else {
    pspan.parentNode.style.display = "none";
    document.getElementById("ghhdomadj").style.display = 'none';
  }
  if (e.altKey == true && engine == 'Google'){
    reQuery(); return;
  }
  bfdiv = document.getElementById("ghhblockform");
  tdiv = document.getElementById("ghhtemp");
  if (!tdiv){
    tdiv = document.createElement("div");
    tdiv.id = "ghhtemp";
  }
  if (isch == true){
    tdiv.setAttribute("style", "position:absolute;right:0;top:0;z-index:3000;width:250px;");
    bbtn.parentNode.appendChild(tdiv);
  } else if (e.target.parentNode.parentNode.nodeName == 'G-INNER-CARD' || e.target.parentNode.parentNode.nodeName == 'G-CARD') {
    tdiv.setAttribute("style", "position:absolute;left:8px;top:8px;z-index:9999;width:100%;");
    e.target.parentNode.parentNode.insertBefore(tdiv, e.target.parentNode.parentNode.children[0]);
  } else if (e.target.parentNode.nodeName == 'G-INNER-CARD' || e.target.parentNode.nodeName == 'G-CARD') {
    tdiv.setAttribute("style", "position:absolute;left:8px;top:8px;z-index:9999;width:100%;");
    e.target.parentNode.insertBefore(tdiv, e.target.parentNode.children[0]);
  } else if (e.target.parentNode.className == 'dbsr') {
    tdiv.setAttribute("style", "position:absolute;left:8px;top:8px;z-index:9999;width:100%;");
    e.target.parentNode.insertBefore(tdiv, e.target.parentNode.children[0]);
  } else {
    lt = bbtn.offsetLeft + bbtn.offsetWidth + 12;
    if (bbtn.parentNode.previousElementSibling){
      if (window.getComputedStyle(bbtn.parentNode.previousElementSibling,null).getPropertyValue("float") != "none" ||
          (bbtn.style.position == "absolute" && bbtn.parentNode.nodeName == "TD")) lt=lt-bbtn.parentNode.offsetLeft;
    }
    if (document.querySelector('table#GTR')){
      lt-=230;
    }
    if (engine != 'Google') lt=lt-bbtn.parentNode.offsetLeft;
    if (engine == 'Ecosia') lt = 16;
    tdiv.setAttribute("style", "position:relative;left:" +  lt + "px;top:-65px;z-index:500;width:250px;");
    if (bbtn.nextElementSibling){
      if (bbtn.nextElementSibling.nodeName == "DIV" || bbtn.nextElementSibling.nodeName == "BR") bbtn.parentNode.insertBefore(tdiv,bbtn.nextElementSibling);
      else bbtn.parentNode.appendChild(tdiv);
    }
    else bbtn.parentNode.appendChild(tdiv);
  }
  tdiv.appendChild(bfdiv);
  if (window.getComputedStyle(tdiv.parentNode).overflowX == "hidden" || window.getComputedStyle(tdiv.parentNode).overflowY == "hidden"){
    tdiv.parentNode.style.overflowX = "visible";
    tdiv.parentNode.style.overflowY = "visible";
  }
  if (pref1click.substr(0,1) == "Y" && e.shiftKey != true  && isch != true){ // 1-click; hold Shift to override
    if (pref1click.substr(2,1) == "N"){
      document.getElementById("ghhbf1").click();
    } else {
      document.getElementById("ghhbf3").click();
    }
  } else { // regular + populating 1-click checkbox
    var chkBF = document.getElementById("chk1clickbf");
    if (pref1click.substr(0,1) == "Y"){
      chkBF.setAttribute("checked","checked");
      chkBF.checked = true;
    } else {
      chkBF.removeAttribute("checked");
      chkBF.checked = false;
    }
    chkBF = document.getElementById("chkshownotcbf");
    if (showYN == "Y"){
      chkBF.setAttribute("checked","checked");
      chkBF.checked = true;
    } else {
      chkBF.removeAttribute("checked");
      chkBF.checked = false;
    }
    bfdiv.style.display = "block";
    document.getElementById("ghhbf1").focus();
  }
  e.stopPropagation();
}
function adjpartdom(e){ // v1.8.1
  var pspan = document.getElementById("ghhpartdom");
  var parts = pspan.textContent.replace('...', '').split(".");
  if (parts.length <= 2){
    if (parts.length == 2 && parts[1].indexOf('tld [all') !== 0){
      // offer the entire TLD option v1.9.9
      parts.push('tld [all dot-' + parts[1] + '\'s]');
    } else {
      // cycle back to the original partial domain
      parts = document.getElementById("ghhfulldom").textContent.split(".");
    }
  }
  parts.shift(); // discard leftmost subdomain
  pspan.textContent = parts.join(".");
}
async function addblock(e){
  var btype, els, i, sdom, tgt;
  tgt = e.target;
  btype = tgt.getAttribute("bt");
  els = tgt.form.querySelectorAll('input[type="radio"]');
  for (i=0; i<els.length; i++){
    if(els[i].checked == true){
      sdom = els[i].nextElementSibling.textContent.split(" ")[0];
      break;
    }
  }
  ghhcloseform(e);
  if (blist.substr(0,1) != "|") blist = "|" + blist;
  if (!btype) btype == "t";
  if (addAt == "end") blist += sdom + ":" + btype + "|";
  else blist = "|" + sdom + ":" + btype + blist;
  needupdate = true;
  if (!GM4){
    GM_setValue("hideyhosts", blist);
  } else {
    await GM.setValue("hideyhosts", blist);
  }
  hidehits(null,true);
  if (document.getElementById("GTR")) removePBs();
  if (addAt == "sort") sortlist(null);
  if (document.getElementById("ghhmngform")){
    if(document.getElementById("ghhmngform").style.display=="block") refreshSiteList();
  }
}
async function ghhcloseform(e){
  if (!e) return;
  if (typeof(e) == "object" && e.target){
    if(e.target.id.indexOf("ghhbf") == 0){
      var mng = e.target.getAttribute("mng");
      var bfdiv = document.getElementById("ghhblockform");
      var tdiv = document.getElementById("ghhtemp");
      bfdiv.style.display = "none";
      document.body.appendChild(bfdiv);
      tdiv.parentNode.removeChild(tdiv);
      if (mng == "Y") showManageForm("mngform");
    }
    if(e.target.id.indexOf("ghhmf") == 0){
      if (mbstyle.split("-")[0] == "mng") toggleBlockHiders("H");
      document.getElementById("ghhmngform").style.display = "none";
      if (mpopen.substr(0,3) == "Y-Y"){
        mpopen = "Y-N";
        ghhPrefO.mngpaneopen[0] = mpopen;
        if (!GM4){
          GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
        } else {
          await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
        }
      }
    }
  } else {
    if(e == "mngform"){
      if (mbstyle.split("-")[0] == "mng") toggleBlockHiders("H");
      document.getElementById("ghhmngform").style.display = "none";
      if (mpopen.substr(0,3) == "Y-Y"){
        mpopen = "Y-N";
        ghhPrefO.mngpaneopen[0] = mpopen;
        if (!GM4){
          GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
        } else {
          await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
        }
      }
    }
  }
  e.stopPropagation();
}
async function imgblockdialog(e){
  var viewer = e.target.parentNode;
  while (!viewer.hasAttribute("ghhresult")){
    viewer=viewer.parentNode;
    if (viewer.nodeName == "BODY") return;
  }
  var ael = viewer.parentNode.children[0].querySelector('._r3 a[href], span > a[href]');
  if (!ael) ael = viewer.querySelector('a[href]'); // Aug. 2019 design
  if (!ael){ alert('Cannot find the URL in this design.'); return; }
  //console.log(ael);
  var ameta = ael.href.split("/")[2];
  if (ameta.indexOf("&url=")>-1) ameta = decodeURIComponent(ameta).match(/&url=([^&]+)/)[1].split("/")[2];
  if (ameta.indexOf(":")> -1) ameta = ameta.substr(0,ameta.indexOf(":")); // Strip port number
  e.target.setAttribute("meta", ameta);
  dompart = ameta;
  while (dompart.indexOf(".")> -1) {
    if (blist.indexOf("|"+dompart+":") > -1){
      if (confirm("Unblock " + dompart + "?")){
        if (!GM4){
          slist = GM_getValue("hideyhosts");
        } else {
          slist = await GM.getValue("hideyhosts");
        }
        if (slist.substr(0,1) != "|") slist = "|" + slist;
        slist = slist.replace("|"+dompart+":t","").replace("|"+dompart+":p","");
        if (!GM4){
          GM_setValue("hideyhosts", slist);
        } else {
          await GM.setValue("hideyhosts", slist);
        }
        blist = slist;
        needupdate = true;
        hidehits(null,true);
        if (document.getElementById("ghhmngform")){
          if(document.getElementById("ghhmngform").style.display=="block") refreshSiteList();
        }
      }
      e.stopPropagation();
      return;
    } else {
      dompart = dompart.slice(dompart.indexOf(".")+1);
    }
  }
  showbfd(e);
}
// Functions relating to the Manage Hiding button
function addMngBtn(){
  if (mbstyle.split("-")[0] == "blk") return;
  if (window.self != window.top) if (mbstyle.split("-")[1] == "ifrN") return;
  var mbtn;
  mbtn = document.createElement("button");
  mbtn.appendChild(document.createTextNode(txts.mngbtn[0]));
  mbtn.className="ghhider unbtn";
  mbtn.setAttribute("title","Manage Google Hit Hider Settings");
  mbtn.id = "ghhMngBtn";
  mbtn.addEventListener("click",showManageForm,true);
  document.body.appendChild(mbtn);
}
function undupMngBtn(){
  var unbtns = document.getElementsByClassName("unbtn");
  while (unbtns.length > 1){
    unbtns[unbtns.length - 1].parentNode.removeChild(unbtns[unbtns.length - 1]);
  }
}
async function showManageForm(e){
  if (window.self != window.top) return;
  var mfd;
  if (!document.getElementById("ghhmngform")) addManageForm();
  mfd = document.getElementById("ghhmngform");
  if (mfd.style.display != "none" && e != "mngform"){ // Toggle to hidden
    if (mbstyle.split("-")[0] == "mng") toggleBlockHiders("H");
    if (mpopen.substr(0,3) == "Y-Y"){
      mpopen = "Y-N";
      ghhPrefO.mngpaneopen[0] = mpopen;
      if (!GM4){
        GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
      } else {
        await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
      }
    }
    mfd.style.display = "none";
  } else {
    if (needupdate == true) refreshSiteList();
    mfd.style.display = "block";
    if (mpopen.substr(0,3) == "Y-Y" && mpopen.length == 5){ // Restore last displayed tab
      var tabnum = mpopen.substr(4,1);
      if (document.getElementById('ghhmt'+tabnum).style.display == "none"){
        togglelist('ghhts'+tabnum);
        if (mbstyle.split("-")[0] == "mng") toggleBlockHiders("S");
        if (typeof e == "object") e.target.blur();
        return
      }
    }
    if (document.getElementById("ghhmt1").style.display != "none" || document.getElementById("ghhmt4").style.display != "none"){
      document.getElementById("ghhmf1").setAttribute("disabled","disabled");
      document.getElementById("ghhutil").style.display == "none";
    }
    else {
      if (document.getElementById("ghhmf1").hasAttribute("disabled")) document.getElementById("ghhmf1").removeAttribute("disabled");
      if (bLUopen != "N") document.getElementById("ghhutil").style.display = "block";
    }
    setCurrentTab();
    if (mbstyle.split("-")[0] == "mng") toggleBlockHiders("S");
  }
  if (typeof e == "object") e.target.blur();
}
function setCurrentTab(){
  var k, tabnum;
  var tabset = document.querySelectorAll("#mflists>div");
  for (k=0; k<tabset.length; k++){
    tabnum = tabset[k].getAttribute("id");
    tabnum = tabnum.substr(tabnum.length-1);
    if (tabset[k].style.display != "none"){
      document.getElementById("ghhts"+tabnum).className = "ghhCurTab";
      if (mpopen.substr(0,1) == "Y"){
        mpopen = "Y-Y-"+tabnum;
        ghhPrefO.mngpaneopen[0] = mpopen;
        if (!GM4){
          GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
        } else { /* NOT SYNCHRONOUS */
          GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
        }
      }
    }
    else document.getElementById("ghhts"+tabnum).className = "";
  }
}
// Functions relating to the Manage GHH form
function addManageForm(){
  var mfd = document.createElement("div");
  mfd.id = "ghhmngform";
  mfd.className = "ghhpane";
  mfd.setAttribute("style","display:none;");
  mfd.innerHTML = "<form onsubmit=\"return false;\"><div id=\"ghhtsdiv\">" +
    "<p style=\"margin:6px 0 -1px 0\" id=\"ghhtstrip\">" +
    "<button type=\"button\" id=\"ghhts1\" title=\"General Use and Notices\">Home</button>" +
    "<button type=\"button\" id=\"ghhts2\" title=\"Regular Block List\">Block</button>" +
    "<button type=\"button\" id=\"ghhts3\" title=\"Perma-ban List\">Perma-ban</button>" +
    "<button type=\"button\" id=\"ghhts4\" title=\"Manage Script Options\">Options</button></p></div>" +
    "<div id=\"mflists\" style=\"width:230px\">" +
    "<div id=\"ghhmt1\"><p>Welcome to Google Hit Hider! <a href=\"https://www.jeffersonscher.com/gm/google-hit-hider/\" " +
    "style=\"float:right;\" target=\"_blank\" title=\"Documentation\">JS</a></p>" +
    "<div class=\"ghhtab\">" +
    "<p style=\"padding:0.25em;margin:0.25em\">Click the block button ( <button type=\"button\" class=\"ghhider\" onclick=\"return false;\">" + txts.block[0] + "</button> ) " +
    "next to a hit title to block results from that site. A <b>regular</b> blocked hit becomes a one-line notation, " +
    "while a <b>Perma-ban</b> disappears completely.</p>" +
    "<p style=\"border-top:1px solid #000; padding:0.25em;margin:0.25em\"><label title=\"Switch between showing and hiding result titles " +
    "for regular blocked hits\"><input type=\"checkbox\" name=\"chkshownotc\" id=\"chkshownotc\"> Show hidden hit notices</label><br>" +
    "<label title=\"Switch between block dialog and one-click blocking\"><input type=\"checkbox\" name=\"chk1click\" " +
    "id=\"chk1click\"> Enable 1-click blocking</label></p>" +
    "<p style=\"border-top:1px solid #000; padding:0.25em;margin:0.25em\">v2.1.2 &copy; 2020 Jefferson Scher. Learn more on " +
    "<a href=\"" + script_about + "\">this script's page</a>.</p></div></div>" +
    "<div id=\"ghhmt2\" style=\"display:none\"><p>Click to remove from regular block list:</p>" +
    "<div class=\"ghhtab\"><ul id=\"ghhsitelist\"></ul></div></div>\n" +
    "<div id=\"ghhmt3\" style=\"display:none\"><p>Click to remove from Perma-ban list:</p>" +
    "<div class=\"ghhtab\"><ul id=\"ghhpbanlist\"></ul></div></div>" +
    "<div id=\"ghhmt4\" style=\"display:none\"><p>Manage script options:</p>" +
    "<div class=\"ghhtab\" id=\"btnedit\">" +
    "<p id=\"addradios\">Add newly blocked domains:<br>" +
    "<label><input type=\"radio\" name=\"addpos\" value=\"end\"> at the end of the list</label><br>" +
    "<label><input type=\"radio\" name=\"addpos\" value=\"top\"> at the top of the list</label><br>" +
    "<label><input type=\"radio\" name=\"addpos\" value=\"sort\"> in alphabetical order</label></p>" +
    "<p id=\"aggressrads\" style=\"border-top:1px solid #000;padding-top:0.25em;margin-bottom:8px\">Block form defaults to:<br>" +
    "<label><input type=\"radio\" name=\"agglevel\" value=\"none\"> always the full domain</label><br>" +
    "<label><input type=\"radio\" name=\"agglevel\" value=\"all\"> always the partial domain</label><br>" +
    "<label><input type=\"radio\" name=\"agglevel\" value=\"www\"> partial domain for www only</label></p>" +
    "<p id=\"btnradios\" style=\"border-top:1px solid #000;padding-top:0.25em;margin-bottom:8px\">User interface style:<br>" +
    "<label><input type=\"radio\" name=\"uistyle\" value=\"both\"> Show Manage Hiding &amp; " + txts.block[0] + "</label><br>" +
    "<label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type=\"checkbox\" name=\"mbiframe\" id=\"mbiframe\"> Manage Hiding in iframes</label><br>" +
    "<label title=\"You can click a " + txts.block[0] + " button to open this dialog\"><input type=\"radio\" name=\"uistyle\" value=\"blk\"> Hide Manage Hiding button</label><br>" +
    "<label title=\"" + txts.block[0] + " buttons will appear only when this dialog is displayed\"><input type=\"radio\" name=\"uistyle\" value=\"mng\"> Hide " + txts.block[0] + " buttons</label><br>" +
    "<span style=\"display:inline-block;margin-top:4px;\">Manage Hiding button position:</span><br>" +
    "<label><input type=\"radio\" name=\"mngbtnpos\" value=\"R\"> Side</label> " +
    "<label><input type=\"radio\" name=\"mngbtnpos\" value=\"T\"> Top</label> " +
    "<label><input type=\"radio\" name=\"mngbtnpos\" value=\"B\"> Bottom</label><br>" +
    "<span style=\"display:inline-block;margin-top:4px;\">Block button position <i>(reloads)</i>:</span><br>" +
    "<label><input type=\"radio\" name=\"blockposit\" value=\"H\"> Headline</label> " +
    "<label><input type=\"radio\" name=\"blockposit\" value=\"C\"> Cite line</label><br>" +
    "<span style=\"display:inline-block;margin-top:4px;\">Display block buttons:</span><br>" +
    "<label><input type=\"radio\" name=\"blockdisp\" value=\"P\"> Always</label> " +
    "<label><input type=\"radio\" name=\"blockdisp\" value=\"M\"> On Mouseover</label><br>" +
    "<span style=\"display:inline-block;margin-top:4px;\">Block button tooltips:</span><br>" +
    "<label><input type=\"radio\" name=\"blockttip\" value=\"Y\"> Full Detail</label> " +
    "<label><input type=\"radio\" name=\"blockttip\" value=\"N\"> None</label></p>" +
    "<p id=\"miscpref\" style=\"border-top:1px solid #000;padding-top:0.25em;margin-bottom:8px\">Misc Preferences:<br>" +
    "<label><input type=\"checkbox\" name=\"chkajax\" id=\"chkajax\"> Instant/AJAX/Autopager</label><br>" +
    "<label><input type=\"checkbox\" name=\"chkdom4\" id=\"chkdom4\"> DOM4 Mutation Observer</label><br>" +
    "<label><input type=\"checkbox\" name=\"chkmpopen\" id=\"chkmpopen\"> Re-open Management Pane</label><br>" +
    "<label><input type=\"checkbox\" name=\"chk1pban\" id=\"chk1pban\"> 1-click to Perma-ban list</label><br>" +
    "<label title=\"Try out features that haven't been completely tested\"><input type=\"checkbox\" name=\"chkbeta\" " +
    "id=\"chkbeta\"> Enable beta features</label></p>" +
    "<p style=\"border-top:1px solid #000;padding-top:0.25em;margin-bottom:8px\">Edit captions:</p>" +
    "<p><button type=\"button\" class=\"ghhider\" id=\"ghhedit1\" key=\"block\">" + txts.block[0] + "</button> " +
    "<button type=\"button\" class=\"ghhider\" id=\"ghhedit3\" key=\"unblock\" style=\"background:#9f6\">" + txts.unblock[0] + "</button> " +
    "<button type=\"button\" class=\"ghhider\" id=\"ghhedit2\" key=\"pban\" style=\"background:#f66\">" + txts.pban[0] + "</button></p>" +
    "<p><i>Reload to complete changes</i></p><p><button type=\"button\" id=\"ghhmfr\">Restore default captions</button></p>" +
    "<p style=\"border-top:1px solid #000;padding-top:0.25em;margin-bottom:8px\">Custom style rules:<br>" +
    "<button type=\"button\" id=\"ghhecsr\">Edit Custom Style Rules</button></p></div></div>" +
    "</div><p style=\"text-align:center;white-space:pre;margin:1em 0\">" +
    "<button type=\"button\" id=\"ghhmf1\">" + txts.savebtn[0] + "<span id=\"numchgs\"></span></button> " +
    "<button type=\"button\" id=\"ghhmf3\" title=\"Display additional buttons for list management\">List Util " +
    "<div style=\"display:inline;font-size:0.9em;color:#888\"><span id=\"ghhdowntriangle\">&#9660;</span>" +
    "<span id=\"ghhuptriangle\" style=\"display:none\">&#9650;</span></div></button> " +
    "<button type=\"button\" id=\"ghhmf2\">" + txts.closebtn[0] + "</button></p><p id=\"ghhutil\" style=\"display:none\">" +
    "<button type=\"button\" id=\"ghhmf4\" title=\"Display block list for copying to backup or share\">" +
    txts.eximbtn[0] + "</button> <button type=\"button\" id=\"ghhmf7\" title=\"Import domains to the block list\">" +
    txts.impobtn[0] + "</button> <button type=\"button\" id=\"ghhmf8\" title=\"Add all domains on this page to current list\">" +
    txts.addallbtn[0] + "</button><br /><button type=\"button\" id=\"ghhmf5\" title=\"Sort list in alphabetical order\">" +
    txts.sortbtn[0] + "</button> <button type=\"button\" id=\"ghhmf6\" title=\"De-duplicate block list by removing unnecessary domains\">" +
    txts.dedupbtn[0] + "</button> <button type=\"button\" id=\"ghhmf9\" title=\"Remove www from blocked domains\">" +
    txts.unwwwbtn[0] + "</button></p></form>";
  document.body.appendChild(mfd);
  fixShowHideBtn();
  fixuistyle();
  fixaddpos();
  fixaggblock();
  fixajaxstyle();
  fixpanepersist();
  fix1clickstyle();
  fixBeta();
  document.getElementById("ghhts1").addEventListener("click",togglelist,true); // tabs
  document.getElementById("ghhts2").addEventListener("click",togglelist,true);
  document.getElementById("ghhts3").addEventListener("click",togglelist,true);
  document.getElementById("ghhts4").addEventListener("click",togglelist,true);
  document.getElementById("chkshownotc").addEventListener("change",updtpref,true); // home
  document.getElementById("chk1click").addEventListener("change",updt1click,true);
  document.getElementById("ghhsitelist").addEventListener("click",togglesite,true); // block
  document.getElementById("ghhpbanlist").addEventListener("click",togglesite,true); // pban
  document.getElementById("addradios").addEventListener("change",updtaddpos,true); // options
  document.getElementById("aggressrads").addEventListener("change",updtaggress,true);
  document.getElementById("chkajax").addEventListener("change",updtAJAX,true);
  document.getElementById("chkdom4").addEventListener("change",updtAJAX,true);
  document.getElementById("chkmpopen").addEventListener("change",updtpersist,true);
  document.getElementById("chk1pban").addEventListener("change",updt1click,true);
  document.getElementById("chkbeta").addEventListener("change",updtBeta,true);
  document.getElementById("btnradios").addEventListener("change",updtuistyle,true);
  document.getElementById("ghhedit1").addEventListener("click",chgcaption,true);
  document.getElementById("ghhedit2").addEventListener("click",chgcaption,true);
  document.getElementById("ghhedit3").addEventListener("click",chgcaption,true);
  document.getElementById("ghhmfr").addEventListener("click",resetTextStrings,true);
  document.getElementById("ghhecsr").addEventListener("click",openCustomStyleBar,true);
  document.getElementById("ghhmf1").addEventListener("click",saveedits,true); // buttons
  document.getElementById("ghhmf2").addEventListener("click",ghhcloseform,true);
  document.getElementById("ghhmf3").addEventListener("click",toggleListUtil,true);
  document.getElementById("ghhmf4").addEventListener("click",exportlist,true);
  document.getElementById("ghhmf5").addEventListener("click",sortlist,true);
  document.getElementById("ghhmf6").addEventListener("click",dedup,true);
  document.getElementById("ghhmf7").addEventListener("click",importlist,true);
  document.getElementById("ghhmf8").addEventListener("click",addAllNow,true);
  document.getElementById("ghhmf9").addEventListener("click",unwww,true);
  // Add JS icon link
	addBtnLink()
}
async function addBtnLink(){
  var JSBTN = document.createElement("img");
  if (!GM4){
    JSBTN.src = GM_getResourceURL("mycon");
  } else { /* asynchronous*/
    JSBTN.src = await GM.getResourceUrl("mycon");
  }
  document.querySelector("#ghhmt1 a").textContent = "";
  document.querySelector("#ghhmt1 a").appendChild(JSBTN);
}
function togglelist(e){ // Change tabs
  if (typeof e === 'string'){
    var tgtid = e;
  } else {
    e.target.blur();
    if (e.target.className == "ghhCurTab") return;
    var tgtid = e.target.id;
  }
  var tabbtns = document.querySelectorAll("#ghhtstrip>button");
  var k, tabnum;
  for (k=0; k<tabbtns.length; k++){
    tabnum = tabbtns[k].id;
    tabnum = tabnum.substr(tabnum.length-1);
    if (tgtid == tabbtns[k].id){
      document.getElementById("ghhmt"+tabnum).style.display = "";
    } else {
      document.getElementById("ghhmt"+tabnum).style.display = "none";
    }
  }
  if (document.getElementById("ghhmt1").style.display != "none" || document.getElementById("ghhmt4").style.display != "none"){
    document.getElementById("ghhmf1").setAttribute("disabled","disabled");
    document.getElementById("ghhutil").style.display = "none";
  } else {
    if (document.getElementById("ghhmf1").hasAttribute("disabled")) document.getElementById("ghhmf1").removeAttribute("disabled");
    if (bLUopen != "N") document.getElementById("ghhutil").style.display = "block";
  }
  setCurrentTab();
}
function toggleListUtil(e){ // Display/close extra set of buttons
  e.target.blur();
  var p = document.getElementById("ghhutil");
  if (!p) return;
  // If not displaying a list now, move to a list
  if (document.getElementById("ghhmt1").style.display != "none" || document.getElementById("ghhmt4").style.display != "none"){
    togglelist('ghhts2');
    p.style.display = "block";  // Always open button pane
    bLUopen = "Y";
    document.getElementById('ghhdowntriangle').style.display = 'none';
    document.getElementById('ghhuptriangle').style.display = '';
  } else {
    if (p.style.display != "block"){  // Toggle when list already was displayed
      p.style.display = "block";
      bLUopen = "Y";
      document.getElementById('ghhdowntriangle').style.display = 'none';
      document.getElementById('ghhuptriangle').style.display = '';
    } else {
      p.style.display = "none";
      bLUopen = "N";
      document.getElementById('ghhdowntriangle').style.display = '';
      document.getElementById('ghhuptriangle').style.display = 'none';
    }
  }
}
function togglesite(e){ // Designate list items for unblock, pban or block
  var t, l, s, pid;
  t = e.target;
  if (t.className == "ghhinfo") t = t.nextElementSibling;
  l = t.parentNode;
  pid = l.parentNode.id;
  switch (t.className){
    case "ghhhost ghhpb":
      t.className = "ghhhost ghhblk";  // toggle to block
      if (l.nodeName == "LI"){
        if (pid == "ghhsitelist"){
          l.children[0].style.display = "none";
          listchgs = listchgs - 1;
        } else {
          l.children[0].style.display = "inline";
          l.children[0].textContent = "to " + txts.block[0];
          l.children[0].style.backgroundColor = "#ccc";
          listchgs = listchgs + 1;
        }
      }
      break;
    case "ghhhost ghhdel":
      t.className = "ghhhost ghhpb";   // toggle to perma-ban
      if (l.nodeName == "LI"){
        if (pid == "ghhpbanlist"){
          l.children[0].style.display = "none";
          listchgs = listchgs - 1;
        } else {
          l.children[0].style.display = "inline";
          l.children[0].textContent = "to " + txts.pban[0];
          l.children[0].style.backgroundColor = "#f66";
        }
      }
      break;
    default:
      t.className = "ghhhost ghhdel";  // toggle to unblock
      if (l.nodeName == "LI"){
        l.children[0].style.display = "inline";
        l.children[0].textContent = "to " + txts.unblock[0];
        l.children[0].style.backgroundColor = "#9f6";
        if (pid == "ghhsitelist"){
          listchgs = listchgs + 1;
        }
      }
                     }
}
async function saveedits(e){  // Save changes made on tabs 2 and 3
  if (e){
    if (listchgs == 0){
      if (!confirm("No changes detected. Save anyway?")){
        e.target.blur();
        return;
      }
    } else {
      if (!confirm("Save changes to block list?")){
        e.target.blur();
        return;
      }
    }
  }
  var slist, i, sp, ttemp, ptemp;
  slist = document.getElementById("ghhsitelist");
  ttemp = "";
  ptemp = "";
  for (i=0;i<slist.children.length;i++){
    if (slist.children[i].nodeName == "LI") {
      sp = slist.children[i].children[1];
      switch (sp.className){
        case "ghhhost ghhblk":
          ttemp += sp.textContent + ":t|";
          break;
        case "ghhhost ghhpb":
          ptemp += sp.textContent + ":p|";
          break;
        default:
          // to be unblocked
                          }
    }
  }
  slist = document.getElementById("ghhpbanlist");
  for (i=0;i<slist.children.length;i++){
    if (slist.children[i].nodeName == "LI") {
      sp = slist.children[i].children[1];
      switch (sp.className){
        case "ghhhost ghhblk":
          ttemp += sp.textContent + ":t|";
          break;
        case "ghhhost ghhpb":
          ptemp += sp.textContent + ":p|";
          break;
        default:
          // to be unblocked
                          }
    }
  }
  if (!GM4){
    GM_setValue("hideyhosts", "|" + ttemp + ptemp);
    blist = GM_getValue("hideyhosts");
  } else {
    await GM.setValue("hideyhosts", "|" + ttemp + ptemp);
    blist = await GM.getValue("hideyhosts");
  }
  hidehits(null,true);
  refreshSiteList();
  listchgs = 0;
  if (e) e.target.blur();
}
function refreshSiteList(){ // Rebuild lists for tabs 2 and 3
  var sarray, slist = '', pblist = '', ulB, ulP, i;
  if (blist.substr(0,1) != "|") blist = "|" + blist;
  sarray = blist.substr(1).split("|");
  for (i=0; i<sarray.length-1; i++){
    if (sarray[i].indexOf(":p")<0) {
      slist += '<li><span class="ghhinfo"></span><span class="ghhhost ghhblk">' + sarray[i].split(':')[0] + '</span></li>';
    } else {
      pblist += '<li><span class="ghhinfo"></span><span class="ghhhost ghhpb">' + sarray[i].split(':')[0] + '</span></li>';
    }
  }
  ulB = document.getElementById("ghhsitelist");
  while (ulB.firstChild) ulB.removeChild(ulB.firstChild);
  ulB.insertAdjacentHTML('beforeend', slist);
  ulP = document.getElementById("ghhpbanlist");
  while (ulP.firstChild) ulP.removeChild(ulP.firstChild);
  ulP.insertAdjacentHTML('beforeend', pblist);
  needupdate = false;
}
async function updtaddpos(e){ // Implement change for radio buttons re where to add to list
  var rads = e.target.parentNode.querySelectorAll("input[type='radio']");
  for (var i=0; i<rads.length; i++){
    if (rads[i].checked){
      if (rads[i].value == "sort"){
        if(confirm("Sort lists now? Sorting is irreversible.")){
          if (listchgs > 0) {
            if (confirm("You have unsaved changes to your lists. Save changes and sort, or cancel sorting?")){
              saveedits(null);
            } else {
              fixaddpos();
              return;
            }
          }
          sortlist(null);
        } else {
          fixaddpos();
          return;
        }
      }
      addAt = rads[i].value;
      ghhPrefO.addtolistpos[0] = addAt;
      if (!GM4){
        GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
      } else {
        await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
      }
      break;
    }
  }
  fixaddpos();
}
function fixaddpos(){ // Check appropriate radio button re where to add to list
  var rads = document.getElementById("addradios").querySelectorAll("input[type='radio']");
  for (i=0; i<rads.length; i++){
    if (rads[i].value == addAt){
      rads[i].setAttribute("checked","checked");
      rads[i].checked = true;
    }
    else{
      if (rads[i].hasAttribute("checked")){
        rads[i].removeAttribute("checked");
        rads[i].checked = false;
      }
    }
  }
}
async function updtaggress(e){ // Implement change for radio buttons re default domain to block
  var rads = e.target.parentNode.querySelectorAll("input[type='radio']");
  for (var i=0; i<rads.length; i++){
    if (rads[i].checked){
      bAggress = rads[i].value;
      ghhPrefO.aggressiveblock[0] = bAggress;
      if (!GM4){
        GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
      } else {
        await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
      }
      break;
    }
  }
  fixaggblock();
}
function fixaggblock(){ // Check appropriate radio button re default domain to block
  var rads = document.getElementById("aggressrads").querySelectorAll("input[type='radio']");
  for (i=0; i<rads.length; i++){
    if (rads[i].value == bAggress){
      rads[i].setAttribute("checked","checked");
      rads[i].checked = true;
    }
    else{
      if (rads[i].hasAttribute("checked")){
        rads[i].removeAttribute("checked");
        rads[i].checked = false;
      }
    }
  }
}
async function updtuistyle(e){ // Store settings for buttons to display
  var mbparts = mbstyle.split("-");
  if (mbparts.length == 1) mbparts.push("ifrN");
  if (mbparts.length == 2) mbparts.push("R");
  if (mbparts.length == 3) mbparts.push("P");
  if (mbparts.length == 4) mbparts.push("Y");
  if (mbparts.length == 5) mbparts.push("H");
  if (e.target.id == "mbiframe") { // Handle iframe checkbox
    var chk = e.target;
    if (chk.checked){
      mbparts[1] = "ifrY";
    } else {
      mbparts[1] = "ifrN";
    }
    mbstyle = mbparts.join("-");
    ghhPrefO.mngbtnstyle[0] = mbstyle;
    if (!GM4){
      GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
    } else {
      await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
    }
  } else { // Handle radio buttons
    if (e.target.getAttribute("name") == "uistyle"){
      var rads = e.target.parentNode.querySelectorAll("input[name='uistyle']");
      for (var i=0; i<rads.length; i++){
        if (rads[i].checked){
          switch (rads[i].value){
            case "blk":
              mbparts[0] = rads[i].value;
              document.getElementById("ghhMngBtn").parentNode.removeChild(document.getElementById("ghhMngBtn"));
              alert("After you close the management pane, click any block button to open it again.");
              break;
            case "mng":
              if(confirm("Display block buttons only when this dialog is open?")) mbparts[0] = "mng";
              else e.target.checked = false;
              break;
            default:
              mbparts[0] = "both";
              if (!document.getElementById("ghhMngBtn")) addMngBtn();
                               }
          mbstyle = mbparts.join("-");
          ghhPrefO.mngbtnstyle[0] = mbstyle;
          if (!GM4){
            GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
          } else {
            await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
          }
          break;
        }
      }
    } else { // Handle Management Button position and block button display style
      var rads = e.target.parentNode.querySelectorAll("input[name='mngbtnpos']");
      for (var i=0; i<rads.length; i++){
        if (rads[i].checked){
          mbparts[2] = rads[i].value;
          mbstyle = mbparts.join("-");
          ghhPrefO.mngbtnstyle[0] = mbstyle;
          if (!GM4){
            GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
          } else {
            await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
          }
          break;
        }
      }
      rads = e.target.parentNode.querySelectorAll("input[name='blockdisp']");
      for (i=0; i<rads.length; i++){
        if (rads[i].checked){
          mbparts[3] = rads[i].value;
          mbstyle = mbparts.join("-");
          ghhPrefO.mngbtnstyle[0] = mbstyle;
          if (!GM4){
            GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
          } else {
            await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
          }
          break;
        }
      }
      rads = e.target.parentNode.querySelectorAll("input[name='blockttip']");
      for (i=0; i<rads.length; i++){
        if (rads[i].checked){
          mbparts[4] = rads[i].value;
          mbstyle = mbparts.join("-");
          ghhPrefO.mngbtnstyle[0] = mbstyle;
          if (!GM4){
            GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
          } else {
            await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
          }
          break;
        }
      }
      rads = e.target.parentNode.querySelectorAll("input[name='blockposit']");
      for (i=0; i<rads.length; i++){
        if (rads[i].checked){
          mbparts[5] = rads[i].value;
          mbstyle = mbparts.join("-");
          ghhPrefO.mngbtnstyle[0] = mbstyle;
          if (!GM4){
            GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
          } else {
            await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
          }
          window.location.reload();
          break;
        }
      }
    }
  }
  fixuistyle();
}
function fixuistyle(){  // Check appropriate radio button re buttons to display
  if (mbstyle.split("-").length == 1) mbstyle = mbstyle + "-ifrN-R-P-Y-H";
  if (mbstyle.split("-").length == 2) mbstyle = mbstyle + "-R-P-Y-H";
  if (mbstyle.split("-").length == 3) mbstyle = mbstyle + "-P-Y-H";
  if (mbstyle.split("-").length == 4) mbstyle = mbstyle + "-Y-H";
  if (mbstyle.split("-").length == 5) mbstyle = mbstyle + "-H";
  var rads = document.getElementById("btnradios").querySelectorAll("input[name^='uistyle']");
  for (i=0; i<rads.length; i++){
    if (rads[i].value == mbstyle.split("-")[0]){
      rads[i].setAttribute("checked","checked");
      rads[i].checked = true;
    }
    else{
      if (rads[i].hasAttribute("checked")){
        rads[i].removeAttribute("checked");
        rads[i].checked = false;
      }
    }
  }
  var chk = document.getElementById("mbiframe");
  if (mbstyle.split("-")[1] == "ifrY"){
    chk.setAttribute("checked","checked");
    chk.checked = true;
  } else {
    chk.removeAttribute("checked");
    chk.checked = false;
  }
  var rads = document.getElementById("btnradios").querySelectorAll("input[name^='mngbtnpos']");
  for (i=0; i<rads.length; i++){
    if (rads[i].value == mbstyle.split("-")[2]){
      rads[i].setAttribute("checked","checked");
      rads[i].checked = true;
    }
    else{
      if (rads[i].hasAttribute("checked")){
        rads[i].removeAttribute("checked");
        rads[i].checked = false;
      }
    }
  }
  var rads = document.getElementById("btnradios").querySelectorAll("input[name^='blockdisp']");
  for (i=0; i<rads.length; i++){
    if (rads[i].value == mbstyle.split("-")[3]){
      rads[i].setAttribute("checked","checked");
      rads[i].checked = true;
    }
    else{
      if (rads[i].hasAttribute("checked")){
        rads[i].removeAttribute("checked");
        rads[i].checked = false;
      }
    }
  }
  var rads = document.getElementById("btnradios").querySelectorAll("input[name^='blockttip']");
  for (i=0; i<rads.length; i++){
    if (rads[i].value == mbstyle.split("-")[4]){
      rads[i].setAttribute("checked","checked");
      rads[i].checked = true;
    }
    else{
      if (rads[i].hasAttribute("checked")){
        rads[i].removeAttribute("checked");
        rads[i].checked = false;
      }
    }
  }
  var rads = document.getElementById("btnradios").querySelectorAll("input[name^='blockposit']");
  for (i=0; i<rads.length; i++){
    if (rads[i].value == mbstyle.split("-")[5]){
      rads[i].setAttribute("checked","checked");
      rads[i].checked = true;
    }
    else{
      if (rads[i].hasAttribute("checked")){
        rads[i].removeAttribute("checked");
        rads[i].checked = false;
      }
    }
  }
  toggleciteline(mbstyle.split("-")[5]);
}
async function updtAJAX(e){ // Store settings for AJAX preferences
  var chk = e.target;
  if (chk.id == "chkajax"){
    if (chk.checked){
      bAJAX = "on";
      if (chgMon) chgMon.disconnect();
      else document.body.removeEventListener("DOMSubtreeModified", checkOlist, false);
      setMutationWatch();
    } else {
      bAJAX = "off";
      if (chgMon) chgMon.disconnect();
      else document.body.removeEventListener("DOMSubtreeModified", checkOlist, false);
    }
  } else {
    if (chk.checked){
      bMutOb = "Y";
      if (!chgMon){
        if (bAJAX){
          document.body.removeEventListener("DOMSubtreeModified", checkOlist, false);
          setMutationWatch();
        }
      }
    } else {
      bMutOb = "N";
      if (chgMon) chgMon.disconnect();
      if (bAJAX){
        document.body.removeEventListener("DOMSubtreeModified", checkOlist, false);
        setMutationWatch();
      }
    }
  }
  ghhPrefO.usemutation[0] = bAJAX + "-" + bMutOb;
  if (!GM4){
    GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
  } else {
    await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
  }
  fixajaxstyle();
}
function fixajaxstyle(){  // Check boxes for AJAX preferences
  var chk = document.getElementById("chkajax");
  if (bAJAX == "on"){
    chk.setAttribute("checked","checked");
    chk.checked = true;
  } else {
    chk.removeAttribute("checked");
    chk.checked = false;
  }
  var chk = document.getElementById("chkdom4");
  if (bMutOb == "Y"){
    chk.setAttribute("checked","checked");
    chk.checked = true;
  } else {
    chk.removeAttribute("checked");
    chk.checked = false;
  }
}
async function updtpersist(e){ // Store setting for persistence preference
  var chk = e.target;
  if (chk.checked){
    mpopen = "Y" + mpopen.substr(1);
  } else {
    mpopen = "N" + mpopen.substr(1);
  }
  ghhPrefO.mngpaneopen[0] = mpopen;
  if (!GM4){
    GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
  } else {
    await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
  }
  fixpanepersist();
}
function fixpanepersist(){  // Check box for persistence preference
  var chk = document.getElementById("chkmpopen");
  if (mpopen.substr(0,1) == "Y"){
    chk.setAttribute("checked","checked");
    chk.checked = true;
  } else {
    chk.removeAttribute("checked");
    chk.checked = false;
  }
}
async function updt1click(e){ // Store setting for 1-click preferences
  var chk = e.target;
  if (chk.id == "chk1click" || chk.id == "chk1clickbf"){
    if (chk.checked){
      pref1click = "Y" + pref1click.substr(1,2);
    } else {
      pref1click = "N" + pref1click.substr(1,2);
    }
  } else {
    if (chk.checked){
      pref1click = pref1click.substr(0,2) + "Y";
    } else {
      pref1click = pref1click.substr(0,2) + "N";
    }
  }
  ghhPrefO.oneclick[0] = pref1click;
  if (!GM4){
    GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
  } else {
    await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
  }
  e.stopPropagation();
  fix1clickstyle();
}
function fix1clickstyle(){  // Check boxes for one-click preferences
  var chkMP = document.getElementById("chk1click");
  var chkBF = document.getElementById("chk1clickbf");
  if (pref1click.substr(0,1) == "Y"){
    chkMP.setAttribute("checked","checked");
    chkMP.checked = true;
    if (chkBF){
      chkBF.setAttribute("checked","checked");
      chkBF.checked = true;
    }
  } else {
    chkMP.removeAttribute("checked");
    chkMP.checked = false;
    if (chkBF){
      chkBF.removeAttribute("checked");
      chkBF.checked = false;
    }
  }
  chk = document.getElementById("chk1pban");
  if (pref1click.substr(2,1) == "Y"){
    chk.setAttribute("checked","checked");
    chk.checked = true;
  } else {
    chk.removeAttribute("checked");
    chk.checked = false;
  }
}
async function updtBeta(e){ // Store setting for runbeta preference
  var chk = e.target;
  if (chk.checked){
    betatest = "Y";
  } else {
    betatest = "N";
  }
  ghhPrefO.runbeta[0] = betatest;
  if (!GM4){
    GM_setValue("ghhprefs", JSON.stringify(ghhPrefO));
  } else {
    await GM.setValue("ghhprefs", JSON.stringify(ghhPrefO));
  }
  fixBeta();
}
function fixBeta(){  // Check box for runbeta preference
  var chk = document.getElementById("chkbeta");
  if (betatest == "Y"){
    chk.setAttribute("checked","checked");
    chk.checked = true;
  } else {
    chk.removeAttribute("checked");
    chk.checked = false;
  }
}
async function chgcaption(e){ // Store button caption changes (but do not immediately refresh)
  var btn, key, input;
  btn = e.target;
  key = e.target.getAttribute("key");
  e.target.blur();
  input = prompt(txts[key][1], txts[key][0]);
  if (!input) return;
  if (input.length > 0 && input != txts[key][0]){
    txts[key][0] = input.replace(/\"/g,"''");
    btn.appendChild(document.createTextNode(txts[key][0]));
    btn.removeChild(btn.firstChild);
    if (!GM4){
      GM_setValue("textstrings", JSON.stringify(txts));
    } else {
      await GM.setValue("textstrings", JSON.stringify(txts));
    }
  }
}
async function resetTextStrings(e){ // Reset buttons captions to defaults
  if (confirm("Restore default button captions?")){
    txts = defaultTxts;
    if (!GM4){
      GM_setValue("textstrings", JSON.stringify(txts));
    } else {
      await GM.setValue("textstrings", JSON.stringify(txts));
    }
    alert("Please reload to see the changes.");
    e.target.blur();
  }
}
async function exportlist(e){ // Display and populate export form, clean up from any prior use
  if (!document.getElementById("ghhexport")) insertExportForm();
  var expDiv = document.getElementById("ghhexport");
  document.getElementById("ghheximhead").innerHTML = "Export Block List";
  document.getElementById("ghheximinfo1").innerHTML = "These boxes display your current block list. " +
    "<button type=\"button\" id=\"expgotopreimp\" style=\"display:none\">Show old block list (prior to last import)</button><br /><br />" +
    "On the left, you have the list in its native format. By saving this format, you can preserve your regular/Perma-ban " +
    "block decisions. <br /><br />On the right, you have a simple list of domains. " +
    "This would be a good format for sharing your list with others.";
  if (!GM4){
		var currlist = GM_getValue("hideyhosts");
  } else {
    var currlist = await GM.getValue("hideyhosts");
  }
  document.getElementById("ghhtaleft").value = currlist;
  var domList = currlist.substr(1).replace(/:[tp]\|/g, "\n");
  document.getElementById("ghhtaright").value = domList.replace(/\n*$/, "");
  if (!GM4){
    var preimpolist = GM_getValue("hideyback", "");
  } else {
    var preimpolist = await GM.getValue("hideyback", "");
  }
  if (preimpolist.length > 0){
    document.getElementById("expgotopreimp").addEventListener("click",exportoldlist,true);
    document.getElementById("expgotopreimp").style.display = "";
  }
  document.getElementById("ghhleftcontrols").style.display = "none";
  document.getElementById("ghhrightcontrols").style.display = "none";
  document.getElementById("ghhtbldiv").style.display = "none";
  if (document.getElementById("ghhtaright").style.display == "none") document.getElementById("ghhtaright").style.display = "";
  expDiv.style.display = "block";
  e.target.blur();
}
function insertExportForm(){
  var dNew, btn, par, ta;
  dNew = document.createElement("div");
  dNew.id = "ghhexport";
  dNew.className = "ghhpane";
  dNew.setAttribute("style","position:fixed;top:10px;left:5%;width:90%;z-index:3002;background:#ddd;padding:1em;font-size:1.25em;display:none");
  dNew.innerHTML = "<button type=\"button\" onclick=\"this.parentNode.style.display='none'\" style=\"float: right; margin: 0 0 4px 4px;\" class=\"ghhider\">Close</button>" +
    "<p style=\"margin-top:0; font-weight: bold;\" id=\"ghheximhead\"></p>" +
    "<p id=\"ghheximinfo1\"></p>" +
    "<div id=\"ghhleft\" style=\"width:49%;float:left\"><textarea id=\"ghhtaleft\" " +
    "spellcheck=\"false\" style=\"width:100%;height:" + (0.6*window.innerHeight) + "px;overflow-y:scroll\"></textarea>" +
    "<div id=\"ghhleftcontrols\" style=\"clear:left;display:none\"><p><button type=\"button\" id=\"ghhexp1\">Parse List for Import</button></p></div></div>" +
    "<div id=\"ghhright\" style=\"width:49%;float:right\"><textarea id=\"ghhtaright\" " +
    "spellcheck=\"false\" style=\"width:100%;height:" + (0.6*window.innerHeight) + "px;overflow-y:scroll\"></textarea>" +
    "<div id=\"ghhtbldiv\" style=\"height:" + (0.58*window.innerHeight) + "px;overflow-y:scroll;overflow-x:scroll;background:#fff;padding:4px 0 0 4px;border:1px solid #aac;margin-top:1px;display:none\"></div> " +
    "<div id=\"ghhrightcontrols\" style=\"clear:right;display:none\"><p id=\"impradios\">Please review the above list for accuracy. If correct, add domains to: <br>" +
    "<label><input type=\"radio\" name=\"impbtype\" value=\"asis\">&nbsp;the list specified under Block Type</label> <br />" +
    "<label><input type=\"radio\" name=\"impbtype\" value=\"t\">&nbsp;the regular block list</label> <br />" +
    "<label><input type=\"radio\" name=\"impbtype\" value=\"p\">&nbsp;the Perma-ban list</label> &nbsp; " +
    "<button type=\"button\" id=\"ghhexp2\">Import</button> &nbsp; <span style=\"float:right; font-style:italic; opacity:0.8;\">Replace entire blocklist:&nbsp;<input type=\"checkbox\" id=\"chkimporepl\"></span></p></div></div>";
  document.body.appendChild(dNew);
}
function importlist(e){ // Display import form, clean up from any prior use
  if (!document.getElementById("ghhexport")) insertExportForm();
  var expDiv = document.getElementById("ghhexport");
  document.getElementById("ghheximhead").innerHTML = 'Import Block List';
  document.getElementById("ghheximinfo1").innerHTML = "<strong>As a precaution in case something goes wrong, please use the <button type=\"button\" id=\"impgotoexp\">Export</button> " +
    "feature to copy and save your current list as a backup.</strong> <br /><br />" +
    "To begin, paste your list into the left box below. Then click the Parse List for Import button. This script can import a list in its own native format, or a plain list of domains with a separate domain on each line, or " +
    "separated by spaces. (It also converts the Noise Reduction for Google and Google Domain Blocker formats.)";
  document.getElementById("ghhtaleft").value = "";
  document.getElementById("ghhleftcontrols").style.display = "";
  document.getElementById("ghhrightcontrols").style.display = "none";
  document.getElementById("ghhexp1").addEventListener("click",parseList,true);
  document.getElementById("impgotoexp").addEventListener("click",exportlist,true);
  document.getElementById("ghhtaright").style.display = "none";
  document.getElementById("ghhtbldiv").style.display = "none";
  document.getElementById("chkimporepl").checked = false;
  expDiv.style.display = "block";
  e.target.blur();
}
function parseList(e){  // Parse putative domain list and redisplay cleaned up
  var txt, sites = [], bHasTypes = 0, i, tbod, thd, rasis, lbpos, rbpos;
  txt = document.getElementById("ghhtaleft").value;
  if (txt.length < 4){
    alert("Block list too short!");
    return;
  }
  document.getElementById("ghhtbldiv").innerHTML = "";
  // clean up/convert domain list to pipe-delimited
  txt = txt.replace(/(http|https):/g, "");
  txt = txt.replace(/(,|\/|;)/g, "|");
  txt = txt.replace(/\s+/g, "|");
  txt = txt.replace(/\|+/g, "|");
  txt = txt.replace(/[\<\>"'=#\!\u2018\u2019\(\)\{\}]/g, "");
  // strip regex
  txt = txt.replace(/(\+|\*|\$|\\)/g, "");
  while (txt.indexOf("[") > -1 && txt.indexOf("]") > -1){
    lbpos = txt.indexOf("[");
    rbpos = txt.indexOf("]")
    if (lbpos > 0 && rbpos + 1 < txt.length) txt = txt.substring(0,lbpos) + txt.substring(rbpos+1);
    else {
      if (lbpos == 0 && rbpos + 1 < txt.length) txt = txt.substring(rbpos+1);
      else break; // for some reason, entire list is bracketed??
    }
  }
  if (txt.indexOf(":") > -1) bHasTypes = 1;
  sites = txt.split("|");
  for (i=0; i<sites.length; i++){
    if (sites[i].length > 1){
      if (sites[i].indexOf(".") == 0) sites[i] = sites[i].substr(1);
      if (sites[i].indexOf("?") > -1) sites[i] = sites[i].substr(0,sites[i].indexOf("?"));
      if (bHasTypes == 1){
        if (sites[i].indexOf(":t") == sites[i].length - 2 || sites[i].indexOf(":p") == sites[i].length - 2){
          sites[i] = "<tr><td>" + sites[i].replace(":t","</td><td>regular").replace(":p","</td><td>Perma-ban") + "</td></tr>";
        } else {
          if (sites[i].indexOf(":") > -1) sites[i] = sites[i].substr(0, sites[i].indexOf(":"));
          sites[i] = "<tr><td>" + sites[i] + "</td><td>(unspecified)</td></tr>";
        }
      } else { // Plain list
        sites[i] = "<tr><td>" + sites[i] + "</td></tr>";
      }
    }
  }
  tbod = "<tbody>\n" + sites.join("\n") + "</tbody>";
  if (sites.length == 0){
    alert("Unable to parse the list, sorry."); return;
  }
  if (bHasTypes == 1) thd  = "<thead><tr><th>Domain</th><th>Block Type</th></tr></thead>";
  else thd  = "<thead><tr><th>Domain</th></tr></thead>";
  document.getElementById("ghhtbldiv").innerHTML = "<table cellspacing=\"0\" class=\"ghhtbl\" id=\"ghhparsed\">" + thd + tbod + "</table>";
  document.getElementById("ghhtbldiv").style.display = "";
  rasis = document.getElementById("ghhrightcontrols").querySelectorAll("input[value='asis']")[0];
  if (bHasTypes == 1){
    if (rasis.hasAttribute("disabled")) rasis.removeAttribute("disabled");
    rasis.checked = true;
    rasis.parentNode.style.color = "";
  } else {
    rasis.setAttribute("disabled","disabled");
    rasis.parentNode.style.color = "rgb(172, 168, 153)";
    document.getElementById("ghhrightcontrols").querySelectorAll("input[value='t']")[0].checked = true;
  }
  document.getElementById("ghhrightcontrols").style.display = "block";
  document.getElementById("ghhexp2").addEventListener("click",doImport,true);
  e.target.blur();
}
async function doImport(e){ // Add sites from cleaned up domain list to script block lists
  var tbl, rads, i, typeRule, rows, dom, newDoms = "";
  tbl = document.getElementById("ghhparsed");
  if (!tbl){
    alert("Unable to locate table of parsed domains!");
    return;
  }
  if (tbl.parentNode.style.display == "none"){
    alert("Please start the import process again!");
    return;
  }
  rads = document.getElementById("ghhrightcontrols").querySelectorAll("input[type='radio']");
  for (i=0; i<rads.length; i++){
    if (rads[i].checked){
      typeRule = rads[i].value;
      break;
    }
  }
  rows = tbl.getElementsByTagName("tbody")[0].getElementsByTagName("tr");
  for (i=0; i<rows.length; i++){
    dom = rows[i].children[0].textContent;
    if (dom.lastIndexOf(".") < dom.length-2 && dom.indexOf(".") > 0){
      switch (typeRule){
        case "asis":
          if (rows[i].children[1].textContent == "Perma-ban") newDoms += dom + ":p|";
          else newDoms += dom + ":t|";
          break;
        default:
          newDoms += dom + ":" + typeRule + "|";
                      }
      rows[i].style.backgroundColor = "#ff0";
    } else {
      rows[i].style.backgroundColor = "#f00";
    }
  }
  if (newDoms != ""){
    // Back up current block list
    if (!GM4){
      GM_setValue("hideyback", blist);
    } else {
      await GM.setValue("hideyback", blist);
    }
    if (document.getElementById("chkimporepl").checked == true){
      if (confirm("Delete current block list and replace it with domains you are importing? (To add to the current block list, click Cancel.)")) {
        blist = "";
      }
    }
    if (blist == "") blist = "|" + newDoms;
    else blist += newDoms;
    // Persist updated block list
    if (!GM4){
      GM_setValue("hideyhosts", blist);
    } else {
      await GM.setValue("hideyhosts", blist);
    }
    if(document.getElementById("ghhmngform").style.display=="block") refreshSiteList();
    hidehits(null,true);
  }
  alert("Import of yellow-highlighted domains completed. Please check the Management Pane to " +
        "view, sort, and/or de-duplicate your imported domains.");
}
async function exportoldlist(e){ // Display and populate export form with pre-import list
  if (!document.getElementById("ghhexport")) insertExportForm();
  var expDiv = document.getElementById("ghhexport");
  document.getElementById("ghheximhead").innerHTML = "Export Old (Pre-Import) Block List";
  document.getElementById("ghheximinfo1").innerHTML = "These boxes display your old block list from before the last import. " +
    "<button type=\"button\" id=\"expgotoblist\">Show current block list</button><br /><br />" +
    "On the left, you have the list in its native format. By saving this format, you can preserve your regular/Perma-ban " +
    "block decisions. <br /><br />On the right, you have a simple list of domains. " +
    "This would be a good format for sharing your list with others.";
  if (!GM4){
    var preimpolist = GM_getValue("hideyback", "");
  } else {
    var preimpolist = await GM.getValue("hideyback", "");
  }
  document.getElementById("ghhtaleft").value = preimpolist;
  var domList = preimpolist.substr(1).replace(/:[tp]\|/g, "\n");
  document.getElementById("ghhtaright").value = domList.replace(/\n*$/, "");
  document.getElementById("expgotoblist").addEventListener("click",exportlist,true);
  document.getElementById("ghhleftcontrols").style.display = "none";
  document.getElementById("ghhrightcontrols").style.display = "none";
  document.getElementById("ghhtbldiv").style.display = "none";
  if (document.getElementById("ghhtaright").style.display == "none") document.getElementById("ghhtaright").style.display = "";
  expDiv.style.display = "block";
  e.target.blur();
}
async function sortlist(e){ // Alpha-sort block list
  if (listchgs > 0) {
    if (confirm("You have unsaved changes to your lists. Save changes and sort, or cancel sorting?")){
      saveedits(null);
    } else {
      return;
    }
  }
  if (blist.substr(0,1) != "|") blist = "|" + blist;
  var sarray = blist.substr(1,blist.length-2).split("|");
  sarray.sort();
  // Persist sorted list
  if (!GM4){
    GM_setValue("hideyhosts", "|" + sarray.join("|") + "|");
    blist = GM_getValue("hideyhosts");
  } else {
    await GM.setValue("hideyhosts", "|" + sarray.join("|") + "|");
    blist = await GM.getValue("hideyhosts");
  }
  refreshSiteList();
  if (e) e.target.blur();
}
async function dedup(e){  // De-duplicate block lists
  if (!confirm("If you block example.com, you don't also need to block www.example.com. Remove unnecessary domains from the block list?")) return;
  var barray, i, j, iadd, smain, stest, sremd = "", sques = "";
  if (blist.substr(0,1) != "|") blist = "|" + blist;
  barray = blist.substr(1,blist.length-2).split("|");
  for (i=0; i<barray.length; i++){
    if (barray[i].indexOf(":t") > -1){
      barray[i] = barray[i].substr(0,barray[i].indexOf(":")).split(".").reverse().join(".") + "!t";
    } else {
      if (barray[i].indexOf(":p") > -1){
        barray[i] = barray[i].substr(0,barray[i].indexOf(":")).split(".").reverse().join(".") + "!p";
      } else {
        barray[i] = barray[i].split(".").reverse().join(".") + "!t";
      }
    }
  }
  barray.sort();
  for (i=0; i<barray.length-1; i++){
    iadd = 0;
    for (j=1; j<barray.length-i; j++){
      if (barray[i+j].indexOf(barray[i].substr(0,barray[i].length-2)) != 0) break;
      smain = barray[i].substr(0,barray[i].length-2).split(".").reverse().join(".");
      stest = barray[i+j].substr(0,barray[i+j].length-2).split(".").reverse().join(".");
      if (stest.indexOf(smain) < 0) break;
      if (barray[i].substr(barray[i].length-1) == barray[i+j].substr(barray[i+j].length-1)){
        blist = blist.replace(stest + ":" + barray[i+j].substr(barray[i+j].length-1) + "|", "");
        sremd += "|Removed: " + stest + "; Covered by: " + smain;
        iadd += 1;
      } else {
        stest += (barray[i+j].substr(barray[i+j].length-1) == "t") ? " (regular)" : " (permaban)";
        smain += (barray[i].substr(barray[i].length-1) == "t") ? " (regular)" : " (permaban)";
        sques += "|Didn't remove " + stest + " due to block type difference from " + smain;
      }
    }
    i += iadd;
  }
  if (!GM4){
    GM_setValue("hideyhosts", blist);
  } else {
    await GM.setValue("hideyhosts", blist);
  }
  refreshSiteList();
  // ToDo: Alerts are temporary; nicer display "some day"
  if (sremd != "") alert(sremd.substr(1).replace(/\|/g,"\n"));
  if (sques != "") alert(sques.substr(1).replace(/\|/g,"\n"));
  if (sremd == "" && sques == "") alert("No unnecessary domains found.");
  if (e) e.target.blur();
}
async function unwww(e){  // Remove www from beginnings of domains
  if (!confirm("You can block other subdomains on example.com by removing www from the beginning (e.g., blog.example.com). Update the block list?")) return;
  if (blist.substr(0,1) != "|") blist = "|" + blist;
  blist = blist.replace(/\|www\./g, "\|");
  if (!GM4){
    GM_setValue("hideyhosts", blist);
  } else {
    await GM.setValue("hideyhosts", blist);
  }
  refreshSiteList();
  if (e) e.target.blur();
}
// Misc functions
function convertFormat(){
  if (GM4) return; //Legacy only
  if (blist.substr(0,1) != "|") blist = "|" + blist;
  blist = "|" + blist.slice(1).replace(/\|/g,":t|");
  GM_setValue("hideyhosts", blist);
}
function convertTxts(strTxts){
  var oldTxts;
  oldTxts = JSON.parse(strTxts);
  txts = defaultTxts;
  if (GM4) return; //Legacy only
  if (txtsPref.indexOf(":[") == -1){  // 0.8x to 0.9x+
    txts.block[0] = oldTxts.block;
    txts.unblock[0] = oldTxts.unblock;
    txts.pban[0] = oldTxts.pban;
    txts.okbtn[0] = oldTxts.okbtn;
    txts.cancelbtn[0] = oldTxts.cancelbtn;
    txts.savebtn[0] = oldTxts.savebtn;
    txts.closebtn[0] = oldTxts.closebtn;
  } else {  // 0.9x to 1.1x+
    txts.block[0] = oldTxts.block[0];
    txts.unblock[0] = oldTxts.unblock[0];
    txts.pban[0] = oldTxts.pban[0];
    txts.okbtn[0] = oldTxts.okbtn[0];
    txts.cancelbtn[0] = oldTxts.cancelbtn[0];
    txts.savebtn[0] = oldTxts.savebtn[0];
    txts.closebtn[0] = oldTxts.closebtn[0];
    if (oldTxts.okPbtn) txts.okPbtn[0] = oldTxts.okPbtn[0];
    if (oldTxts.cancelMbtn) txts.cancelMbtn[0] = oldTxts.cancelMbtn[0];
    if (oldTxts.mngbtn) txts.mngbtn[0] = oldTxts.mngbtn[0];
    if (txts.savebtn[0]=="Save Changes") txts.savebtn[0]="Save Lists"; // v1.1
    // 1.1 to 1.2+
    if (oldTxts.eximbtn) txts.eximbtn[0] = oldTxts.eximbtn[0];
    // 1.2 to 1.3+
    if (oldTxts.utilbtn) txts.utilbtn[0] = oldTxts.utilbtn[0];
    if (oldTxts.sortbtn) txts.sortbtn[0] = oldTxts.sortbtn[0];
    if (oldTxts.unwwwbtn) txts.unwwwbtn[0] = oldTxts.unwwwbtn[0];
    if (oldTxts.dedupbtn) txts.dedupbtn[0] = oldTxts.dedupbtn[0];
    // 2.0.9+ (catch-up)
    if (oldTxts.onetime) txts.onetime[0] = oldTxts.onetime[0];
    if (oldTxts.shownotc) txts.shownotc[0] = oldTxts.shownotc[0];
    if (oldTxts.hidenotc) txts.hidenotc[0] = oldTxts.hidenotc[0];
    if (oldTxts.impobtn) txts.impobtn[0] = oldTxts.impobtn[0];
    if (oldTxts.sharebtn) txts.sharebtn[0] = oldTxts.sharebtn[0];
  }
  GM_setValue("textstrings", JSON.stringify(txts)); // requires Fx 3.5+
}
function ghhkillevent(e){
  if (e.currentTarget.nodeName == "BUTTON" || e.currentTarget.nodeName == "INPUT") return;
  e.stopPropagation();
}
function toggleBlockHiders(str){
  var s = document.getElementById("ghhStyleNoBlock");
  if (str == "S"){
    if (s) s.parentNode.removeChild(s);
    return;
  }
  if (str == "H"){
    if (s) return;
    s = document.createElement("style");
    s.id = "ghhStyleNoBlock";
    s.setAttribute("type", "text/css");
    s.appendChild(document.createTextNode(".ghhb{display:none}"));
    document.body.appendChild(s);
  }
}
function refreshListeners(e){ // for AutoPager extension
  var bbtns, bnotc, i, j;
  if (!document.getElementById("navcnt")) return;
  bbtns = document.getElementById("navcnt").querySelectorAll(".ghhb");
  for (i=0;i<bbtns.length;i++){
    bbtns[i].removeEventListener("click",showbfd,true);
    bbtns[i].addEventListener("click",showbfd,true);
  }
  bnotc = document.getElementById("navcnt").querySelectorAll(".ghhd");
  for (i=0;i<bnotc.length;i++){
    bnotc[i].removeEventListener("click",reshow,true);
    bnotc[i].addEventListener("click",reshow,true);
    bbtns = bnotc[i].querySelectorAll("button.ghhider");
    for (j=0;j<bbtns.length;j++){
      if (bbtns[j].getAttribute("title")=="Unblock this site"){
        bbtns[j].removeEventListener("click",unblock,true);
        bbtns[j].addEventListener("click",unblock,true);
      }
      if (bbtns[j].getAttribute("title")=="Permanently hide this site"){
        bbtns[j].removeEventListener("click",permban,true);
        bbtns[j].addEventListener("click",permban,true);
      }
      if (bbtns[j].getAttribute("title")=="Re-hide this hit"){
        bbtns[j].removeEventListener("click",rehide,true);
        bbtns[j].addEventListener("click",rehide,true);
      }
    }
  }
}
function convertPrefs(arrPrefs, allnew){
  ghhPrefO = arrPrefs;
  if (GM4) return; // Legacy only
  if (allnew == "true"){  // 1.3.7 to 1.4.x
    var tmp = GM_getValue("shownotc");
    if (tmp){
      if (tmp.length > 0) ghhPrefO.shownotc[0] = tmp;
      GM_deleteValue("shownotc");
    }
    tmp = GM_getValue("mngpaneopen");
    if (tmp){
      if (tmp.length > 0) ghhPrefO.mngpaneopen[0] = tmp;
      GM_deleteValue("mngpaneopen");
    }
    tmp = GM_getValue("mngbtnstyle");
    if (tmp) if (tmp.length > 0){
      if (tmp.indexOf("-")>-1) tmp = "both"; // default ancient pref
      ghhPrefO.mngbtnstyle[0] = tmp;
      GM_deleteValue("mngbtnstyle");
    }
    tmp = GM_getValue("addtolistpos");
    if (tmp){
      if (tmp.length > 0) ghhPrefO.addtolistpos[0] = tmp;
      GM_deleteValue("addtolistpos");
    }
    tmp = GM_getValue("aggressiveblock");
    if (tmp){
      if (tmp.length > 0) ghhPrefO.aggressiveblock[0] = tmp;
      GM_deleteValue("aggressiveblock");
    }
    tmp = GM_getValue("usemutation");
    if (tmp){
      if (tmp.length > 0) ghhPrefO.usemutation[0] = tmp;
      GM_deleteValue("usemutation");
    }
  } else {
    if (ghhPrefs.indexOf("reserved1")>-1){
      var oldPrefs = JSON.parse(ghhPrefs);
      ghhPrefO.shownotc[0] = oldPrefs.shownotc[0];
      ghhPrefO.mngpaneopen[0] = oldPrefs.mngpaneopen[0];
      ghhPrefO.mngbtnstyle[0] = oldPrefs.mngbtnstyle[0];
      ghhPrefO.addtolistpos[0] = oldPrefs.addtolistpos[0];
      ghhPrefO.aggressiveblock[0] = oldPrefs.aggressiveblock[0];
      ghhPrefO.usemutation[0] = oldPrefs.usemutation[0];
      ghhPrefO.oneclick[0] = oldPrefs.oneclick[0];
    }
  }
  GM_setValue("ghhprefs", JSON.stringify(ghhPrefO)); // requires Fx 3.5+
}
function togglebbtn(e){
  var bbtn = e.currentTarget.querySelector('.ghhb');
  if (bbtn){
    if (e.type == "mouseover") bbtn.style.visibility = "";
    else bbtn.style.visibility = "hidden";
  }
}
function reQuery(e){
  var ss, rads, i;
  if (e){
    if (e.target.id == "ghhbf5") ss = "+site:";
    else ss = "+-site:";
    rads = e.target.form.querySelectorAll('input[type="radio"]');
  } else {
    ss = "+-site:"; // ALT omit
    rads = document.querySelector('#ghhblockform form').querySelectorAll('input[type="radio"]');
  }
  if (rads.length > 0){
    for (var i=0; i<rads.length; i++){
      if(rads[i].checked){
        ss += rads[i].nextElementSibling.textContent;
        reQry(ss);
        break;
      }
    }
  } else console.log("LOG:reQuery fail: no rads");
}
function reQry(d){
  if (!d) return;
  var qsp = window.location.href.indexOf("?");
  if (qsp < 0) return;
  var q = window.location.href.substr(qsp+1);
  if (d.substr(0,2) == "+-" && (q.indexOf(d+"%20")>-1 || q.indexOf(d+"&")>-1)) return; // try to block dups, may be overinclusive
  var qa = q.split("&");
  var has_q = false
  for (var j=qa.length-1; j>=0; j--){
    if (qa[j].split("=")[0] == "q"){
      qa[j] += d;
      has_q = true;
      break;
    } else {
      if (qa[j].indexOf("#q=") > -1){
        qa[j] += d;
        has_q = true;
        break;
      }
    }
  }
  if (has_q) window.location.href = window.location.href.substr(0, window.location.href.indexOf("?")+1) + qa.join("&");
  else console.log("LOG:Unable to add new search term to URL");
}
function toggleciteline(posit) {
  var ghhbd_sty = document.getElementById("bbposciteline");
  if (posit == "C"){
    if (!ghhbd_sty){
      var ghhbd_sty = document.createElement("style");
      ghhbd_sty.id = "bbposciteline";
      ghhbd_sty.setAttribute("type", "text/css");
      document.body.appendChild(ghhbd_sty);
    }
    // "inline" the action menu
    ghhbd_sty.appendChild(document.createTextNode(".action-menu {vertical-align:baseline !important;} .action-menu .clickable-dropdown-arrow, .action-menu  .ab_button {display:none !important;} .action-menu-panel, .action-menu-panel ul, .action-menu-panel ol, .action-menu-item {display:inline !important; visibility: visible !important; border:none !important; box-shadow:none !important; background-color:transparent !important; margin:0  !important; padding:0 !important; top:0 !important; height:auto !important; line-height:auto !important;} .action-menu-item a.fl, .action-menu-button {padding:0 0 0 6px !important; display:inline !important;}  .action-menu-panel {position:static;} .action-menu-item a.fl:hover {text-decoration:underline !important;} .action-menu + .crc {margin-right: 9px !important;} .action-menu + .crc ._Bs {margin-left: 1px !important;}"));
    // restyle the block button
    ghhbd_sty.appendChild(document.createTextNode(".ghhb {border:none!important; text-decoration:none!important; font-size:1em!important; color:#333!important; padding:0!important; margin-left:8px!important;} .ghhb:hover {background:transparent!important; text-decoration:underline !important;}"));
  } else { // remove citeline rules
    if (ghhbd_sty){
      while(ghhbd_sty.firstChild) ghhbd_sty.removeChild(ghhbd_sty.firstChild);
    }
  }
}
function openCustomStyleBar(e){
  // Create fixed div with text input and buttons: Save, Test, Close
  var csb = document.getElementById("ghhcsb");
  if (csb){
    csb.style.display = "block";
  } else {
    csb = document.createElement("div");
    csb.id = "ghhcsb";
    csb.setAttribute("style","position:fixed;bottom:0;left:0;z-index:750;width:100%;background-color:#afa;");
    csb.innerHTML = "<form onsubmit=\"return false;\"><p style=\"margin:0.75em;\"><input id=\"ghhcsbrule\" type=\"text\" style=\"width:80%\"> " +
      "<button type=\"button\" id=\"ghhcsb1\" title=\"Save and Apply\">Save</button> " +
      "<button type=\"button\" id=\"ghhcsb2\" title=\"Test Current Rules\">Test</button> " +
      "<button type=\"button\" id=\"ghhcsb3\" title=\"Close\">Close</button></p></form>";
    document.body.appendChild(csb);
    document.getElementById("ghhcsb1").addEventListener("click",saveCustomStyle,true);
    document.getElementById("ghhcsb2").addEventListener("click",testCustomStyle,true);
    document.getElementById("ghhcsb3").addEventListener("click",closeCustomStyleBar,true);
  }
  document.getElementById("ghhcsbrule").value = custSty;
}
async function saveCustomStyle(e){
  // Update preferences and apply change to style#ghhbdcuststy
  custSty = document.getElementById("ghhcsbrule").value;
  if (!GM4){
    GM_setValue("hiderStyles", custSty);
  } else {
    await GM.setValue("hiderStyles", custSty);
  }
  document.getElementById("ghhbdcuststy").innerHTML = "";
  document.getElementById("ghhbdcuststy").appendChild(document.createTextNode(custSty));
}
function testCustomStyle(e){
  // Add/Edit style#ghhbdcuststy
  document.getElementById("ghhbdcuststy").innerHTML = "";
  document.getElementById("ghhbdcuststy").appendChild(document.createTextNode(document.getElementById("ghhcsbrule").value));
}
function closeCustomStyleBar(e){
  // Turn off display and reapply saved style to style#ghhbdcuststy
  document.getElementById("ghhcsb").style.display = "none";
  document.getElementById("ghhbdcuststy").innerHTML = "";
  document.getElementById("ghhbdcuststy").appendChild(document.createTextNode(custSty));
}
function removePBs(e){ // GoogleMonkeyR layout only
  // Schedule Permaban removal (prevent simultaneous/conflicting runs)
  var PBsBlanks = document.querySelectorAll("table#GTR li[blockhidden], table#GTR div.g[blockhidden], table#GTR td:empty");
  if (PBsBlanks.length < 1) return;
  if (t_pb) window.clearTimeout(t_pb);
  t_pb = window.setTimeout(GMRshuffle, 100);
}
function GMRshuffle(){ // GoogleMonkeyR layout only
  // Delete Permaban hits
  var PBs = document.querySelectorAll("table#GTR li[blockhidden], table#GTR div.g[blockhidden]");
  if (PBs.length > 0){
    for (var i=PBs.length; i>0; i--) PBs[i-1].remove();
  }
  // Check entire table for empty cells and shuffle contents
  var tbl, row, cell, empties;
  var tbl = document.getElementById("GTR");
  for (row=0; row<tbl.rows.length; row++){
    empties = tbl.rows[row].querySelectorAll("td:empty").length;
    if (empties > 0 && empties < tbl.rows[row].cells.length){
      for (cell=0; cell<tbl.rows[row].cells.length; cell++){
        if (tbl.rows[row].cells[cell].childNodes.length == 0){
          if (fillFromNext(tbl.rows[row].cells[cell]) == "STOP"){
            if (t_pb) window.clearTimeout(t_pb);
            t_pb = window.setTimeout(GMRshuffle, 1000);
            return;
          }
        }
      }
    }
  }
}
function fillFromNext(tgt){
  var src = getNextCell(tgt, true);
  if (!src) return "STOP";
  while (src.childNodes.length > 0) tgt.appendChild(src.childNodes[0]);
}
function getNextCell(aCell, blnNonEmpty){
  var startcell = aCell;
  var retcell;
  var i=0;
  while (i<1000) {
    if (startcell.nextElementSibling){ // not the last cell in the row
      retcell = startcell.nextElementSibling;
    } else {
      if (startcell.parentNode.nextElementSibling){ // last cell in row and there's another row
        retcell = startcell.parentNode.nextElementSibling.cells[0];
      } else {
        return null; // end of table
      }
    }
    if (!retcell){
      return null; // corrupted table structure
    }
    if (blnNonEmpty){
      if (retcell.querySelector("li")){
        return retcell;
      } else {
        startcell = retcell;
      }
    } else {
      return retcell;
    }
    i++
  }
}
// "Add All" feature 2.0.9
async function addAllNow(e){
  var unb = document.querySelectorAll('[ghhresult="unset"][ghhhost]'), dom = '', pdom = '', domlist = '';
  for (var i=0; i<unb.length; i++){
    // Compute domain based on user preference
    dom = unb[i].getAttribute('ghhhost');
    pdom = dom.substr(dom.indexOf('.') + 1);
    if (pdom.indexOf('.') > -1 && patIPv4.test(dom) != true){
      switch (bAggress){
        case 'all':
          dom = pdom; break;
        case 'www':
          if (dom.substr(0,3) == 'www') dom = pdom; break;
        default:
          // default to full domain
      }
    }
    // Add dom to doms arrray (avoiding duplicates)
    if (doms.includes(dom) !== true) doms.push(dom);
  }
  // Add new domains to the currently displayed block list
  if (document.querySelector('button.ghhCurTab').id == 'ghhts3'){ // pban
    domlist = doms.join(':p|') + ':p';
  } else { // regular
    domlist = doms.join(':t|') + ':t';
  }
  if (blist.substr(0,1) != '|') blist = '|' + blist;
  if (addAt == 'end') blist += domlist + '|';
  else blist = '|' + domlist + blist;
  needupdate = true;
  // Store the list
  if (!GM4){
    GM_setValue('hideyhosts', blist);
  } else {
    await GM.setValue('hideyhosts', blist);
  }
  // Apply the change to the results
  hidehits(null,true);
  if (document.getElementById('GTR')) removePBs();
  // Update the dialog
  if (addAt == 'sort') sortlist(null);
  refreshSiteList();
}

/// ustometric.js
var _US_to_Metric_regexps = {
    miles_per_hour: [
        /((?:\.[0-9]|[0-9])[0-9., /]*)(\s|-)*m\.?p\.?h\.?(?=\W|$)/i,    /* 12.34 mph */
        /* 12.34 miles per hour */
        /((?:\.[0-9]|[0-9])[0-9., /]*)(\s|-)*miles?\s+per\s+hour(?=\W|$)/i
    ],
    inches: [
        /((?:\.[0-9]|[0-9])[0-9., /x]*)\s*(")/,                         /* 12.34" */
        /((?:\.[0-9]|[0-9])[0-9., /x]*)(\s|-)*in(ch)?(es)?(?=\W|$)/i    /* 12.34 inches */
    ],
    feet: [
        /((?:\.[0-9]|[0-9])[0-9., /x]*)(\s|-)*f(oo|ee)?t(?=\W|$)/i      /* 12.34 ft, 12-feet */
    ],
    yards: [
        /((?:\.[0-9]|[0-9])[0-9., /x]*)(\s|-)*y(ar)?ds?(?=\W|$)/i       /* 12.34 yds, 12.34 yards */
    ],
    miles: [
        /((?:\.[0-9]|[0-9])[0-9., /x]*)(\s|-)*mi(le)?s?(?=\W|$)/i       /* 12.34 miles */
    ],
    ounces: [
        /((?:\.[0-9]|[0-9])[0-9., /]*)(\s|-)*o(z|unces?)(?=\W|$)/i      /* 12 oz, 12 ounces */
    ],
    pounds: [
        /((?:\.[0-9]|[0-9])[0-9., /]*)(\s|-)*lbs?(?=\W|$)/i,            /* 12.34 lbs */
        /((?:\.[0-9]|[0-9])[0-9., /]*)(\s|-)*pounds?(?=\W|$)/i          /* 12.34 pounds */
    ],
    fluid_ounces: [
        /* 12 fl oz, 12 fluid ounces */
        /((?:\.[0-9]|[0-9])[0-9., /]*)(\s|-)*(u\.?s\.?\s)?fl(uid)?(\s|\.\s?)o(z|unces?)(?=\W|$)/i
    ],
    gallons: [
        /* 12.34 gal, 12.34 US gallon */
        /((?:\.[0-9]|[0-9])[0-9., /x]*)(\s|-)*(u\.?s\.?\s)?gal(lon)?(?=\W|$)/i
    ],
    fahrenheit: [
        /([-−]?[ ]*(?:\.[0-9]|[0-9])[0-9., /]*)\s*°\s*F(?=\W|$)/,       /* 34 °F */
        /* 34 degrees Fahrenheit */
        /([-−]?[ ]*(?:\.[0-9]|[0-9])[0-9., /]*)\s*deg(rees)?\s+f(ahrenheit)?(?=\W|$)/i
    ],
    next: [ ]
};

function _US_to_Metric_click(event)
{
    if (event.ctrlKey) {
        var t, nodes, switched = /_US_to_Metric_switched/.test(this.className);

        if (event.shiftKey)
            nodes = document.getElementsByClassName('_US_to_Metric_value');
        else
            nodes = [ this ];
            
        for (var i = 0; i < nodes.length; i++) 
            if (switched) {
                nodes[i].className = nodes[i].className.replace(' _US_to_Metric_switched', '');
                nodes[i].childNodes[0].nodeValue = nodes[i].title.split(/ = /)[0];
            }
            else {
                nodes[i].className = nodes[i].className.replace(' _US_to_Metric_switched', '');
                nodes[i].childNodes[0].nodeValue = nodes[i].title.split(/ = /)[1];
                nodes[i].className += ' _US_to_Metric_switched';
            }
        
        event.preventDefault();
        return false;
    }
}

function _US_to_Metric()
{
    var nodes, textNodes = [ ];
    var text, mode, r, pre, post, parent, span, t, tt, n, i;
    var regexps = _US_to_Metric_regexps;
    var excluded = { option: 1, script: 1, textarea: 1 };

    nodes = document.evaluate('//body//text()', document, null,
        XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null);
        
    for (i = 0; i < nodes.snapshotLength; i++)
        textNodes.push(nodes.snapshotItem(i));

    i = 0;

    while (i < textNodes.length) {
        if (textNodes[i].parentNode &&
            excluded[textNodes[i].parentNode.tagName.toLowerCase()])
        {
            i++;
            continue;
        }
    
        text = textNodes[i].nodeValue;

        if (!text || !text.match(/[0-9]/)) {
            i++;
            continue;
        }
        
        LOOP:
        for (mode in regexps)
            for (var j = 0; j < regexps[mode].length; j++)
                if (t = regexps[mode][j].exec(text))
                    break LOOP;

        if (mode == 'next') {
            i++;
            continue;
        }

        if (tt = t[1].match(/([0-9]+)\s+([0-9]+)\/([0-9]+)/))
            t[1] = (parseFloat(tt[1]) + tt[2] / tt[3]).toString();
            
        t[1] = t[1].replace(/\s+/g, '');
        t[1] = t[1].replace(',', '');
        t[1] = t[1].replace('−', '-');
        n = t[1].split(/x/);

        for (j = 0; j < n.length; j++)
            if (tt = n[j].match(/([0-9]+)\/([0-9]+)/))
                n[j] = tt[1] / tt[2];
                
        switch (mode) {
        case 'miles_per_hour':
            for (j = 0; j < n.length; j++)
                n[j] = (parseFloat(n[j]) * 1.609344).toFixed(2);
                
            r = n.join(' x ') + ' km/h';                
            break;            
        case 'inches':
            for (j = 0; j < n.length; j++)
                n[j] = (parseFloat(n[j]) * 2.54).toFixed(2);
                
            r = n.join(' x ') + ' cm';
            break;
        case 'feet':
            for (j = 0; j < n.length; j++)
                n[j] = (parseFloat(n[j]) * 0.3048).toFixed(2);
                
            r = n.join(' x ') + ' m';
            break;
        case 'yards':
            for (j = 0; j < n.length; j++)
                n[j] = (parseFloat(n[j]) * 0.9144).toFixed(2);
                
            r = n.join(' x ') + ' m';
            break;
        case 'miles':
            for (j = 0; j < n.length; j++)
                n[j] = (parseFloat(n[j]) * 1.609344).toFixed(2);
                
            r = n.join(' x ') + ' km';
            break;
        case 'ounces':
            for (j = 0; j < n.length; j++)
                n[j] = (parseFloat(n[j]) * 28.349523125).toFixed(2);
                
            r = n.join(' x ') + ' g';
            break;
        case 'pounds':
            for (j = 0; j < n.length; j++)
                n[j] = (parseFloat(n[j]) * 0.45359237).toFixed(2);
                
            r = n.join(' x ') + ' kg';
            break;
        case 'fluid_ounces':
            for (j = 0; j < n.length; j++)
                n[j] = (parseFloat(n[j]) * 29.57353).toFixed(2);
                
            r = n.join(' x ') + ' mL';
            break;
        case 'gallons':
            for (j = 0; j < n.length; j++)
                n[j] = (parseFloat(n[j]) * 3.78541178).toFixed(2);
                
            r = n.join(' x ') + ' L';
            break;
        case 'fahrenheit':
            for (j = 0; j < n.length; j++)
                n[j] = ((parseFloat(n[j]) - 32) * 5 / 9).toFixed(2);
            
            r = n.join(' x ') + ' °C';
            break;
        }
        
        pre = document.createTextNode(text.slice(0, text.indexOf(t[0])));
        post = document.createTextNode(text.slice(text.indexOf(t[0]) + t[0].length));

        span = document.createElement('span');
        span.appendChild(document.createTextNode(t[0]));
        t[0] = t[0].replace(/\s+/g, ' ');
        span.setAttribute('title', t[0] + ' = ' + r);
        span.className = '_US_to_Metric_value';
        span.style.cursor = 'pointer';
        span.addEventListener('click', _US_to_Metric_click, false);
        span.style.color = 'inherit';
        span.style.fontSize = 'inherit';
        span.style.fontWeight = 'inherit';

        parent = textNodes[i].parentNode;
        parent.replaceChild(post, textNodes[i]);
        parent.insertBefore(span, post);
        parent.insertBefore(pre, span);

        textNodes[i] = pre;
        textNodes.push(post);
    }
}
