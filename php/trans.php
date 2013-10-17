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
        'New' => array(
            'es' => 'Nuevo'
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
        'Delayed' => array(
            'es' => 'Retrasado'
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
        'Monto Comprometido' => array(
            'es' => 'Monto Comprometido'
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
        ),
        'Performance' => array(
            'es' => 'Avances'
        ),
        'Risks' => array(
            'es' => 'Riesgos'
        ),
        'HOME_PAGE' => array(
            'es' => 'Bienvenido a la SM2015 Informe Mensual de Ejecución aplicación web. Este sitio le permitirá actualizar el Hito y avances gráficos en el Sitio Web Dashboard además de crear informes en PDF, Word o Excel.',
            'eng' => 'Welcome to the SM2015 Monthly Execution Report Webapp. This site will allow you to update the Milestone and Advances graphics on the Dashboard Website in addition to creating reports in PDF, Word or Excel.'
        ),
        'Milestone_Home' => array(
            'es' => 'Para actualizar los hitos, por favor haga clic en el botón \'Hitos\' a continuación. Para actualizar el estado, haga clic en el menú desplegable Estado para el hito y actualizar en consecuencia. Si un hito no se ha completado el 100% en el trimestre se esperaba, que está pendiente. Si un hito no se ha completado y el trimestre no ha terminado, está en proceso. Si un hito ha sido cumplir con los estándares del jefe del equipo, es completada. Cuando Ud. actualiza el hito en el formato, esta información también se actualizará el sitio Web Dashboard. Para crear comentarios, alertas y recomendaciones del jefe del equipo para el hito, haga clic en el botón Detalles. Esta información no se actualiza en la página web de Dashboard, y sólo se incluye en el informe al exportar.',
            'eng' => 'To update your milestones, please click on the \'Milestones\' button below. To update the Status, click on the status dropdown for the milestone and update accordingly. If a milestone is not completed 100% in the quarter it was expected, it is pending. If a milestone is not completed and the quarter has not ended, it is in process. If a milestone has been met by standards of the team leader, it is completed. This information will also update the Dashboard Website. To create comments, alerts and Team leader recommendations for the milestone, click on the details button. This information is not updated on the Dashboard website, and is only included in the report when you export.'
        ),
        'Performance_Home' => array(
            'es' => 'Para actualizar los avances (triángulo), haga clic en el botón de avance. Hay cinco variables que deben ser actualizados. Para los anticipos financieros, por favor, introduzca el % previsto y % ejecutado para la fecha actual de la PEP. Por avances físicos, por favor, introduzca el% previsto y % ejecutado para la fecha actual de la PEP. Por tiempo, por favor introduzca la fecha de la PEP se ha actualizado.',
            'eng' => 'To update the advances (triangle), please click on the advances button. There are five variables that should be updated. For financial advances, please input the % planned and % executed for the current date from the PEP. For physical advances, please input the % planned and % executed for the current date from the PEP. For time, please input the date the PEP was updated. '
        ),
        'Risks_Home' => array(
            'es' => 'Para actualizar la tabla de riesgo, por favor haga clic en el botón de riesgos. No hay grafico en el Dashboard vinculado a esta información, sólo se incluirá en el informe al exportar.',
            'eng' => 'To update risk table, please click on the risk button. There is no graphic on the dashboard linked to this information, it is only included in the report when you export.'
        ),
        'Manage' => array(
            'es' => 'Editar'
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
