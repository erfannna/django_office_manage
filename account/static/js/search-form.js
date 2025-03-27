jalaliDatepicker.updateOptions({"minDate": "attr"});
jalaliDatepicker.updateOptions({"maxDate": "attr"});

$(" #id_start_date ").change(function() {
    let minDate = $(this).val();
    $(" #id_end_date ").attr('data-jdp-min-date', minDate);

});
$(" #id_end_date ").change(function() {
    let maxDate = $(this).val();
    $(" #id_start_date ").attr('data-jdp-max-date', maxDate);

});