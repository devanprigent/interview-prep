// What's the issue with this test and how to improve it?

const certificate = await this.certificateGenerator.generateCertificate(contractId);

assert(certificate, "Certificate should be available at this stage");

