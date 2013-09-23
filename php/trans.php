<?php

    $translation = array(
        'Hello world!' => array(
            'fr' => 'Bonjour tout le monde!',
            'de' => 'Hallo Welt!'
        ),
        'Country' => array(
            'es'=> 'Pais'
        ),
        'Payment Indicador' => array(
            'es'=> 'Indicador de Pago'
        ),
        'Milestone' => array(
            'es'=> 'Hito'
        ),
        'Quarter' => array(
            'es'=> 'Trimestre'
        ),
        'Audience' => array(
            'es'=> 'Audiencia'
        ),
        'Status' => array(
            'es' => 'Estatus'
        ),
        'Alert/Notes' => array(
            'es' => 'Alerta/Notas'
        ),
        'Recommendation TL' => array(
            'es' => 'Recomendación JE'
        ),
        'Agreements' => array(
            'es' => 'Acuerdos'
        ),
        'Activity in POA' => array(
            'es' => 'Actividad en POA'
        ),
        'Add' => array(
            'es' => 'Añadir'
        ),
        'Close' => array(
            'es' => 'Cerrar'
        ),
        'Detail' => array(
            'es' => 'Detalle'
        ),
        'Edit' => array(
            'es' => 'Editar'
        ),
        'Delete' => array(
            'es' => 'Borrar'
        ),
        'Cancel' => array(
            'es' => 'Cancelar'
        ),
        'Save' => array(
            'es' => 'Salvar'
        ),
        'Completed' => array(
            'es' => 'Completado'
        ),
        'In Process' => array(
            'es' => 'En Proceso'
        ),
        'Pending' => array(
            'es' => 'Pendiente'
        ),
        'Donors' => array(
            'es' => 'Donantes'
        ),
        'Updated' => array(
            'es' => 'Fecha de Actualizacion'
        ),
        'Executed' => array(
            'es' => 'Avances Físicos Planificados'
        ),
        'Financial Executed' => array(
            'es' => 'Avances Financieros Planificados'
        ),
        'Alerts' => array(
            'es' => 'Alertas Tempranas'
        ),
        'Fund' => array(
            'es' => 'Monto Desembolsado'
        ),
        'Physical Progress' => array(
            'es' => 'Avances Físicos Reales'
        ),
        'Financial Progress' => array(
            'es' => 'Avances Financieros actuales'
        ),
        'Recommendation' => array(
            'es' => 'Recomendaciones'
        )
    );

if(!function_exists('_t'))
{
  function _t($token, $lang = null) {
      global $translation;
      if ( empty($lang)
          || !array_key_exists($token, $translation)
          || !array_key_exists($lang, $translation[$token])
      ) {
          return $token;
      } else {
          return $translation[$token][$lang];
      }
  }
}

?>
