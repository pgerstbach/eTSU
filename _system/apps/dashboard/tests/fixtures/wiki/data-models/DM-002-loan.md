---
id: DM-002
type: data-model
title: Loan
status: agreed
created: 2026-01-01
updated: 2026-01-01
sources: []
related: []
tags: [data-model]
stereotype: entity
parent: []
bounded-context: Lending
source-of-truth: Library system
---

# Loan

**Purpose.** One lending transaction between a member and a book.

**Identity.** `loanId`

**Attributes.**

- `loanId` : string — identifier
- `status` : enum(planned, active, returned) — lifecycle

**Relationships.**

- concerns → [[DM-003-member]] · 1 · association · mandatory
- concerns → [[DM-001-book]] · 1 · association · mandatory

**Invariants / rules.**

- A loan is always bound to one member and one book.
