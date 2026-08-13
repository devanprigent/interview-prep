// What's the issue with this test and how to improve it?

const certificate = await this.certificateGenerator.generateCertificate(contractId);

assert(certificate, "Certificate should be available at this stage");



/*
SOLUTION

The issue of this test is obvious if you imagine you're the one checking the 

error message without any knowledge of the system.

You get "Certificate should be available at this stage".

That's all.

If that happens to you, you'd have a million questions.

What are we talking about? What's a certificate? Why should we have a certificate?

Which contract are we talking about?

Where did this fail? The certificate generation failed yes, but at which step?

Based on that error, the search space to solve the problem is huge.

The first improvement would be to add more context in the error message:

assert(certificate,
  'Unable to generate the insurance certificate right after signing the contract')

The second improvement would be to add more context by including the faulty contract:

const certificate = 
  await this.certificateGenerator.generateCertificate(contractId)

if (!certificate) {
  throw new TechnicalError(
    'Unable to generate the insurance certificate right after signing the contract',
    { context: { contractId } }
  );
}

The third improvement would require more changes. We still don't know where the generation failed

so we'd need to debug the entire generation logic. Instead, we could modify generateCertificate

to return a standardized response message with a status SUCCESS/ERROR and a message. Then, show

this message in case of error.


*/