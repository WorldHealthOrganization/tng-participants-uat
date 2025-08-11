
## 🔐 Certificate Details

| Folder | Filename         | Description |
|--------|------------------|-------------|
| `sca/` | `CSCA.pem`       | Issuing CA used to sign Document Sign Certificates (DSCs). |
| `sca/` | `ROOTCA.pem`     | ROOT CA used of certificate chain of Document Sign Certificates (DSCs). |
| `tls/` | `CSCA.pem`       | Issuing CA used to sign TLS Certificate. |
| `tls/` | `ROOTCA.pem`     | ROOT CA used of certificate chain of TLS Certificate. |
| `tls/` | `ACC_TLS.pem`    | TLS certificate used for HTTPS/API endpoints. Ensures secure communication. |
| `up/`  | `ACC_UP.pem`     | Certificate used to sign the DSC payload during upload. |

## 📄 Format & Encoding

All certificates are provided in **PEM format** (`.pem` or `.cer`) and include the full certificate chain where applicable.

## ✅ Validation Notes

- Each certificate has been verified for expiration, key usage, and chain validity.
- This structure supports automated onboarding tools and manual audit review.

## 🧾 Contact

For questions or verification, please contact:
- Organization: One Authen Company Limited
- Technical Lead: Paradorn Athichitsakul (PKI Technical Lead)
- Email: paradorn.at@oneauthen.in.th