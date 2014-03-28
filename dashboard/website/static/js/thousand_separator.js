function thousandSeparator(n){
    var rx = /(\d+)(\d{3})/;
    var thousand_symbol = '.';
    if(CURRENT_LANGUAGE == 'en'){
      thousand_symbol = ',';
    }
    return String(n).replace(/^\d+/, function(w){
        while(rx.test(w)){
            w = w.replace(rx, '$1'+thousand_symbol+'$2');
        }
        return w;
    });
}
