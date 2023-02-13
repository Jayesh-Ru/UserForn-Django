
window.onload=function(){
    //script kept getting loaded before the content hence, used window.onload();

var user_name = document.querySelector('.name');
var email = document.querySelector('.id_email');
var dob = document.querySelectorAll('.dob');


user_name.addEventListener('change', function(){

    if(user_name.value ==""){
        alert("User Name can't be empty");
    }
  });

email.addEventListener('change',function(){
    var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if(emailPattern.test(email.value)){
        console.log('correct input');
    }
    else if(email.value === ''){
        alert('email is required!. please provide an email')
    }
    else{
        alert('You must enter email in correct format: example@gmail.com');
    }
  });


dob[2].addEventListener('input',function(){
    if(getAge(dob)<18){
        alert('Only 18+ Users are allowed');
      }
  });


function getAge(dateString) {
    var today = new Date();
    var age = today.getFullYear() - dateString[2].value;
    var m = today.getMonth() - dateString[1].value;
    if (m < 0 || (m === 0 && today.getDate() < dateString[0].value)) {
        age--;
    }
    return age;
}

}