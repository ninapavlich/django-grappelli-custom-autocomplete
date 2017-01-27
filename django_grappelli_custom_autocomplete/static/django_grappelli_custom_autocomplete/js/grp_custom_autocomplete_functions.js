// GRAPPELLI CUSTOM AUTOCOMPLETE CUSTOM
function customRemoveRelatedObject(triggeringLink) {  
    var id = triggeringLink.id.replace(/^remove_/, '');
    var elem = document.getElementById(id);
    elem.value = "";
    django.jQuery(elem).parent().next('.grp-custom-extra-display').html('')
    elem.focus();
}
window.customRemoveRelatedObject = customRemoveRelatedObject;