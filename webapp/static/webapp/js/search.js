$(document).ready(function () {

  $('#filter_A').on('click', function (e) {
    e.preventDefault();
    window.location.href = window.location.href + '&nutri_filter=' + $(this).attr("value")
    // $.get("", { nutri_filter: $(this).attr("value") });
  });
  $('#filter_B').on('click', function (e) {
    e.preventDefault();
    window.location.href = window.location.href + '&nutri_filter=' + $(this).attr("value")
    // $.get("", { nutri_filter: $(this).attr("value") });
  });
  $('#filter_C').on('click', function (e) {
    e.preventDefault();
    window.location.href = window.location.href + '&nutri_filter=' + $(this).attr("value")
    // $.get("", { nutri_filter: $(this).attr("value") });
  });
  $('#filter_D').on('click', function (e) {
    e.preventDefault();
    window.location.href = window.location.href + '&nutri_filter=' + $(this).attr("value")
    // $.get("", { nutri_filter: $(this).attr("value") });
  });
  $('#filter_E').on('click', function (e) {
    e.preventDefault();
    window.location.href = window.location.href + '&nutri_filter=' + $(this).attr("value")
    // $.get("", { nutri_filter: $(this).attr("value") });
  });
});