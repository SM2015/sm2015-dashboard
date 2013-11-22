<?php include('./php/signin.php'); ?>
<?php require_once('./php/trans.php'); ?>
<?php
$home = _t('HOME_PAGE', $_SESSION['SESS_LANG']);
?>

<?php include_once('./header.php') ?>

<!-- BEGIN CONTAINER -->
<div class="page-container row-fluid"> 

    <?php include_once('./sidebar.php') ?>
    
    <div class="page-content"> 
        <div class="map-container">
            (mapa)
        </div>

        <div class="content">  
           <div id="container">
                <div class="row-fluid spacing-bottom 2col">	
                    <div class="span3 ">	
                        (grafico)
                    </div>
                    <div class="span3 ">	
                        (grafico)
                    </div>
                    <div class="span3 ">	
                        (grafico)
                    </div>
                    <div class="span3 ">	
                        (grafico)
                    </div>
		        </div>
           </div> 
        </div>  
    </div>
</div>
<!-- END CONTAINER --> 

<?php include_once('./footer.php') ?>
