param(
    [Parameter(Mandatory=$true)][string]$Version
)

$nuget_ids = "Couchbase.Lite","Couchbase.Lite.Enterprise","Couchbase.Lite.Support.Android","Couchbase.Lite.Support.iOS","Couchbase.Lite.Support.NetDesktop","Couchbase.Lite.Support.UWP","Couchbase.Lite.Enterprise.Support.NetDesktop","Couchbase.Lite.Enterprise.Support.UWP"

$download_counts = 0,0,0,0,0,0,0,0

$index = 0
foreach($id in $nuget_ids) {
    $download_url = "https://www.nuget.org/api/v2/Packages(Id='$id',Version='$Version')"
    [xml]$content = Invoke-WebRequest -Uri $download_url
    $download_counts[$index] = $content.entry.properties.VersionDownloadCount.InnerText
    $index += 1
}


$download_counts | Set-Content downloads.txt
& python download_graph.py
