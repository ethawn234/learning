## Linting Configuration Files and Minimal Setup for ESLint and Prettier

### Configuration Files

1. **`.eslintrc`**:
   - ESLint configuration file.
   - Formats: `.eslintrc.json`, `.eslintrc.js`, `.eslintrc.yml`, or `eslintConfig` in `package.json`.
   - Specifies rules, plugins, and environments for ESLint.

2. **`.prettierrc`**:
   - Prettier configuration file.
   - Formats: `.prettierrc`, `.prettierrc.json`, `.prettierrc.yml`, `.prettierrc.js`, or `prettier` in `package.json`.
   - Defines formatting options for Prettier.

3. **`.eslintignore`**:
   - Specifies files/directories to ignore during ESLint checks.
   - Similar format to `.gitignore`.

4. **`.prettierignore`**:
   - Specifies files/directories to ignore during Prettier formatting.
   - Similar format to `.gitignore`.

5. **`.editorconfig`**:
   - Configuration file for editor-related settings.
   - Ensures consistent formatting across different editors/IDEs.

### Interaction

- **ESLint and Prettier**: ESLint checks code for style issues, while Prettier formats code. The `eslint-plugin-prettier` runs Prettier as an ESLint rule, and `eslint-config-prettier` disables ESLint rules that conflict with Prettier.

### Minimal Setup

1. **Install dependencies**:
   ```sh
   npm install --save-dev eslint prettier eslint-plugin-prettier eslint-config-prettier
2. **Create .eslintrc.json**:
```json
{
  "env": {
    "browser": true,
    "es2021": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "prettier"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": 12,
    "sourceType": "module"
  },
  "plugins": ["@typescript-eslint", "prettier"],
  "rules": {
    "prettier/prettier": "error"
  }
}
```
3. **Create .prettierrc:**:
```json
{
  "singleQuote": true,
  "semi": false
}
```
4. **Create .eslintignore:**
```
node_modules
dist
```
5. **Create .prettierignore:**
```
node_modules
dist
```
Summary

    .eslintrc: Configures ESLint with TypeScript support and integrates Prettier.

    .prettierrc: Configures Prettier formatting rules.
    
    .eslintignore & .prettierignore: Specifies ignored files for ESLint and Prettier respectively.

This minimal setup ensures both ESLint and Prettier work together smoothly, with ESLint enforcing code style and Prettier handling code formatting.
