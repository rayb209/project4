var onClose = function() {
 alert("connection lost try to refresh");
  }

var onError = function() {
 alert("we have an error"); 
}
var cardel=document.getElementById("card");

var onMessage = function(message) {

  var otheruser = sessionStorage.otheruser; 
    
     b.innerHTML=message.data;


}


var onOpened = function() {
  //figure out otherusername

 if (sessionStorage.otheruser)
  {
     // nothing to do
     // 
  }
  else 
      {
          // if not set then prompt
         sessionStorage.otheruser = prompt("enter the other person's name, please ensure that the name is correct"");
         person2=sessionStorage.otheruser;
      }
   
    var currentuser = location.href.split('/').reverse()[0];
    var roomid = document.getElementById("roomid").innerHTML;
    var otheruser = sessionStorage.otheruser;
    var otheruserbox = document.getElementById("otheruser");
    otheruserbox.innerHTML = otheruser;
    var cardflip = document.getElementById("card");
   
    if (cardflip){
           cardflip.addEventListener("click", function(event) {
              event.preventDefault();
             // update the chatroom
             messagebox = b.innerHTML;
              
             // send a message using ajax to the server 
             sendMessage(otheruser,roomid,messagebox);
           
             
                         
                   // reset messagebox
            messagebox = "";

            });
        
    }
       }

var sendMessage = function(name,roomid,message) {
var xhr = new XMLHttpRequest();
  xhr.open('POST', '/sendmessage/' + name + '/' + roomid, true);
  xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  xhr.send("message="+message);
};