<?php include('./php/signin.php'); ?>
<?php require_once('./php/trans.php'); ?>
<?php
$home = _t('HOME_PAGE', $_SESSION['SESS_LANG']);
?>

<?php include_once('./header.php') ?>

<!-- BEGIN CONTAINER -->
<div class="page-container row-fluid"> 

    <?php include_once('./sidebar.php') ?>

  <!-- BEGIN PAGE CONTAINER-->
  <div class="page-content"> 
    <!-- BEGIN SAMPLE PORTLET CONFIGURATION MODAL FORM-->
    <div id="portlet-config" class="modal hide">
      <div class="modal-header">
        <button data-dismiss="modal" class="close" type="button"></button>
        <h3>Widget Settings</h3>
      </div>
      <div class="modal-body"> Widget settings form goes here </div>
    </div>
    <div class="clearfix"></div>
    <div class="content">  

	</div> 
  </div>  
  <!-- END PAGE --> 
</div>
<!-- END CONTAINER --> 

<?php include_once('./footer.php') ?>
