# Introduction

This repository contains the current onboarded key material in UAT environment for the Smart Trust Network. To be part of it, follow the instructions below. 

# Procedure

To be part of the Smart Trust Network, copy/fork at first the [template repository](https://github.com/WorldHealthOrganization/tng-participant-template) and send an onboarding/participation request to tng-support@who.int. After verification of your request your repository will be linked with this one and your onboarding informations are replicated to the environment.

# QA Checks

The incoming content needs to be checked for the following rules:


|Checks|Description|
|----|-----------|
|Valid Folder Structure|Checks if the folder structure is valid and all required files are there.|
|Valid PEM | The certificates will be checked for a valid pem structure|
|Key Length| The key length should be for RSA-PSS minimum 3072, and for EC-DSA 256 bit|
|Algorithm| OID TBD|
|Country Flag| The country flag (C value) must be set to the correct country code|
|Oversea Territory OU | TBD|
|Explicit Parameter| ICAO TBD|
|CSCA Validity Range| TBD |
|Extended Key Usages| List of valid [OIDs](https://github.com/WorldHealthOrganization/smart-trust-network-gateway/blob/main/docs/Architecture.md#dsc-limitation)|
|Key Usages| TBD e.g. Digital Signature|
|Repository Crosscheck| Keys must not be existing in uat, dev|


