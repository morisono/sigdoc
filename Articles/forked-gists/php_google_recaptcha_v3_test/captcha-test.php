<?php
  if(isset($_POST["username"])){
    header("Content-type: text/plain");

    function challenge($secret, $response, $remoteIP = null, $action = "submit"){
      $ch = curl_init();
      curl_setopt($ch, CURLOPT_URL,"https://www.google.com/recaptcha/api/siteverify");
      curl_setopt($ch, CURLOPT_POST, 1);

      curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query(array(
        'secret' => $secret, 
        'response' => $response,
        'remoteip' => $remoteIP)));
      
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
      $response = curl_exec($ch);
      curl_close($ch);
      $arrResponse = json_decode($response, true);
       
      // verify the response
      if($arrResponse["success"] == '1' && $arrResponse["action"] == $action && $arrResponse["score"] >= 0.5) {

        /**
         * check with database if valid username/password
         */

        return array("code" => 0, "message" => "success", "data" => $arrResponse);
      } else {
        return array("code" => 1, "message" => "failed", "data" => $arrResponse);
      }
    }

    // IMPORTANT: $_POST["g-recaptcha-response"],
    
    $privatekey = "SECRET_KEY";
    $response = $_POST["g-recaptcha-response"];
    $recaptchaResult = challenge($privatekey, $response);

    print_r($recaptchaResult);
    exit;
  }
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<!--Head-->
<head>
<title>LOGIN PAGE</title>

<link id="favicon" rel="icon" type="image/x-icon" href="/favicon.ico"/>


<!--Styles-->
<link rel="stylesheet" type="text/css" href="/styles/login.css" />
<!--End Styles-->

<!--Scripts-->
<script src="https://www.google.com/recaptcha/api.js"></script>
<script type="text/javascript">
   function onSubmit(token) {
     document.getElementById("loginFRM").submit();
   }
</script><!--End Scripts-->

</head>
<!--End Head-->
<body>

<!--Layout-->
<form method="post" action="/captcha-test.php" id="loginFRM">
      <fieldset>
        <h1><img src="/images/banner.png" /></h1>
              <label for="username">Username:</label>
        <input type="text" name="username" id="username" value="" />
        <label for="password">Password:</label>
        <input type="password" name="password" id="password" />
        <input type="submit" 
          class="loginBTN g-recaptcha" 
          data-sitekey="SITE_KEY" 
          data-callback='onSubmit' 
          data-action='submit'
          value="Login"
        />
        <p>
            <a href="/login/forgot" title="Forgot Password">Forgot Password</a>
        </p>
      </fieldset>
    </form>
<!--End Layout-->  
</body>
</html>