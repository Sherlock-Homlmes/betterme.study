$(document).ready(function(){
  
  // display login form
  $('.welcome .primary').click(function(){
    $('.welcome').hide();
    $('form').fadeIn();
  });

  // display welcome
  $('form .minor').click(function(){
    $('form').hide();
    $('.welcome').fadeIn();
  });
  
  // form validation
  $('.field input').keyup(function(){
    var username = $.trim($('.field input[name=username]').val());
    var password = $.trim($('.field input[name=password]').val());
  
    if (username.length > 0 && password.length > 0 ) {
      $('form .primary').removeClass('disabled');
    } else {
      $('form .primary').addClass('disabled');
    }
  });
  
});