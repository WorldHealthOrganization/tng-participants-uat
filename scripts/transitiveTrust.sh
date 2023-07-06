#!/bin/bash

echo "Start Transitive Trust"

rm -rf transit
git clone https://$GITHUB_TOKEN@$TRANSITIVE_TRUST transit
tree
cd transit
cd UAT
mkdir signing 
cd signing
echo $PWD
tree
echo -n "${NB_UP_SIGNING_PUB}" > pub-key.pem
echo -n "${NB_UP_SIGNING_KEY}" > priv-key.pem
cd .. 
cd ..
echo $PWD
./extract.sh UAT    
cd ..
echo "Finished Transitive Trust"
tree
