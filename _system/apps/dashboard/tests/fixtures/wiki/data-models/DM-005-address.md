---
id: DM-005
type: data-model
title: Address
status: draft
created: 2026-01-01
updated: 2026-01-01
sources: []
related: []
tags: [data-model]
stereotype: value-object
parent: []
bounded-context: Lending
source-of-truth: Library system
---

# Address

**Purpose.** A postal address; equality by value, no lifecycle of its own.

**Attributes.**

- `street` : string — street and number
- `city` : string — city

**Relationships.**

- describes → [[DM-006-missing-target]] · 1 · association · mandatory
