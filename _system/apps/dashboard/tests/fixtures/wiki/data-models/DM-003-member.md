---
id: DM-003
type: data-model
title: Member
status: draft
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

# Member

**Purpose.** A registered person allowed to borrow books.

**Identity.** `memberId`

**Attributes.**

- `memberId` : string — identifier
- `name` : string — full name

**Relationships.**

- takes part in → [[DM-002-loan]] · 0..n · association · optional

**Invariants / rules.**

- A member is known by their memberId.
