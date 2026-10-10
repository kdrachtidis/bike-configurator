# Bike Configurator – Copilot Guidance

This document explains the system architecture, product intent, and the interaction patterns that matter most for feature development. It is intended to help AI coding assistants understand the app deeply enough to recommend changes, implement new features safely, and reason about edge cases.

## 1) Product Summary

The app is a bike configurator where a user can:
- choose a bike model or base frame
- customize components (frame, wheels, drivetrain, saddle, handlebar, etc.)
- see compatibility constraints and price changes live
- validate selections against real rules (size compatibility, drivetrain compatibility, optional add-ons)
- save/share or review a final configuration
- possibly proceed to purchase/quote flow

This is a configuration-heavy product, so the main complexity is not just CRUD—it is:
- decision logic
- compatibility validation
- live pricing updates
- multi-step UX state
- partial/incomplete configuration handling
- real-time recalculation after each selection

## 2) Current Architecture

### Frontend: Vue
The frontend is a Vue-based UI that manages interactive configuration state. The app should be treated as a stateful product configurator rather than a simple CRUD dashboard.

Expected frontend responsibilities:
- render product selection steps
- maintain selected parts and current configuration
- trigger validation checks
- display summary and pricing
- handle loading/error/empty states
- support interactive navigation between configuration sections

Likely frontend concerns:
- component tree organized by configuration domain:
  - product overview or model selector
  - component picker panels
  - compatibility summary
  - final configuration review
  - cart/quote actions
- app state should separate:
  - selected product model
  - selected options
  - compatibility result
  - derived price
  - UI state: loading, error, dirty, validation warnings

### Backend: Python
The backend is likely responsible for:
- exposing product/catalog data
- resolving option availability
- validating compatibility rules
- computing dynamic pricing
- storing user configurations or quote sessions
- serving business rules cleanly away from UI logic

The backend should be designed around domain logic rather than UI concerns. The key rule is:
- Vue decides how to present state
- Python decides what is valid and what is possible

## 3) Core Business Rules

The app’s highest-value logic is not generic CRUD but product rules. Most important domain concepts:

### Bike Model / Base Product
Each configuration should start from a base bike model or frame type. The selected model defines:
- frame size options
- wheel size options
- drivetrain compatibility
- price range
- allowed accessories
- available colorways or finishes

### Component Compatibility
The app should enforce compatibility constraints such as:
- frame and wheel size mismatch
- rim compatibility with tire width
- drivetrain compatibility with frame mount types
- fork compatibility with wheel set
- handlebar width not allowed for a certain frame geometry
- incompatible accessory combinations

This logic should live in backend validation or a shared rules layer, not just in the front-end UI.

### Price Calculation
Every option should update the total summary. Price logic should be:
- deterministic
- centralized
- testable
- aware of optional add-ons, taxes, discounts, or shipping

A price update should be derived from:
- base bike price
- selected components
- upgrades and add-ons
- optional services
- any applied discount or promo rules

### Validation / Incomplete State
The app should distinguish between:
- valid configuration
- partially completed configuration
- invalid configuration
- warning state (allowed but suboptimal)
- blocked state (not allowed, must change options)

Important behavior:
- A user should be able to see why a selection is invalid
- Validation feedback should be specific and actionable
- The app should not silently permit impossible configurations

## 4) Important Interaction Patterns

These are the interaction patterns that matter most for this app.

### Pattern A: Option Selection Updates State and Price
Example:
- User selects a frame
- App updates available accessories
- Price recalculates
- Compatibility warnings appear if needed

Requirements:
- UI updates immediately after each option change
- business rules are evaluated consistently
- derived values are recalculated in one place
- there is a predictable behavior for loading and stale responses

### Pattern B: Compatibility Warning vs Hard Error
Not all invalid combinations are equal.

Examples:
- hard error: bike frame incompatible with selected wheel set
- warning: recommended but not required upgrade
- informational note: component is compatible but reduces performance

Implementation guidance:
- separate validation categories into:
  - blocked
  - warning
  - informational
- UI should show visual differentiation
- backend should not hide important reasons

### Pattern C: Multi-Step Configuration Flow
Users often go through screens or panels in sequence:
- choose model
- choose frame
- choose drivetrain
- choose wheel set
- choose seat/handlebar
- choose accessories
- review and buy

Requirements:
- steps should preserve prior selections
- users can go back and modify earlier options without losing state
- reconfiguration must recalculate downstream selections
- incompatible prior choices should be surfaced clearly when navigating back

### Pattern D: Save or Quote Flow
The app may need to allow:
- temporary save
- restore previous configuration
- quote generation
- compare configurations

These workflows need:
- stable configuration IDs
- consistent serialization
- explicit handling of default values and missing selections

### Pattern E: Degraded UX / Incomplete Setup
Users may start a configuration and leave it incomplete. The system should gracefully handle:
- missing required fields
- disabled selections
- partially valid configurations
- stale pricing if derived state is not available

This is important for configurator products because users often change decisions in non-linear ways.

## 5) Product Features to Support

Below is a recommended feature list and expected interaction details.

### Feature 1: Model / Frame Selection
Goal: user picks the bike type and frame series.

Expected behavior:
- model selection defines available options
- price and base attributes update immediately
- incompatible or unavailable frames are disabled appropriately
- if model changes, downstream selections may reset or remain if valid

Edge cases:
- selected component no longer valid after model switch
- previous user choices should be preserved if still valid
- should show “compatible with current model” labels

### Feature 2: Component Customization
Goal: user customizes parts such as drivetrain, tires, seat, handlebars, pedals, accessories.

Expected behavior:
- option groups update dynamically
- selected options reveal compatibility notes
- price updates instantly
- unavailable combinations are visually disabled

Edge cases:
- option becomes unavailable after another option changes
- option selected but no longer valid due to backend rule

### Feature 3: Compatibility Validation
Goal: ensure configuration is usable and legal.

Expected behavior:
- validation runs when user changes selections
- errors/warnings are shown inline near the affected component
- summary includes all active blockers
- selection cannot be finalized while invalid blockers remain

Acceptance criteria:
- invalid combinations are blocked
- context-specific reasons are displayed
- warnings do not prevent flow unless product rules require it

### Feature 4: Dynamic Pricing
Goal: maintain real-time total breakdown.

Expected behavior:
- each option contributes to the total
- selected add-ons update subtotal
- discounts/promos can be applied or calculated
- final total is recomputed after any change

Acceptance criteria:
- totals are based on selected configuration only
- pricing changes are visible immediately
- rounding/tax rules are handled consistently

### Feature 5: Configuration Review and Finalization
Goal: user reviews and confirms the bike before checkout or quote submission.

Expected behavior:
- summary of all selections
- clear validation status
- final warnings before submission
- optional save/share/quote actions
- consistent state between review and purchase flow

### Feature 6: Persisted Configurations
Goal: retain user choices across sessions or flows.

Expected behavior:
- save configuration state with stable IDs
- allow restore/compare existing designs
- keep original selected items and final status
- support editing after restore

## 6) Architectural Guidance for Implementation

### Keep State Flat and Derived
For the frontend, keep:
- base selected values
- derived values (computed totals, compatibility status, final summary)
- UI state

Avoid scattering logic across many components. The app should prefer:
- a central configuration store or state manager
- component-level forms for editing values
- computed selectors from a single source of truth

### Prefer Business Logic in the Backend
The backend should own:
- compatibility rules
- pricing calculations
- validation decisions
- product constraints and definitions

The frontend should own:
- user interaction
- animation and feedback
- form state
- ephemeral notifications

### Plan for Errors and Null States
The app is highly interactive. Must account for:
- option partially missing
- backend response slow or failed
- product catalog stale
- user switching configuration too quickly
- repeated updates causing race conditions

Do not assume synchronous updates. The UI should handle asynchronous validation and stale state carefully.

## 7) Engineering Principles

- Keep business logic explicit and testable.
- Do not duplicate pricing rules in multiple places.
- Treat compatibility checks as first-class services.
- Make invalid states understandable.
- Prefer consistency over cleverness.
- Keep configuration state serializable and easy to debug.
- When a user changes an earlier option, downstream updates must be deterministic.

## 8) Testing Expectations

This app should be tested heavily at the logic level.

Required test categories:
- component compatibility logic
- pricing calculations
- invalid selection handling
- model switching and reset behavior
- persisted configuration restore flow
- UI validation states

Prefer tests at the domain logic layer, because most important bugs here are not visual—they are rule and validation bugs.

## 9) Examples of Good Implementation Pattern

A good feature implementation should:
- receive the current configuration
- evaluate all rules
- return:
  - valid/invalid state
  - warnings
  - price delta
  - affected components or reasons
- allow UI to render those results cleanly

This pattern should be reused across:
- bike model changes
- accessory toggles
- dynamic price calculations
- review screens
- final purchase validation

## 10) What to Avoid

- Hardcoding business rules in Vue templates
- Repeating price logic across components
- Letting the frontend silently accept invalid configurations
- Using poor state resets when switching model or category
- Treating warnings and blockers as the same thing
- Storing configuration state in non-serializable or deeply nested ad hoc objects without clear structure

## 11) High-Value Future Features

Potential additions that fit the product:
- 3D bike preview
- accessory visual comparison
- size recommendation logic
- saved configuration library
- “compare two builds”
- quote export / PDF
- seasonal bundles or package offers

These features will be much easier to implement if the base configuration model is clean and the validation rules are centralized.

## 12) Working Style for AI Assistance

When asking for code changes or feature implementation, prefer to describe:
- the user journey
- the state transitions
- dependencies between options
- validation behavior
- pricing implications
- edge cases and invalid combinations

Strong guidance prompt example:
> “Add a bicycle configuration step where changing the frame type resets downstream drivetrain options only if they are no longer valid. Preserve valid selections when possible, show compatibility warnings, and update the summary price in real time. Ensure the backend validation returns explicit reasons and the frontend renders the blocked state with a clear message.”

This type of prompt gives the assistant enough detail to reason about the system instead of patching blindly.

## 13) Notes for Future Refinement

This file should eventually be expanded with:
- actual app module structure
- exact Python package names
- exact Vue component hierarchy
- API contract examples
- sample request/response payloads for configuration update endpoints
- real compatibility rules for bike categories
- screenshots or annotated UI flows for key interactions

If this project grows, it is worth splitting this into:
- ARCHITECTURE.md
- FEATURES.md
- ROADMAP.md
- API.md
- DECISIONS.md

But this file is the right starting point for now.