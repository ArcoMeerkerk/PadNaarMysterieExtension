param (
    $JavaDir32 = "C:\Program Files (x86)\Java\jre1.8.0_271",
    $JavaDir64 = "C:\dev\Processing\processing.py-3017-windows64\jre",
    $Launch4jExe = "C:\Program Files (x86)\Launch4j\launch4jc.exe",
    $InnoSetupExe = "C:\Program Files (x86)\Inno Setup 6\iscc.exe"
)

Set-Location -Path $PSScriptRoot

function CheckAndMakeDir {
param (
    $Path
)

if ($Path -is [array]) {
    Foreach ($p in $Path)
    {
        CheckAndMakeDir $p
    } 
}
else {
    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -ItemType directory -Path $Path > $null
        "Created directory" + $Path
    }
}
}
function CheckAndRenameDir {
param (
    $Path,
    $Name
    )
    
    if (Test-Path -LiteralPath $Path) {
        Rename-Item -Path $Path -NewName $Name > $null
        "Renamed " + $Path + " to " + $Name
}
}

function CheckAndCopyDir {
param (
    $SourcePath,
    $TargetPath,
    $TargetName,
    $Multiple = $false
)
$TempCopyFolderOldPath = $TargetPath + '\' + (Split-Path $SourcePath -Leaf)
if ($null -ne $TargetName) {
    $CustomTargetFolderPath = $TargetPath + "\" + $TargetName
}
else {
    $CustomTargetFolderPath = $TargetPath
}

if ($SourcePath -is [array]) {
    Foreach ($path in $SourcePath)
    {
        CheckAndCopyDir $path $TargetPath -Multiple $Multiple
    } 
}
else {
    if ((Test-Path -LiteralPath $SourcePath) -and
        (Test-Path -LiteralPath $TargetPath) -and
        #Check if source directory name doesn't exist in target path
        -not (Test-Path -LiteralPath $TempCopyFolderOldPath) -and
        (((Get-ChildItem $TargetPath | Measure-Object).Count -eq 0) -or
        (
            #Check if a custom folder is given
            ($null -ne $TargetName) -and
            #Check if custom check folder doesn't exists
            -not (Test-Path -LiteralPath $CustomTargetFolderPath)
        ) -or
        ($Multiple -eq $true))
    ) {
        "Copying " + $SourcePath
        Copy-Item -Path $SourcePath -Destination $CustomTargetFolderPath -Recurse
        "Copied to folder " + $TempCopyFolderOldPath
    }
}
}

function CheckAndCopyFile {
    param (
        $SourcePath,
        $TargetPath
    )

    if ($SourcePath -is [array]) {
        Foreach ($path in $SourcePath)
        {
            CheckAndCopyFile $path $TargetPath
        } 
    }
    else {
        if ((Test-Path $SourcePath -PathType Leaf) -and (Test-Path -LiteralPath $TargetPath)) {
            Copy-Item -Path $SourcePath -Destination $TargetPath
        }
    }
}


function ExportProject {
param (
    $exportFolder,
    $JavaDir
)
    $libPath1 = '..\application.windows32\lib'
    $libPath2 = '..\application.windows64\lib'
    $processingFolders = '..\modules', '..\assets'
    $processingFiles = '..\PadNaarMysterieExtension.pyde'

    CheckAndMakeDir $exportFolder

    CheckAndCopyDir $libPath1 $exportFolder "libraries"
    CheckAndCopyDir $libPath2 $exportFolder "libraries"
    CheckAndCopyDir $JavaDir $exportFolder "jre"
    CheckAndCopyDir $processingFolders $exportFolder -Multiple $true
    CheckAndCopyFile $processingFiles $exportFolder
}


$exportFolderPath = '.\bin\export'
ExportProject ($exportFolderPath + '32') $JavaDir32
ExportProject ($exportFolderPath + '64') $JavaDir64


# iscc setup.iss /DMyAppPlatform=32
 
Start-Process -NoNewWindow -Wait -FilePath $Launch4jExe -ArgumentList 'build32.xml'
Start-Process -NoNewWindow -Wait -FilePath $Launch4jExe -ArgumentList 'build64.xml'
Start-Process -NoNewWindow -Wait -FilePath $InnoSetupExe -ArgumentList 'setup.iss',"/DMyAppPlatform=32"
Start-Process -NoNewWindow -Wait -FilePath $InnoSetupExe -ArgumentList 'setup.iss',"/DMyAppPlatform=64"