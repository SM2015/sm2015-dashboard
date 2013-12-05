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
        var pattern = /^\s*\d+\s*$/g;
        var re = new RegExp(pattern);
        return re.test(value);
    };

    // check is number
    var regIsNumber = function (fData)
    {
        var reg = new RegExp("^[-]?[0-9]+[\\.]?[0-9]+$");
        return reg.test(fData);
    };

    // Check if string is a whole number(digits only).
    var isWhole = function (s) {
        var isWhole_re = /^\s*\d+\s*$/;
        return String(s).search (isWhole_re) != -1;
    };

    var removePerc = function(text) {
        var last = text[text.length - 1];
        if (last === '%') {
            text = text.replace('%', '');
        }
        return text;
    };
    // Checks that an input string is a decimal number, with an optional +/- sign character.
    var isDecimal = function (s) {
        var isDecimal_re     = /^\s*(\+|-)?((\d+(\.\d+)?)|(\.\d+))\s*$/;
       return String(s).search (isDecimal_re) != -1;
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
        isNumber: isDecimal,
        removePerc: removePerc
    };

})();
