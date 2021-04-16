
// ========================= FUNCTIOns ==============================

const popUpModal = function popUpModal($query) {

    const $modal = $query.parents(".modal");
    console.log($modal)

    // console.log("error")
    // here it is calling the on ready function, so that it will only show the pop up once is loaded and ready
    // example 
    // $( document ).ready(function() {
    //    modal.modal('show')
    // });
    // same thing
    $(() => $modal.modal('show'));

    
}


const $next = $("#login").siblings("input[name='next']");
console.log($next);
if($next.attr("value")){
    // console.log($next.attr("value"));
    popUpModal($next);
}

const $error = $(".errorlist")
console.log($error)
if ($error.length !== 0) {

    popUpModal($error);

    // const $modal = $error.parents(".modal");
    // console.log($modal)

    // console.log("error")
    // // here it is calling the on ready function, so that it will only show the pop up once is loaded and ready
    // // example 
    // // $( document ).ready(function() {
    // //    modal.modal('show')
    // // });
    // // same thing
    // $(() => $modal.modal('show'));
    
}


// not sure why this doesnt work
// modal.on('load', () => modal.modal('show'))


