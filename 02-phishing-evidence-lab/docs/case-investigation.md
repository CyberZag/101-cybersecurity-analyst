# Synthetic phishing case investigation

## Scope and result

Case 02 is an original, inert training message. The workbench reports three observations: a Reply-To domain difference, a visible-link host mismatch, and an unverified authentication failure claim. These justify review. The evidence does not establish delivery to a real user, link access, credential entry, or account compromise.

## Evidence record

Use `reports/findings.json` for the exact source SHA-256 and byte count. Recompute it directly from the `.eml` file before comparing analyses. Keep the original file intact and separate from notes. These checks support integrity comparison, not a complete legal chain of custody.

| Evidence | Observation | Interpretation and uncertainty |
|---|---|---|
| From | support at company.example | An asserted sender identity, not authenticated ownership |
| Reply-To | collect at external.example | Replies would go to a different domain; may be authorized or deceptive |
| Anchor text | portal.company.example | Visible host differs from the target host |
| Actual target | collect.external.example | Requires validation in an authorized investigation; no visit occurred |
| Authentication-Results | spf=fail and dmarc=fail | Untrusted file claims; confirm the receiving gateway and header provenance |

## Next actions in a real authorized SOC workflow

1. Preserve the reported message and establish its source, gateway trace ID, timestamps, and receiving system.
2. Confirm message delivery and impacted recipients in approved mail telemetry. Corroborate authentication results at the receiving boundary.
3. Review approved URL-click, proxy, DNS, endpoint, and identity telemetry around the message time. Delivery, click, credential submission, and compromise are different claims requiring different evidence.
4. Validate the purported request through an independent known contact channel. Do not reply to the suspicious message to verify itself.
5. Escalate according to scope and confidence. Recommend containment only where evidence and the organization's playbook support it; document approval, action, and subsequent checks.

No containment action was executed in this lab.

## False-positive control

Case 04 is a known synthetic partner workflow. Its reply-domain difference still generates review. A blanket rule that blocks every domain mismatch would incorrectly block this case. A future tuning exercise could use an explicitly approved sender/reply-domain pair with owner, business reason, expiration, and continued logging. A broad domain allowlist could hide abuse; document and test the scope.

## Case notes to complete yourself

- What I ran and the date:
- Source hash I independently verified:
- Two observations I can demonstrate in the raw message:
- What I cannot conclude:
- Evidence that would change my disposition:
- My own code or test improvement:

Leave these blank until you do the work. Do not present this sample report as a real incident you handled.
