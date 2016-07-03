function readCookie(cName){
  cookieSep = document.cookie.split(/;|=/);
  for(i = 0; i < cookieSep.length; i = i + 2){
    cookieSep[i] = cookieSep[i].replace(" ","")
    if(cookieSep[i] == cName){
      console.log("[CM] Read cookie " + cName + " as " + cookieSep[i + 1]);
      return cookieSep[i + 1]
    }
  }
}
