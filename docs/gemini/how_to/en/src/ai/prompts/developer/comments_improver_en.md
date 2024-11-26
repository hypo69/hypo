# Improving Comments in Code (English)

This guide provides tips for writing better, more effective comments in your code. Clear and concise comments are crucial for maintainability and understanding.

**General Principles**

* **Explain *why*, not *what*.**  Focus on the intent behind the code, not just what it does.  Instead of:

```
// Calculate the total price.
total = price * quantity;
```

...use:

```
// Calculate the total price, accounting for potential discounts.
total = price * quantity;
```

* **Be specific and concise.**  Avoid vague or overly general statements.  Instead of:

```
// This function does something.
function doSomething(input) {
  // ...
}
```

...use:

```
// Calculate the square root of the input.
function calculateSquareRoot(input) {
  // Validate input.
  if (input < 0) {
    throw new Error("Input must be non-negative.");
  }

  return Math.sqrt(input);
}
```

* **Use clear and consistent language.**  Avoid jargon or technical terms that might not be immediately understood.

* **Document complex logic clearly.** For multi-step procedures, break down the logic with comments.

**Specific Cases**

* **Function Comments:** Describe the function's purpose, parameters, return value, and any pre- or post-conditions.

```
/**
 * Calculates the area of a rectangle.
 *
 * @param {number} length - The length of the rectangle.
 * @param {number} width - The width of the rectangle.
 * @returns {number} The area of the rectangle.
 * @throws {Error} If length or width is negative.
 */
function calculateRectangleArea(length, width) {
  // Validate inputs.
  if (length < 0 || width < 0) {
    throw new Error("Length and width must be non-negative.");
  }

  return length * width;
}
```

* **Loop Comments:** Explain the purpose of the loop and what it's iterating over.

```
// Iterate over all items in the inventory and update their prices.
for (let i = 0; i < inventory.length; i++) {
  // Update the price based on the discount.
  inventory[i].price = calculateDiscountedPrice(inventory[i].originalPrice);
}
```

* **Conditional Comments:** Describe the conditions under which different parts of the code will execute.

```
// If the user is logged in, display their profile information.
if (isLoggedIn) {
  displayProfile(currentUser);
} else {
  displayLoginScreen();
}
```

* **Error Handling:** Explain the reasons for specific error conditions and what actions are taken.

```
try {
  // Attempt to read the file.
  const data = fs.readFileSync('data.txt', 'utf-8');
} catch (error) {
  // Handle the error, log it, and return an appropriate message.
  console.error('Error reading file:', error);
  return 'Error reading the file.';
}
```

**Best Practices**

* **Avoid Redundancy:**  Don't comment on obvious code; comments should add value.
* **Keep Comments Up-to-Date:**  If your code changes, update the comments to reflect those changes.
* **Use a Consistent Style:**  Follow a specific format for comments (e.g., using Javadoc style for Java).
* **Don't Overcomment:**  Comments should help understand the intent; they shouldn't substitute for well-structured code.

**Tools and Resources**

* IDE features for code commenting can often help you generate comments.

By following these guidelines, you can write comments that are both helpful and concise, greatly improving the readability and maintainability of your code.