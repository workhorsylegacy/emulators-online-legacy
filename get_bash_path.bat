

schtasks /delete /f /tn "Build"
schtasks /create /f /tn "Build" /sc once /st 23:59 /tr "'%~1' -c 'echo $PATH > %~2'"
schtasks /run /tn "Build"
