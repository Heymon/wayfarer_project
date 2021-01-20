
modal = $("#signupModal");

console.log(modal);

const error = $(".error")
console.log(error)
if (error.length !== 0) {


    console.log("error")
    // here it is calling the on ready function, so that it will only show the pop up once is loaded and ready
    // example 
    // $( document ).ready(function() {
    //    modal.modal('show')
    // });
    // same thing
    $(() => modal.modal('show'));
    
}


// not sure why this doesnt work
// modal.on('load', () => modal.modal('show'))