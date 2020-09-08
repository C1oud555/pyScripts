syncpath="/home/komer/Desktop/SyncMyDevices"

function share {
    cp -rf $1 ${syncpath}
}

function show {
    echo "The files in share folder"
    echo "***********************************************************************"
    ls -al ${syncpath}
    echo "***********************************************************************"
}