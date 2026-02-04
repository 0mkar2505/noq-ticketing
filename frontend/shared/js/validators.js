/**
 * Shared validation utilities for auth forms
 */

/**
 * Validate email format
 * @param {string} email
 * @returns {boolean}
 */
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email.trim());
}

/**
 * Validate password requirements
 * Minimum 8 characters, at least 1 letter and 1 number
 * @param {string} password
 * @returns {boolean}
 */
function isValidPassword(password) {
  const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d).{8,}$/;
  return passwordRegex.test(password);
}

/**
 * Check if password matches confirmation
 * @param {string} password
 * @param {string} confirmPassword
 * @returns {boolean}
 */
function passwordsMatch(password, confirmPassword) {
  return password === confirmPassword;
}

/**
 * Show error message in element
 * @param {HTMLElement} element
 * @param {string} message
 */
function showError(element, message) {
  element.textContent = message;
  element.style.display = 'block';
}

/**
 * Clear error message
 * @param {HTMLElement} element
 */
function clearError(element) {
  element.textContent = '';
  element.style.display = 'none';
}
