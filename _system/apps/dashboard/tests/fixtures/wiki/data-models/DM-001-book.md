---
id: DM-001
type: data-model
title: Book
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

# Book

**Purpose.** A physical copy the library lends out.

**Identity.** `isbn`

**Attributes.**

- `isbn` : string — identifier
- `title` : string — display title
- `shelf` : enum(fiction, nonfiction) — location

**Relationships.**

- stocked on → [[DM-004-shelf]] · 1..n · association · mandatory

**Invariants / rules.**

- An isbn is unique.
