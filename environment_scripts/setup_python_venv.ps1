# redirect stderr into stdout
$p = & { python -V } 2>&1
$python_version = [System.Version]"3.10.8"
$reference_version = [System.Version]"3.7.9"
$version_number = if (!($p -is [System.Management.Automation.ErrorRecord])) {
    [System.Version]($p -replace '\D+(\s+)', '$1')
}

function install_python {

    $filename = "python-$python_version-amd64.exe"
    $uri = "https://www.python.org/ftp/python/$python_version/$filename"
    $outpath = "C:\Users\$env:UserName\Downloads\"    
    $out = $outpath + $filename


    Invoke-WebRequest -URI $uri -OutFile $out
    Start-Process $out -Wait -ArgumentList '/quiet', 'InstallAllUsers=0', 'PrependPath=1', 'InstallLauncherAllUsers=0'
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")

}

function setup_venv {
    if (!(Test-Path env:VIRTUAL_ENV)) {
        python -m venv .\venv
        }
    .\venv\Scripts\Activate
    Write-Output "venv active"
    Write-Output "venv installed in $env:VIRTUAL_ENV"
}

# check if an ErrorRecord was returned or [System.Version] is less than $reference_version
if (!($p -is [System.Management.Automation.ErrorRecord] -or $version_number -lt $reference_version)) {
    # return as is and run setup_venv
    Write-Output $p" installed"
    setup_venv
}
else {
    # otherwise grab the version string from the error message and run install_python  
    Write-Output "python has not been found or your version number is lower than" $reference_version
    install_python
    setup_venv
}
