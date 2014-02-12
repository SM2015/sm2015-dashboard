/*
 * Datepicker for Jeditable
 *
 * Copyright (c) 2011 Piotr 'Qertoip' Włodarek
 *
 * Licensed under the MIT license:
 *   http://www.opensource.org/licenses/mit-license.php
 *
 * Depends on jQuery UI Datepicker
 *
 * Project home:
 *   http://github.com/qertoip/jeditable-datepicker
 *
 */

// add :focus selector
jQuery.expr[':'].focus = function( elem ) {
  return elem === document.activeElement && ( elem.type || elem.href );
};

$.editable.addInputType( 'datepicker', {

    /* create input element */
    element: function( settings, original ) {
      var form = $( this ),
          input = $( '<input />' );
      input.attr( 'autocomplete','off' );
      form.append( input );
      return input;
    },
    
    /* attach jquery.ui.datepicker to the input element */
    plugin: function( settings, original ) {
      var form = this,
          input = form.find( "input" );

      // Don't cancel inline editing onblur to allow clicking datepicker
      settings.onblur = 'nothing';
      
      input.datepicker()
        .on('changeDate', function(event){
          input.datepicker('hide');
        })
        .on('hide', function(event){
          form.submit()
        });
    }
} );
