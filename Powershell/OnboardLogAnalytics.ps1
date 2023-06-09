﻿#OnboardLogAnalyticsAgent.ps1 
 

$MMAObj = Get-WmiObject -Class Win32_Product -Filter "name='Microsoft Monitoring Agent'"
 
#If the agent is not installed then install it
if($MMAObj -eq $null)
{
    $OMS64bitDownloaURL = "https://go.microsoft.com/fwlink/?LinkId=828603"
    $OMSDownloadPath = "c:\Temp"
    $OMSDownloadFileName = "MMASetup-AMD64.exe"
    $OMSDownloadFullPath = "$OMSDownloadPath\$OMSDownloadFileName"
 
    #Create temporary folder if it does not exist
    if (-not (Test-Path $OMSDownloadPath)) { New-Item -Path $OMSDownloadPath -ItemType Directory | Out-Null }
 
    Write-Output "Downloading the agent..."
 
    #Download to the temporary folder
    Invoke-WebRequest -Uri $OMS64bitDownloaURL -OutFile $OMSDownloadFullPath | Out-Null
 
    Write-Output "Installing the agent..."
 
    #Install the agent
    $ArgumentList = '/C:"setup.exe /qn ADD_OPINSIGHTS_WORKSPACE=0 AcceptEndUserLicenseAgreement=1"'
    Start-Process $OMSDownloadFullPath -ArgumentList $ArgumentList -ErrorAction Stop -Wait | Out-Null
}
 
#Add the CSE Workspace
$WorkspaceID = ''
$WorkspaceKey = ''
 
#Check if the CSE workspace is already configured
$AgentCfg = New-Object -ComObject AgentConfigManager.MgmtSvcCfg
$OMSWorkspaces = $AgentCfg.GetCloudWorkspaces()
 
$CSEWorkspaceFound = $false
foreach($OMSWorkspace in $OMSWorkspaces)
{
    if($OMSWorkspace.workspaceId -eq $WorkspaceID)
    {
        $CSEWorkspaceFound = $true
    }
}
 
if(!$CSEWorkspaceFound)
{
    Write-Output "Adding CSE OMS Workspace..."
    $AgentCfg.AddCloudWorkspace($WorkspaceID,$WorkspaceKey)
    Restart-Service HealthService
}
else
{
    Write-Output "CSE OMS Workspace already configured"
}
 

$AgentCfg.GetCloudWorkspaces()