$(document).ready(function () {

  $('save').on('click', function (e) {
    e.preventDefault();
    $.post(
      '/save',
      {
        question: $('#question input:text').val(),
      },
    )
  });
});