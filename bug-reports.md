# SauceDemo — Manual Test Report

## Test plan

**Application under test:** [SauceDemo](https://www.saucedemo.com/) — a demo e-commerce
web application provided by Sauce Labs for testing practice.

**Objective:** Verify the core user flows (login, product inventory, cart, and
checkout) and document any defects found.

**Scope & approach:** Manual exploratory testing of the web UI in Chrome, focused on
the functional correctness of the main purchase flow.

**Test accounts:** Two accounts were used deliberately:
- `standard_user` — used as the **baseline/reference** account, expected to behave
  correctly.
- `problem_user` — the account **under test**. Its behavior was compared against
  `standard_user` to separate genuine defects from expected behavior.

**Flows covered:** login (multiple accounts), inventory page (product images, sorting,
add-to-cart), cart (add / remove), product detail pages, and the checkout information
form.

**Note on false positives:** A suspected default-sorting issue (products not ordered by
item id) was investigated but **ruled out** — comparing against `standard_user`
confirmed that this ordering is the application's expected default behavior, not a
defect. It is therefore not reported below.

**Result:** 5 defects were identified, ranging in severity from Medium to Critical.

---

## Bug 1 — Inventory: all product images load as the same dog photo

**Environment:** saucedemo.com · user: `problem_user` · Chrome

**Steps to reproduce:**
1. Log in as `problem_user` / `secret_sauce`.
2. Wait for the Inventory page to load.
3. Observe the images displayed on the product cards.

**Expected result:** Each product card displays its own authentic product image
(e.g., a real backpack, a real bike light).

**Actual result:** Every product image on the page is replaced by the exact same
picture of a dog.

**Severity:** High — negatively impacts brand image and user experience, causing
severe confusion.

---

## Bug 2 — Inventory: sort dropdown options are unresponsive

**Environment:** saucedemo.com · user: `problem_user` · Chrome

**Steps to reproduce:**
1. Log in as `problem_user` / `secret_sauce`.
2. Click the sort dropdown menu at the top right to open it.
3. Attempt to select a different sorting option (e.g., "Price (high to low)").

**Expected result:** The selected option is applied and the products are reordered
based on the new criteria.

**Actual result:** The dropdown opens, but clicking a sorting option triggers no
action. The selection is ignored and the product order does not change.

**Severity:** Medium — restricts navigation and user experience, though it does not
outright block the purchasing path.

---

## Bug 3 — Inventory: most items cannot be added to the cart

**Environment:** saucedemo.com · user: `problem_user` · Chrome

**Steps to reproduce:**
1. Log in as `problem_user` / `secret_sauce`.
2. Locate any item other than the Backpack, Bike Light, or Onesie
   (e.g., "Sauce Labs Bolt T-Shirt").
3. Click the "Add to cart" button for that item.

**Expected result:** The button changes to "Remove" and the cart counter increases,
successfully adding the item.

**Actual result:** The click registers no action; the item is not added to the cart.
Only the Backpack, Bike Light, and Onesie can be added.

**Severity:** Critical — blocks purchasing for a large portion of the inventory,
directly resulting in revenue loss.

---

## Bug 4 — Product details: Fleece Jacket (item id=6) shows broken data

**Environment:** saucedemo.com · user: `problem_user` · Chrome

**Steps to reproduce:**
1. Log in as `problem_user` / `secret_sauce`.
2. Click the title or image of "Sauce Labs Fleece Jacket" to open its details page.
3. Observe the product name, description, and price fields.

**Expected result:** The page displays the correct product name, a relevant
description, and a valid numerical price.

**Actual result:** The product name shows "ITEM NOT FOUND"; the description displays a
phone-operator recording ("We're sorry, but your call could not be completed as
dialled..."); and the price field shows an invalid value instead of a valid price.
The affected item is inventory item id=6 (visible in the URL).

**Severity:** Critical — the product detail page for this item is completely broken and
unusable, likely due to a data mismatch or UI bug.

---

## Bug 5 — Checkout: typing in "Last Name" enters text into "First Name"

**Environment:** saucedemo.com · user: `problem_user` · Chrome

**Steps to reproduce:**
1. Log in as `problem_user` / `secret_sauce`.
2. Add an item to the cart and proceed to "Checkout: Your Information".
3. Click the "Last Name" input field to focus it.
4. Type any characters on the keyboard.

**Expected result:** The typed characters appear inside the "Last Name" field.

**Actual result:** Although the "Last Name" field is focused, the keystrokes appear in
the "First Name" field instead. The "Last Name" field remains empty.

**Severity:** High — prevents the user from completing the checkout form, as the
mandatory field validation cannot be satisfied.
