function getDomain (URL) {
  var domain = "";
  var domainMode = false;
  URL = URL.toString();
  for (var c in URL){
    if(domainMode && URL[c] === "/"){
      domainMode === false;
      return domain;
    }
    if(domainMode){
      domain = domain + URL[c];
    }
    if(URL[c] === "/" && URL[c-1] === "/"){
      domainMode = true;
    }
  }
}
