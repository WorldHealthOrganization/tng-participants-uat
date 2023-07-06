#!/bin/bash

echo "Start Transitive Trust"

rm -rf transit
git clone https://$GITHUB_TOKEN@$TRANSITIVE_TRUST transit
cd transit
cd $ENV
mkdir signing 
cd signing
echo $PWD
echo "$NB_UP_SIGNING_PUB" > pub-key.pem
echo "$NB_UP_SIGNING_KEY" > priv-key.pem
cd .. 
cd ..
echo $PWD
./extract.sh $ENV $1     
cd ..
echo "Finished Transitive Trust"
