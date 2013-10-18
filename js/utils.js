var utils = (function () {

    var dialogLoginerror = '#dialog-html-login';
    var dialogEvaliationError = '#dialog-html-evaluation';

    var checkEmail = function (val) {
        var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        return filter.test(val);
    };

    var isEmpty = function (val) {
        if (typeof val == 'string')
            return (val.trim() === '') ? true : false;
    };

    var setMsgDialogLogin = function (value) {
        $(dialogLoginerror).html(value);
    };

    var setMsgDialogEvalution = function (value) {
        $(dialogEvaliationError).html(value);
    };

    var openDialogLogin = function () {
        dialogLoginerror.dialog('open');
    };

    var upperFirst = function (txt) {
        var newTxt = '';
        if (txt && typeof txt == 'string') {
            newTxt = txt.charAt(0).toUpperCase() + txt.slice(1);
        }
        return newTxt;
    };

    var removeSpace = function(txt) {
        var newTxt = '';
        if (txt && typeof txt == 'string') {
            newTxt = txt.toLowerCase().replace(/\s/g, '');
        }
        return newTxt;
    };

    var cleanInputs = function(form) {
        $(form + ' input').each( function (index, elem) {
            $(elem).val('');
        });
    };

    var paddingText = function(aString, limit){
        if (!limit && typeof(limit) == "undefined") {
            limit = 40;
        }
        if (aString.length <= limit) {
            return aString;
        }
        var value = "";
        try {
            value = aString.substr(0, limit) + '... ';
        }
        catch (e) {
            if (aString.length > limit) {
                value = aString.substr(0, limit) + '... ';
            }
        }
        return value;
    };

    var isNumber = function(value) {
        return (/\D/.test(value));
    };


    return {
        checkEmail: checkEmail,
        isEmpty: isEmpty,
        setMsgDialogLogin: setMsgDialogLogin,
        setMsgDialogEvalution: setMsgDialogEvalution,
        upperFirst: upperFirst,
        removeEmpty: removeSpace,
        cleanInputs: cleanInputs,
        paddingText: paddingText,
        isNumber: isNumber
    };

})();
