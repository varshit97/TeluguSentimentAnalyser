
function myFunc()
{
  var val = document.getElementById('transliterateTextarea').value;
  console.log(val);
  document.getElementById('tempHello').innerHTML = val;
}

setInterval(myFunc,1000);
