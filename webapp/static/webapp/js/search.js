$(document).ready(function () {
  $('.filter').on('click', function (e) {
    e.preventDefault();
    var currentUrl = location.href;
    var url = new URL(currentUrl);
    url.searchParams.set('nutri_filter', $(this).attr("value"));
    url.searchParams.set('page', 1);
    var newUrl = url.href;
    location.href = newUrl;
  });
});