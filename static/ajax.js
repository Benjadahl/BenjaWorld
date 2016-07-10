function ajaxRequest (aUrl, aData) {
  console.log("ajaxbois");
  $.ajax({
    type: 'POST',
    // Provide correct Content-Type, so that Flask will know how to process it.
    contentType: 'application/json',
    // Encode your data as JSON.
    data: JSON.stringify(aData),
    // This is the type of data you're expecting back from the server.
    dataType: 'json',
    url: '/' + aUrl + '/',
    success: function (e) {
      updateStuff();
    }
  });
}
